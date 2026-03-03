import json
import os
from datetime import datetime, timezone

import httpx
import yfinance as yf

YFINANCE_INDICATORS = {
    "treasury_10y": {"symbol": "^TNX", "name": "10-Year Treasury Yield", "unit": "%", "divisor": 1},
    "treasury_2y": {"symbol": "^IRX", "name": "13-Week Treasury Bill Rate", "unit": "%", "divisor": 1},
    "vix": {"symbol": "^VIX", "name": "CBOE Volatility Index (VIX)", "unit": "index", "divisor": 1},
    "dollar_index": {"symbol": "DX-Y.NYB", "name": "US Dollar Index (DXY)", "unit": "index", "divisor": 1},
    "gold": {"symbol": "GC=F", "name": "Gold Futures", "unit": "USD/oz", "divisor": 1},
    "oil": {"symbol": "CL=F", "name": "Crude Oil WTI Futures", "unit": "USD/barrel", "divisor": 1},
}

TAVILY_INDICATORS = {
    "interest_rate": {"query": "US Federal Reserve interest rate current", "name": "Federal Funds Rate", "unit": "%"},
    "inflation": {"query": "US inflation rate CPI year over year latest", "name": "US CPI YoY", "unit": "%"},
    "gdp": {"query": "US GDP growth rate quarterly latest", "name": "US GDP Growth Rate", "unit": "%"},
    "unemployment": {"query": "US unemployment rate latest", "name": "US Unemployment Rate", "unit": "%"},
    "pmi": {"query": "US ISM Manufacturing PMI latest", "name": "ISM Manufacturing PMI", "unit": "index"},
}

ALL_INDICATORS = list(YFINANCE_INDICATORS.keys()) + list(TAVILY_INDICATORS.keys())


def register_macro_tools(mcp):
    @mcp.tool()
    async def get_macro_indicators(indicator: str, action: str) -> str:
        """Get macroeconomic indicators from market data (yfinance) and web search (Tavily).

        Args:
            indicator: One of 'treasury_10y', 'treasury_2y', 'vix', 'dollar_index', 'gold', 'oil',
                       'interest_rate', 'inflation', 'gdp', 'unemployment', 'pmi'
            action: One of 'current' (latest value), 'history' (last 30 data points for yfinance indicators),
                    'dashboard' (all key indicators summary)
        """
        try:
            if action == "dashboard":
                dashboard = []
                for ind_key, ind_info in YFINANCE_INDICATORS.items():
                    try:
                        value = _fetch_yfinance_current(ind_info["symbol"])
                        dashboard.append(
                            {"indicator": ind_info["name"], "value": value, "unit": ind_info["unit"], "source": "yfinance"}
                        )
                    except Exception as e:
                        dashboard.append(
                            {
                                "indicator": ind_info["name"],
                                "value": "N/A",
                                "unit": ind_info["unit"],
                                "source": "yfinance",
                                "error": str(e),
                            }
                        )
                for ind_key, ind_info in TAVILY_INDICATORS.items():
                    try:
                        result = await _fetch_tavily_indicator(ind_info["query"], ind_info["name"])
                        dashboard.append(
                            {"indicator": ind_info["name"], "value": result, "unit": ind_info["unit"], "source": "tavily_search"}
                        )
                    except Exception as e:
                        dashboard.append(
                            {
                                "indicator": ind_info["name"],
                                "value": "N/A",
                                "unit": ind_info["unit"],
                                "source": "tavily_search",
                                "error": str(e),
                            }
                        )
                return json.dumps({"macro_dashboard": dashboard, "fetched_at": datetime.now(timezone.utc).isoformat()})

            if indicator not in YFINANCE_INDICATORS and indicator not in TAVILY_INDICATORS:
                return json.dumps({"error": f"Unknown indicator: {indicator}. Available: {ALL_INDICATORS}"})

            if indicator in YFINANCE_INDICATORS:
                ind = YFINANCE_INDICATORS[indicator]
                if action == "current":
                    value = _fetch_yfinance_current(ind["symbol"])
                    return json.dumps({"indicator": ind["name"], "value": value, "unit": ind["unit"], "source": "yfinance"})
                elif action == "history":
                    history = _fetch_yfinance_history(ind["symbol"], period="3mo")
                    return json.dumps(
                        {"indicator": ind["name"], "unit": ind["unit"], "history": history, "source": "yfinance"}
                    )
                else:
                    return json.dumps({"error": f"Unknown action: {action}. Use 'current', 'history', or 'dashboard'."})

            if indicator in TAVILY_INDICATORS:
                ind = TAVILY_INDICATORS[indicator]
                if action == "current":
                    result = await _fetch_tavily_indicator(ind["query"], ind["name"])
                    return json.dumps(
                        {"indicator": ind["name"], "value": result, "unit": ind["unit"], "source": "tavily_search"}
                    )
                elif action == "history":
                    return json.dumps(
                        {
                            "error": f"History not available for '{indicator}'. "
                            f"Tavily-sourced indicators only support 'current' and 'dashboard'."
                        }
                    )
                else:
                    return json.dumps({"error": f"Unknown action: {action}. Use 'current' or 'dashboard'."})

            return json.dumps({"error": f"Unknown action: {action}. Use 'current', 'history', or 'dashboard'."})
        except Exception as e:
            return json.dumps({"error": f"Macro indicator error: {str(e)}"})


def _fetch_yfinance_current(symbol: str) -> float:
    ticker = yf.Ticker(symbol)
    info = ticker.info
    price = info.get("regularMarketPrice") or info.get("previousClose")
    if price is None:
        hist = ticker.history(period="5d")
        if hist.empty:
            raise ValueError(f"No data available for {symbol}")
        price = float(hist["Close"].iloc[-1])
    return round(float(price), 4)


def _fetch_yfinance_history(symbol: str, period: str = "3mo") -> list:
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period)
    if hist.empty:
        raise ValueError(f"No historical data for {symbol}")
    result = []
    for date, row in hist.iterrows():
        result.append({"date": date.strftime("%Y-%m-%d"), "value": round(float(row["Close"]), 4)})
    return result


async def _fetch_tavily_indicator(query: str, indicator_name: str) -> str:
    tavily_key = os.environ.get("TAVILY_API_KEY", "")
    if not tavily_key:
        raise ValueError("TAVILY_API_KEY not set — required for macro indicator search")
    async with httpx.AsyncClient(timeout=15.0) as client:
        resp = await client.post(
            "https://api.tavily.com/search",
            json={
                "api_key": tavily_key,
                "query": query,
                "search_depth": "basic",
                "include_answer": True,
                "max_results": 3,
            },
        )
        resp.raise_for_status()
        data = resp.json()
        answer = data.get("answer", "")
        if answer:
            return f"{indicator_name}: {answer}"
        results = data.get("results", [])
        if results:
            return f"{indicator_name}: {results[0].get('content', 'No data found')[:500]}"
        return f"{indicator_name}: No current data found"

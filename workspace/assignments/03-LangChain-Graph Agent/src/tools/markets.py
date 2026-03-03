import json

import yfinance as yf

COMMON_SYMBOLS = {
    "sp500": "^GSPC",
    "dow": "^DJI",
    "nasdaq": "^IXIC",
    "dax": "^GDAXI",
    "ftse": "^FTSE",
    "nikkei": "^N225",
    "eurusd": "EURUSD=X",
    "gold": "GC=F",
    "oil": "CL=F",
}


def register_market_tools(mcp):
    @mcp.tool()
    def get_market_data(symbol: str, action: str, period: str = "1mo") -> str:
        """Get global market data from Yahoo Finance.

        Args:
            symbol: Ticker symbol (e.g., '^GSPC', 'AAPL', 'EURUSD=X') or alias ('sp500', 'gold', 'oil')
            action: One of 'quote' (current price + stats), 'history' (price history), 'compare' (multiple symbols comma-separated)
            period: History period for 'history' action — '1mo', '3mo', '6mo', '1y' (default: '1mo')
        """
        try:
            resolved = COMMON_SYMBOLS.get(symbol.lower(), symbol)

            if action == "quote":
                ticker = yf.Ticker(resolved)
                info = ticker.info
                return json.dumps(
                    {
                        "symbol": resolved,
                        "name": info.get("shortName", resolved),
                        "price": info.get("regularMarketPrice"),
                        "change_pct": round(info.get("regularMarketChangePercent", 0) or 0, 2),
                        "volume": info.get("regularMarketVolume"),
                        "high_52w": info.get("fiftyTwoWeekHigh"),
                        "low_52w": info.get("fiftyTwoWeekLow"),
                        "pe_ratio": info.get("trailingPE"),
                        "market_cap": info.get("marketCap"),
                    }
                )
            elif action == "history":
                ticker = yf.Ticker(resolved)
                hist = ticker.history(period=period)
                if hist.empty:
                    return json.dumps({"error": f"No history found for {resolved}"})
                records = [
                    {"date": str(idx.date()), "close": round(float(row["Close"]), 2), "volume": int(row["Volume"])}
                    for idx, row in hist.iterrows()
                ]
                return json.dumps({"symbol": resolved, "period": period, "data": records})
            elif action == "compare":
                symbols = [COMMON_SYMBOLS.get(s.strip().lower(), s.strip()) for s in resolved.split(",")]
                comparison = []
                for sym in symbols:
                    t = yf.Ticker(sym)
                    info = t.info
                    comparison.append(
                        {
                            "symbol": sym,
                            "name": info.get("shortName", sym),
                            "price": info.get("regularMarketPrice"),
                            "change_pct": round(info.get("regularMarketChangePercent", 0) or 0, 2),
                        }
                    )
                return json.dumps({"comparison": comparison})
            else:
                return json.dumps({"error": f"Unknown action: {action}. Use 'quote', 'history', or 'compare'."})
        except Exception as e:
            return json.dumps({"error": f"Yahoo Finance error: {str(e)}"})

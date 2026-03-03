import json

import httpx
import numpy as np
import pandas as pd
import yfinance as yf

COINGECKO_BASE = "https://api.coingecko.com/api/v3"


def register_analysis_tools(mcp):
    @mcp.tool()
    async def technical_analysis(
        symbol: str, asset_type: str, indicators: str = "rsi,sma_20,sma_50,macd,bollinger"
    ) -> str:
        """Compute technical analysis indicators for a given asset.

        Args:
            symbol: Asset identifier — CoinGecko ID for crypto ('bitcoin') or ticker for stocks ('^GSPC', 'AAPL')
            asset_type: 'crypto' or 'stock' — determines data source
            indicators: Comma-separated list of indicators: rsi, sma_20, sma_50, ema_12, ema_26, macd, bollinger, volatility (default: rsi,sma_20,sma_50,macd,bollinger)
        """
        try:
            prices = await _fetch_prices(symbol, asset_type, days=90)
            if prices is None or len(prices) < 30:
                return json.dumps({"error": f"Insufficient price data for {symbol}. Need at least 30 days."})

            close = pd.Series(prices)
            requested = [i.strip() for i in indicators.split(",")]
            results = {
                "symbol": symbol,
                "asset_type": asset_type,
                "data_points": len(close),
                "current_price": round(float(close.iloc[-1]), 2),
                "indicators": {},
            }

            for ind in requested:
                if ind == "rsi":
                    rsi_val = _calc_rsi(close)
                    if rsi_val > 70:
                        interp = "Overbought — potential reversal or correction"
                    elif rsi_val < 30:
                        interp = "Oversold — potential bounce or recovery"
                    else:
                        interp = "Neutral range"
                    results["indicators"]["rsi"] = {"value": round(rsi_val, 1), "interpretation": interp}
                elif ind == "sma_20":
                    sma = round(float(close.rolling(20).mean().iloc[-1]), 2)
                    pos = "above" if close.iloc[-1] > sma else "below"
                    results["indicators"]["sma_20"] = {"value": sma, "interpretation": f"Price is {pos} 20-day SMA"}
                elif ind == "sma_50":
                    sma = round(float(close.rolling(50).mean().iloc[-1]), 2)
                    pos = "above" if close.iloc[-1] > sma else "below"
                    trend = "Bullish trend" if pos == "above" else "Bearish trend"
                    results["indicators"]["sma_50"] = {
                        "value": sma,
                        "interpretation": f"{trend} ({pos} 50-day moving average)",
                    }
                elif ind == "ema_12":
                    ema = round(float(close.ewm(span=12).mean().iloc[-1]), 2)
                    results["indicators"]["ema_12"] = {"value": ema}
                elif ind == "ema_26":
                    ema = round(float(close.ewm(span=26).mean().iloc[-1]), 2)
                    results["indicators"]["ema_26"] = {"value": ema}
                elif ind == "macd":
                    macd_line = close.ewm(span=12).mean() - close.ewm(span=26).mean()
                    signal = macd_line.ewm(span=9).mean()
                    histogram = macd_line - signal
                    hist_val = round(float(histogram.iloc[-1]), 4)
                    prev_hist = round(float(histogram.iloc[-2]), 4)
                    if hist_val > 0 and hist_val > prev_hist:
                        interp = "Bullish momentum building"
                    elif hist_val < 0 and hist_val < prev_hist:
                        interp = "Bearish momentum building"
                    elif hist_val > 0:
                        interp = "Bullish but weakening"
                    else:
                        interp = "Bearish but weakening"
                    results["indicators"]["macd"] = {
                        "macd_line": round(float(macd_line.iloc[-1]), 4),
                        "signal_line": round(float(signal.iloc[-1]), 4),
                        "histogram": hist_val,
                        "interpretation": interp,
                    }
                elif ind == "bollinger":
                    sma20 = close.rolling(20).mean()
                    std20 = close.rolling(20).std()
                    upper = round(float((sma20 + 2 * std20).iloc[-1]), 2)
                    lower = round(float((sma20 - 2 * std20).iloc[-1]), 2)
                    mid = round(float(sma20.iloc[-1]), 2)
                    price = float(close.iloc[-1])
                    if price > upper:
                        interp = "Price above upper band — overbought signal"
                    elif price < lower:
                        interp = "Price below lower band — oversold signal"
                    else:
                        interp = "Price within bands — normal range"
                    results["indicators"]["bollinger"] = {
                        "upper": upper,
                        "middle": mid,
                        "lower": lower,
                        "interpretation": interp,
                    }
                elif ind == "volatility":
                    returns = close.pct_change().dropna()
                    vol = round(float(returns.std() * np.sqrt(365 if asset_type == "crypto" else 252) * 100), 1)
                    level = "High" if vol > 50 else "Moderate" if vol > 20 else "Low"
                    results["indicators"]["volatility"] = {
                        "annualized_pct": vol,
                        "interpretation": f"{level} volatility at {vol}%",
                    }

            return json.dumps(results)
        except Exception as e:
            return json.dumps({"error": f"Technical analysis error: {str(e)}"})


def _calc_rsi(prices: pd.Series, period: int = 14) -> float:
    delta = prices.diff()
    gain = delta.where(delta > 0, 0.0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0.0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return float(rsi.iloc[-1])


async def _fetch_prices(symbol: str, asset_type: str, days: int = 90) -> list | None:
    if asset_type == "crypto":
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.get(
                    f"{COINGECKO_BASE}/coins/{symbol}/market_chart",
                    params={"vs_currency": "usd", "days": str(days), "interval": "daily"},
                )
                if resp.status_code != 200:
                    return None
                return [p[1] for p in resp.json()["prices"]]
        except Exception:
            return None
    elif asset_type == "stock":
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=f"{days}d")
            if hist.empty:
                return None
            return hist["Close"].tolist()
        except Exception:
            return None
    return None

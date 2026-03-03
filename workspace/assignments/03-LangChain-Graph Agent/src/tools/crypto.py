import json

import httpx

COINGECKO_BASE = "https://api.coingecko.com/api/v3"


def register_crypto_tools(mcp):
    @mcp.tool()
    async def get_crypto_data(symbol: str, action: str) -> str:
        """Get cryptocurrency market data from CoinGecko.

        Args:
            symbol: CoinGecko cryptocurrency ID (e.g., 'bitcoin', 'ethereum', 'solana')
            action: One of 'price' (current price + 24h stats), 'history' (30-day daily prices), 'market_overview' (top 10 by market cap)
        """
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                if action == "price":
                    resp = await client.get(
                        f"{COINGECKO_BASE}/simple/price",
                        params={
                            "ids": symbol,
                            "vs_currencies": "usd",
                            "include_24hr_change": "true",
                            "include_market_cap": "true",
                            "include_24hr_vol": "true",
                        },
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    if symbol not in data:
                        return json.dumps(
                            {"error": f"Unknown symbol: {symbol}. Use CoinGecko IDs like 'bitcoin', 'ethereum'."}
                        )
                    d = data[symbol]
                    return json.dumps(
                        {
                            "symbol": symbol,
                            "price_usd": d["usd"],
                            "change_24h_pct": round(d.get("usd_24h_change", 0), 2),
                            "market_cap_usd": d.get("usd_market_cap"),
                            "volume_24h_usd": d.get("usd_24h_vol"),
                        }
                    )
                elif action == "history":
                    resp = await client.get(
                        f"{COINGECKO_BASE}/coins/{symbol}/market_chart",
                        params={"vs_currency": "usd", "days": "30", "interval": "daily"},
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    prices = [{"date": p[0], "price": round(p[1], 2)} for p in data["prices"]]
                    return json.dumps({"symbol": symbol, "period": "30d", "prices": prices})
                elif action == "market_overview":
                    resp = await client.get(
                        f"{COINGECKO_BASE}/coins/markets",
                        params={
                            "vs_currency": "usd",
                            "order": "market_cap_desc",
                            "per_page": "10",
                            "page": "1",
                            "sparkline": "false",
                            "price_change_percentage": "24h,7d,30d",
                        },
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    overview = [
                        {
                            "rank": i + 1,
                            "name": c["name"],
                            "symbol": c["symbol"].upper(),
                            "price": c["current_price"],
                            "change_24h": round(c.get("price_change_percentage_24h_in_currency", 0) or 0, 2),
                            "change_7d": round(c.get("price_change_percentage_7d_in_currency", 0) or 0, 2),
                            "market_cap": c["market_cap"],
                        }
                        for i, c in enumerate(data)
                    ]
                    return json.dumps({"top_10_crypto": overview})
                else:
                    return json.dumps(
                        {"error": f"Unknown action: {action}. Use 'price', 'history', or 'market_overview'."}
                    )
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                return json.dumps({"error": "Rate limited by CoinGecko. Try again in 60 seconds."})
            return json.dumps({"error": f"CoinGecko API error: {e.response.status_code}"})
        except httpx.TimeoutException:
            return json.dumps({"error": "Request timed out. Try again."})
        except Exception as e:
            return json.dumps({"error": f"Unexpected error: {str(e)}"})

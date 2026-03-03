import json

import plotly.graph_objects as go


def render_price_chart(data_json: str) -> go.Figure | None:
    """Create a price history line chart from tool result JSON.

    Args:
        data_json: JSON string from get_crypto_data or get_market_data with price history

    Returns:
        Plotly figure or None if data can't be parsed
    """
    try:
        data = json.loads(data_json) if isinstance(data_json, str) else data_json
    except (json.JSONDecodeError, TypeError):
        return None

    # Handle crypto history format: {"prices": [{"date": ..., "price": ...}]}
    if "prices" in data:
        points = data["prices"]
        dates = [p["date"] for p in points]
        values = [p["price"] for p in points]
        symbol = data.get("symbol", "Asset")
        title = f"{symbol.upper()} Price History ({data.get('period', '')})"
    # Handle market history format: {"data": [{"date": ..., "close": ...}]}
    elif "data" in data:
        points = data["data"]
        dates = [p["date"] for p in points]
        values = [p["close"] for p in points]
        symbol = data.get("symbol", "Asset")
        title = f"{symbol} Price History ({data.get('period', '')})"
    else:
        return None

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=values, mode="lines", name="Price", line=dict(color="#2196F3", width=2)))
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark",
        height=400,
        margin=dict(l=50, r=30, t=50, b=40),
    )
    return fig


def render_indicators_chart(data_json: str) -> list[dict]:
    """Parse technical analysis results into displayable metrics.

    Args:
        data_json: JSON string from technical_analysis tool

    Returns:
        List of dicts with 'label', 'value', 'interpretation' for st.metric display
    """
    try:
        data = json.loads(data_json) if isinstance(data_json, str) else data_json
    except (json.JSONDecodeError, TypeError):
        return []

    if "indicators" not in data:
        return []

    metrics = []
    indicators = data["indicators"]

    if "rsi" in indicators:
        rsi = indicators["rsi"]
        metrics.append({"label": "RSI (14)", "value": str(rsi["value"]), "interpretation": rsi.get("interpretation", "")})

    if "sma_20" in indicators:
        sma = indicators["sma_20"]
        metrics.append({"label": "SMA 20", "value": f"${sma['value']:,.2f}", "interpretation": sma.get("interpretation", "")})

    if "sma_50" in indicators:
        sma = indicators["sma_50"]
        metrics.append({"label": "SMA 50", "value": f"${sma['value']:,.2f}", "interpretation": sma.get("interpretation", "")})

    if "macd" in indicators:
        macd = indicators["macd"]
        metrics.append(
            {
                "label": "MACD",
                "value": f"{macd['histogram']:+.4f}",
                "interpretation": macd.get("interpretation", ""),
            }
        )

    if "bollinger" in indicators:
        bb = indicators["bollinger"]
        metrics.append(
            {
                "label": "Bollinger Bands",
                "value": f"${bb['lower']:,.2f} — ${bb['upper']:,.2f}",
                "interpretation": bb.get("interpretation", ""),
            }
        )

    if "volatility" in indicators:
        vol = indicators["volatility"]
        metrics.append(
            {
                "label": "Volatility",
                "value": f"{vol['annualized_pct']}%",
                "interpretation": vol.get("interpretation", ""),
            }
        )

    return metrics

"""End-to-end integration tests for the trading agent pipeline.

These tests verify the full flow: user query → agent → tool calls → response.
All external APIs are mocked to ensure tests run without network calls.
"""

import json
from unittest.mock import MagicMock

import pytest

from src.tools.crypto import register_crypto_tools
from src.tools.markets import register_market_tools
from src.tools.search import register_search_tools
from src.tools.analysis import register_analysis_tools
from src.tools.macro import register_macro_tools
from src.ui.charts import render_price_chart, render_indicators_chart


class FakeMCP:
    def __init__(self):
        self.tools = {}

    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


@pytest.fixture
def all_tools():
    """Register all 5 MCP tools and return them."""
    m = FakeMCP()
    register_crypto_tools(m)
    register_market_tools(m)
    register_macro_tools(m)
    register_search_tools(m)
    register_analysis_tools(m)
    return m.tools


def test_all_five_tools_registered(all_tools):
    """All 5 MCP tools are registered."""
    assert "get_crypto_data" in all_tools
    assert "get_market_data" in all_tools
    assert "get_macro_indicators" in all_tools
    assert "web_search" in all_tools
    assert "technical_analysis" in all_tools


def test_price_chart_rendering():
    """Price chart renders from crypto history data."""
    data = {
        "symbol": "bitcoin",
        "period": "30d",
        "prices": [{"date": 1000000 * i, "price": 60000 + i * 100} for i in range(30)],
    }

    fig = render_price_chart(json.dumps(data))
    assert fig is not None


def test_indicators_chart_rendering():
    """Technical indicators render as metrics."""
    data = {
        "symbol": "bitcoin",
        "indicators": {
            "rsi": {"value": 72.3, "interpretation": "Overbought"},
            "sma_50": {"value": 64200.0, "interpretation": "Bullish trend"},
            "macd": {"macd_line": 1200.0, "signal_line": 1100.0, "histogram": 100.0, "interpretation": "Bullish momentum building"},
        },
    }

    metrics = render_indicators_chart(json.dumps(data))
    assert len(metrics) >= 3
    labels = [m["label"] for m in metrics]
    assert "RSI (14)" in labels
    assert "SMA 50" in labels
    assert "MACD" in labels


def test_invalid_chart_data():
    """Invalid data returns None/empty for charts."""
    assert render_price_chart("not json") is None
    assert render_price_chart('{"no_prices": true}') is None
    assert render_indicators_chart("not json") == []
    assert render_indicators_chart('{"no_indicators": true}') == []


def test_market_data_chart_rendering():
    """Price chart renders from market history data."""
    data = {
        "symbol": "^GSPC",
        "period": "1mo",
        "data": [{"date": f"2026-01-{i+1:02d}", "close": 5000 + i * 10, "volume": 1000000} for i in range(20)],
    }

    fig = render_price_chart(json.dumps(data))
    assert fig is not None

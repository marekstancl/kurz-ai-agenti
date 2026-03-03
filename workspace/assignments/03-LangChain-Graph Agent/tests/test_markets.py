import json
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.tools.markets import register_market_tools


class FakeMCP:
    def __init__(self):
        self.tools = {}

    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


@pytest.fixture
def mcp():
    m = FakeMCP()
    register_market_tools(m)
    return m


@pytest.fixture
def get_market_data(mcp):
    return mcp.tools["get_market_data"]


def test_quote_returns_valid_json(get_market_data):
    mock_info = {
        "shortName": "S&P 500",
        "regularMarketPrice": 5200.50,
        "regularMarketChangePercent": 0.75,
        "regularMarketVolume": 3500000000,
        "fiftyTwoWeekHigh": 5300.0,
        "fiftyTwoWeekLow": 4100.0,
        "trailingPE": 24.5,
        "marketCap": None,
    }

    with patch("src.tools.markets.yf.Ticker") as mock_ticker:
        mock_ticker.return_value.info = mock_info
        result = get_market_data("^GSPC", "quote")
        data = json.loads(result)

        assert data["symbol"] == "^GSPC"
        assert data["name"] == "S&P 500"
        assert data["price"] == 5200.50
        assert data["change_pct"] == 0.75
        assert "volume" in data


def test_alias_resolution(get_market_data):
    mock_info = {
        "shortName": "S&P 500",
        "regularMarketPrice": 5200.50,
        "regularMarketChangePercent": 0.75,
        "regularMarketVolume": 3500000000,
    }

    with patch("src.tools.markets.yf.Ticker") as mock_ticker:
        mock_ticker.return_value.info = mock_info
        result = get_market_data("sp500", "quote")
        data = json.loads(result)

        assert data["symbol"] == "^GSPC"
        mock_ticker.assert_called_with("^GSPC")


def test_history_returns_records(get_market_data):
    dates = pd.date_range("2026-01-01", periods=20, freq="D")
    hist_df = pd.DataFrame(
        {"Close": [5000 + i * 10 for i in range(20)], "Volume": [1000000] * 20},
        index=dates,
    )

    with patch("src.tools.markets.yf.Ticker") as mock_ticker:
        mock_ticker.return_value.history.return_value = hist_df
        result = get_market_data("^GSPC", "history")
        data = json.loads(result)

        assert data["symbol"] == "^GSPC"
        assert data["period"] == "1mo"
        assert len(data["data"]) == 20
        assert "date" in data["data"][0]
        assert "close" in data["data"][0]


def test_empty_history_returns_error(get_market_data):
    with patch("src.tools.markets.yf.Ticker") as mock_ticker:
        mock_ticker.return_value.history.return_value = pd.DataFrame()
        result = get_market_data("INVALID", "history")
        data = json.loads(result)

        assert "error" in data


def test_unknown_action_returns_error(get_market_data):
    result = get_market_data("^GSPC", "invalid_action")
    data = json.loads(result)

    assert "error" in data
    assert "invalid_action" in data["error"]


def test_compare_multiple_symbols(get_market_data):
    mock_info_1 = {"shortName": "Apple", "regularMarketPrice": 180.0, "regularMarketChangePercent": 1.5}
    mock_info_2 = {"shortName": "Google", "regularMarketPrice": 140.0, "regularMarketChangePercent": -0.5}

    with patch("src.tools.markets.yf.Ticker") as mock_ticker:
        mock_ticker.return_value.info = mock_info_1
        # For compare, the symbol resolution happens first
        result = get_market_data("AAPL,GOOGL", "compare")
        data = json.loads(result)

        assert "comparison" in data

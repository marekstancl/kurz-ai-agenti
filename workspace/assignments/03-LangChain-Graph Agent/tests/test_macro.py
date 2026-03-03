import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.tools.macro import register_macro_tools


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
    register_macro_tools(m)
    return m


@pytest.fixture
def get_macro_indicators(mcp):
    return mcp.tools["get_macro_indicators"]


@pytest.mark.asyncio
async def test_yfinance_current(get_macro_indicators):
    with patch("src.tools.macro._fetch_yfinance_current", return_value=4.35):
        result = await get_macro_indicators("treasury_10y", "current")
        data = json.loads(result)

        assert data["indicator"] == "10-Year Treasury Yield"
        assert data["value"] == 4.35
        assert data["unit"] == "%"
        assert data["source"] == "yfinance"


@pytest.mark.asyncio
async def test_yfinance_history(get_macro_indicators):
    mock_history = [
        {"date": "2026-01-01", "value": 4.3},
        {"date": "2026-01-02", "value": 4.35},
    ]

    with patch("src.tools.macro._fetch_yfinance_history", return_value=mock_history):
        result = await get_macro_indicators("vix", "history")
        data = json.loads(result)

        assert "history" in data
        assert data["source"] == "yfinance"
        assert len(data["history"]) == 2


@pytest.mark.asyncio
async def test_tavily_current(get_macro_indicators):
    with patch("src.tools.macro._fetch_tavily_indicator", new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = "Federal Funds Rate: 5.25-5.50%"
        result = await get_macro_indicators("interest_rate", "current")
        data = json.loads(result)

        assert data["indicator"] == "Federal Funds Rate"
        assert "5.25" in data["value"] or "Federal Funds Rate" in data["value"]
        assert data["source"] == "tavily_search"


@pytest.mark.asyncio
async def test_tavily_history_not_available(get_macro_indicators):
    result = await get_macro_indicators("inflation", "history")
    data = json.loads(result)

    assert "error" in data
    assert "not available" in data["error"].lower() or "History not available" in data["error"]


@pytest.mark.asyncio
async def test_unknown_indicator_returns_error(get_macro_indicators):
    result = await get_macro_indicators("invalid", "current")
    data = json.loads(result)

    assert "error" in data
    assert "invalid" in data["error"]
    assert "Available" in data["error"]


@pytest.mark.asyncio
async def test_dashboard(get_macro_indicators):
    with (
        patch("src.tools.macro._fetch_yfinance_current", return_value=4.35),
        patch("src.tools.macro._fetch_tavily_indicator", new_callable=AsyncMock, return_value="Fed Rate: 5.50%"),
    ):
        result = await get_macro_indicators("treasury_10y", "dashboard")
        data = json.loads(result)

        assert "macro_dashboard" in data
        assert "fetched_at" in data
        assert len(data["macro_dashboard"]) > 0

        sources = {item["source"] for item in data["macro_dashboard"]}
        assert "yfinance" in sources
        assert "tavily_search" in sources

import json
from unittest.mock import AsyncMock, patch

import numpy as np
import pytest

from src.tools.analysis import _calc_rsi, register_analysis_tools

import pandas as pd


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
    register_analysis_tools(m)
    return m


@pytest.fixture
def technical_analysis(mcp):
    return mcp.tools["technical_analysis"]


@pytest.mark.asyncio
async def test_default_indicators(technical_analysis):
    prices = [60000 + i * 100 + np.sin(i) * 500 for i in range(91)]

    with patch("src.tools.analysis._fetch_prices", new_callable=AsyncMock, return_value=prices):
        result = await technical_analysis("bitcoin", "crypto")
        data = json.loads(result)

        assert data["symbol"] == "bitcoin"
        assert data["asset_type"] == "crypto"
        assert data["data_points"] == 91
        assert "rsi" in data["indicators"]
        assert "sma_20" in data["indicators"]
        assert "sma_50" in data["indicators"]
        assert "macd" in data["indicators"]
        assert "bollinger" in data["indicators"]


@pytest.mark.asyncio
async def test_specific_indicators(technical_analysis):
    prices = [60000 + i * 100 for i in range(91)]

    with patch("src.tools.analysis._fetch_prices", new_callable=AsyncMock, return_value=prices):
        result = await technical_analysis("bitcoin", "crypto", "rsi,sma_50,macd")
        data = json.loads(result)

        assert "rsi" in data["indicators"]
        assert "sma_50" in data["indicators"]
        assert "macd" in data["indicators"]
        assert "sma_20" not in data["indicators"]
        assert "bollinger" not in data["indicators"]


@pytest.mark.asyncio
async def test_insufficient_data(technical_analysis):
    with patch("src.tools.analysis._fetch_prices", new_callable=AsyncMock, return_value=[100, 200]):
        result = await technical_analysis("nonexistent", "crypto")
        data = json.loads(result)

        assert "error" in data
        assert "Insufficient" in data["error"]


@pytest.mark.asyncio
async def test_no_data(technical_analysis):
    with patch("src.tools.analysis._fetch_prices", new_callable=AsyncMock, return_value=None):
        result = await technical_analysis("nonexistent", "crypto")
        data = json.loads(result)

        assert "error" in data


def test_rsi_monotonic_increase():
    """Monotonically increasing prices should produce RSI near 100."""
    prices = pd.Series([100 + i for i in range(50)])
    rsi = _calc_rsi(prices)
    assert rsi > 95


def test_rsi_monotonic_decrease():
    """Monotonically decreasing prices should produce RSI near 0."""
    prices = pd.Series([100 - i * 0.5 for i in range(50)])
    rsi = _calc_rsi(prices)
    assert rsi < 5


def test_rsi_neutral():
    """Alternating up/down prices should produce RSI near 50."""
    prices = pd.Series([100 + (1 if i % 2 == 0 else -1) for i in range(50)])
    rsi = _calc_rsi(prices)
    assert 40 < rsi < 60


@pytest.mark.asyncio
async def test_macd_bullish(technical_analysis):
    """Rising prices should show bullish MACD."""
    prices = [50000 + i * 200 for i in range(91)]

    with patch("src.tools.analysis._fetch_prices", new_callable=AsyncMock, return_value=prices):
        result = await technical_analysis("bitcoin", "crypto", "macd")
        data = json.loads(result)

        macd = data["indicators"]["macd"]
        assert "Bullish" in macd["interpretation"]


@pytest.mark.asyncio
async def test_macd_bearish(technical_analysis):
    """Falling prices should show bearish MACD."""
    prices = [80000 - i * 200 for i in range(91)]

    with patch("src.tools.analysis._fetch_prices", new_callable=AsyncMock, return_value=prices):
        result = await technical_analysis("bitcoin", "crypto", "macd")
        data = json.loads(result)

        macd = data["indicators"]["macd"]
        assert "Bearish" in macd["interpretation"]


@pytest.mark.asyncio
async def test_interpretation_strings_present(technical_analysis):
    prices = [60000 + i * 100 + np.sin(i) * 500 for i in range(91)]

    with patch("src.tools.analysis._fetch_prices", new_callable=AsyncMock, return_value=prices):
        result = await technical_analysis("bitcoin", "crypto", "rsi,sma_50,macd,bollinger")
        data = json.loads(result)

        assert "interpretation" in data["indicators"]["rsi"]
        assert "interpretation" in data["indicators"]["sma_50"]
        assert "interpretation" in data["indicators"]["macd"]
        assert "interpretation" in data["indicators"]["bollinger"]

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import pytest_asyncio

from src.tools.crypto import register_crypto_tools


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
    register_crypto_tools(m)
    return m


@pytest.fixture
def get_crypto_data(mcp):
    return mcp.tools["get_crypto_data"]


@pytest.mark.asyncio
async def test_price_returns_valid_json(get_crypto_data):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = {
        "bitcoin": {
            "usd": 67420.0,
            "usd_24h_change": -2.1,
            "usd_market_cap": 1320000000000,
            "usd_24h_vol": 28000000000,
        }
    }

    with patch("src.tools.crypto.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.get = AsyncMock(return_value=mock_response)
        mock_instance.__aenter__ = AsyncMock(return_value=mock_instance)
        mock_instance.__aexit__ = AsyncMock(return_value=False)
        mock_client.return_value = mock_instance

        result = await get_crypto_data("bitcoin", "price")
        data = json.loads(result)

        assert data["symbol"] == "bitcoin"
        assert data["price_usd"] == 67420.0
        assert data["change_24h_pct"] == -2.1
        assert "market_cap_usd" in data
        assert "volume_24h_usd" in data


@pytest.mark.asyncio
async def test_history_returns_data_points(get_crypto_data):
    mock_prices = [[1000000 * i, 60000 + i * 100] for i in range(31)]
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = {"prices": mock_prices}

    with patch("src.tools.crypto.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.get = AsyncMock(return_value=mock_response)
        mock_instance.__aenter__ = AsyncMock(return_value=mock_instance)
        mock_instance.__aexit__ = AsyncMock(return_value=False)
        mock_client.return_value = mock_instance

        result = await get_crypto_data("bitcoin", "history")
        data = json.loads(result)

        assert data["symbol"] == "bitcoin"
        assert data["period"] == "30d"
        assert len(data["prices"]) == 31
        assert "date" in data["prices"][0]
        assert "price" in data["prices"][0]


@pytest.mark.asyncio
async def test_unknown_symbol_returns_error(get_crypto_data):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = {}

    with patch("src.tools.crypto.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.get = AsyncMock(return_value=mock_response)
        mock_instance.__aenter__ = AsyncMock(return_value=mock_instance)
        mock_instance.__aexit__ = AsyncMock(return_value=False)
        mock_client.return_value = mock_instance

        result = await get_crypto_data("nonexistent", "price")
        data = json.loads(result)

        assert "error" in data
        assert "nonexistent" in data["error"]


@pytest.mark.asyncio
async def test_unknown_action_returns_error(get_crypto_data):
    with patch("src.tools.crypto.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.__aenter__ = AsyncMock(return_value=mock_instance)
        mock_instance.__aexit__ = AsyncMock(return_value=False)
        mock_client.return_value = mock_instance

        result = await get_crypto_data("bitcoin", "invalid_action")
        data = json.loads(result)

        assert "error" in data
        assert "invalid_action" in data["error"]


@pytest.mark.asyncio
async def test_market_overview(get_crypto_data):
    mock_data = [
        {
            "name": "Bitcoin",
            "symbol": "btc",
            "current_price": 67420,
            "price_change_percentage_24h_in_currency": -2.1,
            "price_change_percentage_7d_in_currency": 5.3,
            "market_cap": 1320000000000,
        }
    ]
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = mock_data

    with patch("src.tools.crypto.httpx.AsyncClient") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.get = AsyncMock(return_value=mock_response)
        mock_instance.__aenter__ = AsyncMock(return_value=mock_instance)
        mock_instance.__aexit__ = AsyncMock(return_value=False)
        mock_client.return_value = mock_instance

        result = await get_crypto_data("bitcoin", "market_overview")
        data = json.loads(result)

        assert "top_10_crypto" in data
        assert data["top_10_crypto"][0]["name"] == "Bitcoin"
        assert data["top_10_crypto"][0]["symbol"] == "BTC"

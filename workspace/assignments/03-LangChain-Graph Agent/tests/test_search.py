import json
from unittest.mock import MagicMock, patch

import pytest

from src.tools.search import register_search_tools


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
    register_search_tools(m)
    return m


@pytest.fixture
def web_search(mcp):
    return mcp.tools["web_search"]


def test_news_search_returns_results(web_search):
    mock_results = {
        "results": [
            {"title": "Bitcoin ETF Sees Record Inflows", "url": "https://example.com/1", "content": "Bitcoin ETFs saw record inflows of $1.2 billion..."},
            {"title": "Crypto Market Rallies", "url": "https://example.com/2", "content": "The crypto market saw broad-based gains..."},
        ]
    }

    with patch("src.tools.search.TavilyClient") as mock_client:
        mock_instance = MagicMock()
        mock_instance.search.return_value = mock_results
        mock_client.return_value = mock_instance

        result = web_search("Bitcoin ETF news", "news")
        data = json.loads(result)

        assert data["query"] == "Bitcoin ETF news"
        assert data["count"] == 2
        assert len(data["results"]) == 2
        assert "title" in data["results"][0]
        assert "url" in data["results"][0]
        assert "snippet" in data["results"][0]


def test_invalid_search_type_defaults(web_search):
    mock_results = {"results": [{"title": "Test", "url": "https://example.com", "content": "Test content"}]}

    with patch("src.tools.search.TavilyClient") as mock_client:
        mock_instance = MagicMock()
        mock_instance.search.return_value = mock_results
        mock_client.return_value = mock_instance

        result = web_search("test query", "invalid_type")
        data = json.loads(result)

        # Should not crash, defaults to general
        assert "error" not in data
        assert data["count"] >= 1


def test_empty_results(web_search):
    with patch("src.tools.search.TavilyClient") as mock_client:
        mock_instance = MagicMock()
        mock_instance.search.return_value = {"results": []}
        mock_client.return_value = mock_instance

        result = web_search("very obscure query", "general")
        data = json.loads(result)

        assert data["count"] == 0
        assert data["results"] == []


def test_missing_api_key(web_search):
    with patch.dict("os.environ", {"TAVILY_API_KEY": ""}):
        result = web_search("test", "news")
        data = json.loads(result)

        assert "error" in data

import json
from datetime import datetime, timezone, timedelta
from unittest.mock import MagicMock, patch

import pytest


def _make_mock_qdrant():
    """Create a mock QdrantClient with basic collection behavior."""
    mock = MagicMock()
    mock.get_collections.return_value = MagicMock(collections=[])
    mock.create_collection = MagicMock()
    mock.upsert = MagicMock()
    return mock


def _make_mock_openai():
    """Create a mock OpenAI client with embedding support."""
    mock = MagicMock()
    mock_embedding = MagicMock()
    mock_embedding.data = [MagicMock(embedding=[0.1] * 1536)]
    mock.embeddings.create.return_value = mock_embedding
    return mock


@pytest.fixture
def memory_manager():
    with (
        patch("src.agent.memory.QdrantClient", return_value=_make_mock_qdrant()),
        patch("src.agent.memory.OpenAI", return_value=_make_mock_openai()),
    ):
        from src.agent.memory import MemoryManager
        mm = MemoryManager()
        return mm


def test_creates_collections(memory_manager):
    """MemoryManager creates both collections on init."""
    assert memory_manager.available is True
    assert memory_manager.qdrant.create_collection.call_count == 2


def test_store_analysis(memory_manager):
    """store_analysis inserts a point into Qdrant."""
    memory_manager.store_analysis(
        query="What is Bitcoin price?",
        response="Bitcoin is currently at $67,420...",
        summary="BTC at $67,420, down 2.1%",
        assets=["BTC"],
        sentiment="bearish",
        tools_used=["get_crypto_data"],
        reasoning_steps=2,
    )

    memory_manager.qdrant.upsert.assert_called_once()
    call_args = memory_manager.qdrant.upsert.call_args
    assert call_args.kwargs["collection_name"] == "analyses"


def test_retrieve_context_with_results(memory_manager):
    """retrieve_context returns formatted string when results exist."""
    mock_point = MagicMock()
    mock_point.payload = {
        "query": "Bitcoin analysis",
        "summary": "BTC at $67k, bearish short-term",
        "sentiment": "bearish",
        "assets": ["BTC"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    mock_result = MagicMock()
    mock_result.points = [mock_point]
    memory_manager.qdrant.query_points.return_value = mock_result

    context = memory_manager.retrieve_context("Bitcoin analysis")

    assert "Previous relevant analyses" in context
    assert "BTC" in context


def test_retrieve_context_empty(memory_manager):
    """retrieve_context returns empty string when no results."""
    mock_result = MagicMock()
    mock_result.points = []
    memory_manager.qdrant.query_points.return_value = mock_result

    context = memory_manager.retrieve_context("completely unrelated topic")

    assert context == ""


def test_get_cached_indicator_fresh(memory_manager):
    """get_cached_indicator returns data when within TTL."""
    mock_point = MagicMock()
    mock_point.payload = {
        "indicator": "interest_rate",
        "value": "5.50%",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "ttl_hours": 24,
    }

    mock_result = MagicMock()
    mock_result.points = [mock_point]
    memory_manager.qdrant.query_points.return_value = mock_result

    result = memory_manager.get_cached_indicator("interest_rate")

    assert result is not None
    assert result["value"] == "5.50%"


def test_get_cached_indicator_expired(memory_manager):
    """get_cached_indicator returns None when TTL exceeded."""
    mock_point = MagicMock()
    mock_point.payload = {
        "indicator": "interest_rate",
        "value": "5.50%",
        "fetched_at": (datetime.now(timezone.utc) - timedelta(hours=48)).isoformat(),
        "ttl_hours": 24,
    }

    mock_result = MagicMock()
    mock_result.points = [mock_point]
    memory_manager.qdrant.query_points.return_value = mock_result

    result = memory_manager.get_cached_indicator("interest_rate")

    assert result is None


def test_get_cached_indicator_not_found(memory_manager):
    """get_cached_indicator returns None when no cached data."""
    mock_result = MagicMock()
    mock_result.points = []
    memory_manager.qdrant.query_points.return_value = mock_result

    result = memory_manager.get_cached_indicator("nonexistent")

    assert result is None


def test_memory_unavailable_degrades_silently():
    """When Qdrant is down, all operations return safely."""
    with (
        patch("src.agent.memory.QdrantClient", side_effect=Exception("Connection refused")),
        patch("src.agent.memory.OpenAI", return_value=_make_mock_openai()),
    ):
        from src.agent.memory import MemoryManager
        mm = MemoryManager()

        assert mm.available is False
        assert mm.retrieve_context("test") == ""
        assert mm.get_cached_indicator("test") is None

        # Should not raise
        mm.store_analysis("q", "r", "s", [], "neutral", [], 0)
        mm.cache_indicator("test", {"value": 1})

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agent.prompts import TRADING_ANALYST_PROMPT


def test_system_prompt_contains_tools():
    """System prompt mentions all 5 tools."""
    assert "get_crypto_data" in TRADING_ANALYST_PROMPT
    assert "get_market_data" in TRADING_ANALYST_PROMPT
    assert "get_macro_indicators" in TRADING_ANALYST_PROMPT
    assert "web_search" in TRADING_ANALYST_PROMPT
    assert "technical_analysis" in TRADING_ANALYST_PROMPT


def test_system_prompt_contains_disclaimer():
    """System prompt requires disclaimer."""
    assert "disclaimer" in TRADING_ANALYST_PROMPT.lower()


def test_system_prompt_contains_reasoning():
    """System prompt requires step-by-step reasoning."""
    assert "step by step" in TRADING_ANALYST_PROMPT.lower()


@pytest.mark.asyncio
async def test_run_agent_stream_events():
    """run_agent_stream yields correct event types."""
    from src.agent.graph import run_agent_stream

    mock_agent = AsyncMock()

    # Simulate astream_events yielding tool_start, tool_end, then text
    events = [
        {"event": "on_tool_start", "name": "get_crypto_data", "data": {"input": {"symbol": "bitcoin", "action": "price"}}},
        {"event": "on_tool_end", "name": "get_crypto_data", "data": {"output": '{"price_usd": 67420}'}},
        {"event": "on_chat_model_stream", "data": {"chunk": MagicMock(content="Bitcoin is at $67,420.")}},
    ]

    async def mock_stream(*args, **kwargs):
        for e in events:
            yield e

    mock_agent.astream_events = mock_stream

    collected = []
    async for event in run_agent_stream(mock_agent, "What is the Bitcoin price?"):
        collected.append(event)

    types = [e["type"] for e in collected]
    assert "tool_call" in types
    assert "tool_result" in types
    assert "text" in types
    assert "done" in types


@pytest.mark.asyncio
async def test_run_agent_stream_with_memory():
    """run_agent_stream integrates memory context."""
    from src.agent.graph import run_agent_stream

    mock_agent = AsyncMock()
    mock_memory = MagicMock()
    mock_memory.retrieve_context.return_value = "Previous: BTC was $65,000 yesterday"

    async def mock_stream(input_messages, **kwargs):
        # Verify context was prepended
        msg = input_messages["messages"][0][1]
        assert "Previous: BTC was $65,000 yesterday" in msg
        yield {"event": "on_chat_model_stream", "data": {"chunk": MagicMock(content="Analysis with context.")}}

    mock_agent.astream_events = mock_stream

    collected = []
    async for event in run_agent_stream(mock_agent, "BTC update", memory=mock_memory):
        collected.append(event)

    mock_memory.retrieve_context.assert_called_once_with("BTC update")


@pytest.mark.asyncio
async def test_run_agent_stream_memory_failure_nonfatal():
    """Memory failure should not crash the agent."""
    from src.agent.graph import run_agent_stream

    mock_agent = AsyncMock()
    mock_memory = MagicMock()
    mock_memory.retrieve_context.side_effect = Exception("Qdrant down")

    async def mock_stream(input_messages, **kwargs):
        yield {"event": "on_chat_model_stream", "data": {"chunk": MagicMock(content="Response without context.")}}

    mock_agent.astream_events = mock_stream

    collected = []
    async for event in run_agent_stream(mock_agent, "test", memory=mock_memory):
        collected.append(event)

    # Should still get a response
    assert any(e["type"] == "text" for e in collected)

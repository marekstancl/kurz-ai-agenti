from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from src.agent.prompts import TRADING_ANALYST_PROMPT
from src.config import Config


async def create_agent():
    """Create the LangGraph ReAct agent with MCP tools.

    Returns the agent instance. The MCP client is stored on the agent
    as ``_mcp_client`` so callers can manage its lifetime if needed.
    """
    mcp_config = {
        "trading-tools": {
            "command": "python",
            "args": [Config.MCP_SERVER_PATH],
            "transport": "stdio",
        }
    }

    client = MultiServerMCPClient(mcp_config)
    tools = await client.get_tools()

    llm = ChatOpenAI(
        model=Config.LLM_MODEL,
        api_key=Config.OPENAI_API_KEY,
        temperature=0.1,
        streaming=True,
    )

    agent = create_react_agent(
        llm,
        tools=tools,
        prompt=TRADING_ANALYST_PROMPT,
    )

    agent._mcp_client = client
    return agent


async def run_agent_stream(agent, user_message: str, memory=None):
    """Run the agent and yield streaming events.

    Args:
        agent: The LangGraph agent instance
        user_message: User's input message
        memory: Optional MemoryManager instance for context retrieval

    Yields:
        dict with keys:
            - type: "tool_call" | "tool_result" | "text" | "done"
            - content: str
            - tool_name: str (only for tool_call/tool_result)
    """
    context = ""
    if memory:
        try:
            context = memory.retrieve_context(user_message)
        except Exception:
            context = ""

    full_message = user_message
    if context:
        full_message = f"[Context from previous analyses: {context}]\n\nUser question: {user_message}"

    input_messages = {"messages": [("user", full_message)]}
    full_response_parts = []
    tools_used = []

    async for event in agent.astream_events(input_messages, version="v2"):
        kind = event["event"]

        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                full_response_parts.append(content)
                yield {"type": "text", "content": content}

        elif kind == "on_tool_start":
            tools_used.append(event["name"])
            raw_input = event["data"].get("input", {})
            if isinstance(raw_input, dict):
                raw_input = {k: v for k, v in raw_input.items() if k != "runtime"}
            yield {
                "type": "tool_call",
                "tool_name": event["name"],
                "content": str(raw_input),
            }

        elif kind == "on_tool_end":
            output = event["data"].get("output", "")
            if hasattr(output, "content"):
                output = output.content
            yield {
                "type": "tool_result",
                "tool_name": event["name"],
                "content": str(output)[:500],
            }

    yield {"type": "done", "content": ""}

    # Store analysis in memory if available
    full_response = "".join(full_response_parts)
    if memory and full_response:
        try:
            memory.store_analysis(
                query=user_message,
                response=full_response,
                summary=full_response[:200],
                assets=[],
                sentiment="neutral",
                tools_used=tools_used,
                reasoning_steps=len(tools_used),
            )
        except Exception:
            pass  # Memory storage is non-blocking

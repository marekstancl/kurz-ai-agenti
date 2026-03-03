VERSION = "0.1.0"

import asyncio
import json

import streamlit as st

from src.agent.graph import create_agent, run_agent_stream
from src.agent.memory import MemoryManager
from src.ui.charts import render_indicators_chart, render_price_chart

st.set_page_config(page_title="Trading Agent", page_icon="📈", layout="wide")

st.title("📈 Trading Analysis Agent")
st.caption("Powered by LangGraph + MCP Tools | Crypto & Global Markets")

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")

    st.divider()
    st.subheader("Quick Actions")
    quick_actions = {
        "🌍 Market Overview": "Give me a quick overview of the crypto market and major global indices today.",
        "📊 Macro Dashboard": "Show me the current macroeconomic dashboard — interest rates, inflation, unemployment, GDP, treasury yields, VIX.",
        "₿ BTC Analysis": "Provide a comprehensive analysis of Bitcoin — current price, technical indicators (RSI, MACD, Bollinger Bands), macro context, and recent news.",
        "📰 Market News": "What are the most important financial news stories today that could affect crypto and global markets?",
    }
    for label, prompt in quick_actions.items():
        if st.button(label, use_container_width=True):
            st.session_state["quick_action"] = prompt

    st.divider()
    st.caption(f"v{VERSION}")


# --- Event loop helper ---
def get_or_create_event_loop():
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            raise RuntimeError
        return loop
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop


# --- Initialize agent and memory ---
@st.cache_resource
def init_memory():
    return MemoryManager()


async def ensure_agent():
    if "agent" not in st.session_state:
        agent = await create_agent()
        st.session_state["agent"] = agent
        st.session_state["agent_ready"] = True


loop = get_or_create_event_loop()
memory = init_memory()
loop.run_until_complete(ensure_agent())

# --- Chat history ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            for tc in msg.get("tool_calls", []):
                with st.expander(f"🔧 {tc['tool_name']}", expanded=False):
                    st.code(tc.get("input", ""), language="json")
                    if tc.get("result"):
                        st.text(tc["result"])
            st.markdown(msg["content"])
            for chart_data in msg.get("charts", []):
                fig = render_price_chart(chart_data)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
            for metric_group in msg.get("metrics", []):
                if isinstance(metric_group, list):
                    cols = st.columns(min(len(metric_group), 4))
                    for col, m in zip(cols, metric_group):
                        with col:
                            st.metric(m["label"], m["value"])
                            st.caption(m.get("interpretation", ""))
        else:
            st.markdown(msg["content"])


# --- Process user input ---
def process_input(user_input: str):
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        tool_calls = []
        charts = []
        metrics = []

        async def stream_response():
            nonlocal full_response, tool_calls, charts, metrics
            agent = st.session_state["agent"]

            async for event in run_agent_stream(agent, user_input, memory=memory):
                if event["type"] == "tool_call":
                    tool_calls.append(
                        {"tool_name": event["tool_name"], "input": event["content"], "result": None}
                    )
                    with st.expander(f"🔧 {event['tool_name']}", expanded=True):
                        st.code(event["content"], language="json")

                elif event["type"] == "tool_result":
                    if tool_calls:
                        tool_calls[-1]["result"] = event["content"]
                    try:
                        result_data = json.loads(event["content"])
                        if "prices" in result_data or "data" in result_data:
                            charts.append(result_data)
                            fig = render_price_chart(result_data)
                            if fig:
                                st.plotly_chart(fig, use_container_width=True)
                        if "indicators" in result_data:
                            indicator_metrics = render_indicators_chart(result_data)
                            if indicator_metrics:
                                metrics.append(indicator_metrics)
                                cols = st.columns(min(len(indicator_metrics), 4))
                                for col, m in zip(cols, indicator_metrics):
                                    with col:
                                        st.metric(m["label"], m["value"])
                                        st.caption(m.get("interpretation", ""))
                    except (json.JSONDecodeError, TypeError):
                        pass

                elif event["type"] == "text":
                    full_response += event["content"]
                    response_placeholder.markdown(full_response + "▌")

                elif event["type"] == "done":
                    response_placeholder.markdown(full_response)

        loop.run_until_complete(stream_response())

    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": full_response,
            "tool_calls": tool_calls,
            "charts": charts,
            "metrics": metrics,
        }
    )


# Handle quick action
if "quick_action" in st.session_state:
    prompt = st.session_state.pop("quick_action")
    process_input(prompt)
    st.rerun()

# Chat input
user_input = st.chat_input("Ask about crypto, markets, or macro indicators...")
if user_input:
    process_input(user_input)
    st.rerun()

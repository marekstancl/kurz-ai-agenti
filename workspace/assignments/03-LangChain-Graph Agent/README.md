# Trading Analysis Agent

LangGraph ReAct trading analysis agent with MCP-based tools for crypto and global market analysis.

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Docker Compose                         │
│                                                          │
│  ┌─────────────────┐         ┌──────────────────────┐   │
│  │  Streamlit App   │         │     Qdrant 1.13+     │   │
│  │  (Port 8501)     │────────▶│   (Port 6333/6334)   │   │
│  │                  │         │   Collection:         │   │
│  │  ┌────────────┐  │         │   - analyses          │   │
│  │  │ LangGraph  │  │         │   - market_context    │   │
│  │  │ ReAct Agent│  │         └──────────────────────┘   │
│  │  │            │  │                                    │
│  │  │  ┌──────┐  │  │                                    │
│  │  │  │ MCP  │  │  │   External APIs (free tier):       │
│  │  │  │Client│──┼──┼──▶ CoinGecko API (no key)         │
│  │  │  └──┬───┘  │  │   Yahoo Finance (yfinance)        │
│  │  │     │      │  │   Tavily Search (free key)        │
│  │  └─────┼──────┘  │                                    │
│  │        │ stdio   │                                    │
│  │  ┌─────▼──────┐  │                                    │
│  │  │ MCP Server │  │                                    │
│  │  │ (subprocess)│  │                                    │
│  │  │ 5 tools    │  │                                    │
│  │  └────────────┘  │                                    │
│  └─────────────────┘                                    │
└──────────────────────────────────────────────────────────┘
```

## Features

- **ReAct Agent Pattern** — LangGraph `create_react_agent` with cyclic reasoning loop
- **5 MCP Tools:**
  - `get_crypto_data` — Real-time crypto prices from CoinGecko
  - `get_market_data` — Global stocks, indices, forex from Yahoo Finance
  - `get_macro_indicators` — Macro data via yfinance + Tavily search
  - `web_search` — Financial news via Tavily Search API
  - `technical_analysis` — RSI, SMA, MACD, Bollinger Bands, volatility
- **Persistent Memory** — Qdrant vector DB stores past analyses for contextual follow-ups
- **Streaming UI** — Streamlit chat with real-time response streaming and tool call visualization
- **Interactive Charts** — Plotly price history and technical indicator displays

## Prerequisites

- Docker and Docker Compose
- OpenAI API key ([platform.openai.com](https://platform.openai.com))
- Tavily API key (free at [tavily.com](https://tavily.com))

## Quick Start

1. **Clone and configure:**
   ```bash
   git clone <repository-url>
   cd assignment2
   cp .env.example .env
   # Edit .env with your API keys
   ```

2. **Start the application:**
   ```bash
   docker compose up --build
   ```

3. **Open the UI:**
   - Streamlit: http://localhost:8501
   - Qdrant: http://localhost:6333/dashboard

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | — | OpenAI API key for LLM + embeddings |
| `TAVILY_API_KEY` | Yes | — | Tavily API key for web search |
| `LLM_MODEL` | No | `gpt-4o-mini` | LLM model to use |
| `QDRANT_URL` | No | `http://qdrant:6333` | Qdrant connection URL |
| `MAX_AGENT_ITERATIONS` | No | `10` | Max ReAct loop iterations |

## Demo Scenarios

### 1. Market Overview
> "Give me a quick overview of the crypto market and major global indices today."

The agent calls `get_crypto_data` (market overview) and `get_market_data` (S&P 500, Nasdaq) to provide a combined snapshot.

### 2. Comprehensive BTC Analysis
> "Provide a comprehensive analysis of Bitcoin — current price, technical indicators, macro context, and recent news."

The agent uses 3+ tools: `get_crypto_data`, `technical_analysis`, `get_macro_indicators`, and `web_search`.

### 3. Macro Dashboard
> "Show me the current macroeconomic dashboard."

The agent calls `get_macro_indicators` with dashboard action to display treasury yields, VIX, inflation, unemployment, etc.

### 4. Impact Analysis
> "How might the Federal Reserve rate decision affect crypto markets?"

The agent combines `get_macro_indicators` (interest rates), `web_search` (Fed news), and `get_crypto_data` (current BTC state).

## Development

### Run tests
```bash
pip install -e ".[dev]"
pytest tests/ -v
```

### Project structure
```
src/
├── agent/
│   ├── graph.py      # LangGraph ReAct agent + streaming
│   ├── memory.py     # Qdrant memory manager
│   └── prompts.py    # System prompt
├── tools/
│   ├── server.py     # FastMCP server entry point
│   ├── crypto.py     # CoinGecko crypto data
│   ├── markets.py    # Yahoo Finance market data
│   ├── macro.py      # Macro indicators (yfinance + Tavily)
│   ├── search.py     # Tavily web search
│   └── analysis.py   # Technical analysis (RSI, MACD, etc.)
├── ui/
│   ├── app.py        # Streamlit chat interface
│   └── charts.py     # Plotly chart rendering
└── config.py         # Environment configuration

tests/
├── test_crypto.py    # CoinGecko tool tests
├── test_markets.py   # Yahoo Finance tool tests
├── test_macro.py     # Macro indicator tests
├── test_search.py    # Tavily search tests
├── test_analysis.py  # Technical analysis tests
├── test_memory.py    # Qdrant memory tests
├── test_agent.py     # Agent + streaming tests
└── test_integration.py # End-to-end pipeline tests
```

## Technology Stack

- **Agent:** LangGraph 0.3+ with `create_react_agent`
- **Tools:** MCP (Model Context Protocol) via `langchain-mcp-adapters`
- **LLM:** OpenAI GPT-4o-mini (configurable)
- **Embeddings:** OpenAI `text-embedding-3-small`
- **Vector DB:** Qdrant
- **UI:** Streamlit
- **Charts:** Plotly
- **Data:** CoinGecko, Yahoo Finance, Tavily Search

## Disclaimer

This is an educational project for a school assignment. All analysis is for informational purposes only and does not constitute financial advice.

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY: str = os.environ["OPENAI_API_KEY"]
    TAVILY_API_KEY: str = os.environ["TAVILY_API_KEY"]
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    QDRANT_COLLECTION_ANALYSES: str = "analyses"
    QDRANT_COLLECTION_MARKET: str = "market_context"
    MCP_SERVER_PATH: str = os.path.join(os.path.dirname(__file__), "tools", "server.py")
    MAX_AGENT_ITERATIONS: int = int(os.getenv("MAX_AGENT_ITERATIONS", "10"))

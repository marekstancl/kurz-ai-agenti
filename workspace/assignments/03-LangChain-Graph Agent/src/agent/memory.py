import uuid
from datetime import datetime, timezone

from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from src.config import Config


class MemoryManager:
    def __init__(self):
        self.available = True
        try:
            self.qdrant = QdrantClient(url=Config.QDRANT_URL)
            self.openai = OpenAI(api_key=Config.OPENAI_API_KEY)
            self._ensure_collections()
        except Exception:
            self.available = False

    def _ensure_collections(self):
        """Create Qdrant collections if they don't exist."""
        collections = [c.name for c in self.qdrant.get_collections().collections]

        if Config.QDRANT_COLLECTION_ANALYSES not in collections:
            self.qdrant.create_collection(
                collection_name=Config.QDRANT_COLLECTION_ANALYSES,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
            )

        if Config.QDRANT_COLLECTION_MARKET not in collections:
            self.qdrant.create_collection(
                collection_name=Config.QDRANT_COLLECTION_MARKET,
                vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
            )

    def _embed(self, text: str) -> list[float]:
        """Generate embedding using OpenAI text-embedding-3-small."""
        response = self.openai.embeddings.create(model=Config.EMBEDDING_MODEL, input=text)
        return response.data[0].embedding

    def retrieve_context(self, query: str, limit: int = 3) -> str:
        """Retrieve relevant past analyses for the given query.

        Returns a formatted string of past analyses to prepend to agent input.
        Returns empty string if no relevant results found or memory unavailable.
        """
        if not self.available:
            return ""

        try:
            embedding = self._embed(query)
            results = self.qdrant.query_points(
                collection_name=Config.QDRANT_COLLECTION_ANALYSES,
                query=embedding,
                limit=limit,
                score_threshold=0.5,
            )

            if not results.points:
                return ""

            context_parts = []
            for point in results.points:
                p = point.payload
                age = _time_ago(p.get("timestamp", ""))
                context_parts.append(
                    f"- [{age}] Q: {p['query']} -> {p['summary']} "
                    f"(sentiment: {p.get('sentiment', 'unknown')}, assets: {', '.join(p.get('assets', []))})"
                )

            return "Previous relevant analyses:\n" + "\n".join(context_parts)
        except Exception:
            return ""

    def store_analysis(
        self,
        query: str,
        response: str,
        summary: str,
        assets: list[str],
        sentiment: str,
        tools_used: list[str],
        reasoning_steps: int,
    ):
        """Store a completed analysis in Qdrant for future retrieval."""
        if not self.available:
            return

        try:
            embed_text = f"{query} {summary}"
            embedding = self._embed(embed_text)

            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "query": query,
                    "response": response[:2000],
                    "summary": summary,
                    "assets": assets,
                    "sentiment": sentiment,
                    "tools_used": tools_used,
                    "reasoning_steps": reasoning_steps,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
            )

            self.qdrant.upsert(
                collection_name=Config.QDRANT_COLLECTION_ANALYSES,
                points=[point],
            )
        except Exception:
            pass  # Non-blocking

    def get_cached_indicator(self, indicator: str) -> dict | None:
        """Check if a macro indicator is cached and still fresh."""
        if not self.available:
            return None

        try:
            embedding = self._embed(indicator)
            results = self.qdrant.query_points(
                collection_name=Config.QDRANT_COLLECTION_MARKET,
                query=embedding,
                limit=1,
                score_threshold=0.8,
            )

            if not results.points:
                return None

            point = results.points[0]
            fetched_at = datetime.fromisoformat(point.payload.get("fetched_at", "2000-01-01"))
            ttl_hours = point.payload.get("ttl_hours", 24)
            age_hours = (datetime.now(timezone.utc) - fetched_at).total_seconds() / 3600

            if age_hours > ttl_hours:
                return None

            return point.payload
        except Exception:
            return None

    def cache_indicator(self, indicator: str, data: dict):
        """Cache a macro indicator in Qdrant."""
        if not self.available:
            return

        try:
            embedding = self._embed(f"{indicator} {data.get('region', 'US')}")
            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    **data,
                    "indicator": indicator,
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                    "ttl_hours": data.get("ttl_hours", 24),
                },
            )
            self.qdrant.upsert(
                collection_name=Config.QDRANT_COLLECTION_MARKET,
                points=[point],
            )
        except Exception:
            pass  # Non-blocking


def _time_ago(timestamp_str: str) -> str:
    """Convert ISO timestamp to human-readable relative time."""
    if not timestamp_str:
        return "unknown time"
    try:
        ts = datetime.fromisoformat(timestamp_str)
        delta = datetime.now(timezone.utc) - ts
        if delta.days > 0:
            return f"{delta.days}d ago"
        hours = delta.seconds // 3600
        if hours > 0:
            return f"{hours}h ago"
        return "just now"
    except (ValueError, TypeError):
        return "unknown time"

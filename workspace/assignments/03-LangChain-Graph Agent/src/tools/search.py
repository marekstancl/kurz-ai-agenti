import json
import os

from tavily import TavilyClient


def register_search_tools(mcp):
    @mcp.tool()
    def web_search(query: str, search_type: str = "news") -> str:
        """Search the web for financial news and market information.

        Args:
            query: Search query (e.g., 'Bitcoin ETF inflows February 2026', 'Fed interest rate decision')
            search_type: 'news' for recent articles (default), 'general' for broader search
        """
        try:
            api_key = os.environ.get("TAVILY_API_KEY", "")
            if not api_key:
                return json.dumps({"error": "TAVILY_API_KEY not configured"})
            client = TavilyClient(api_key=api_key)
            topic = "news" if search_type in ("news", "general") else "general"
            if search_type not in ("news", "general"):
                topic = "general"
            results = client.search(query=query, search_depth="basic", max_results=5, topic=topic)
            formatted = [
                {"title": r["title"], "url": r["url"], "snippet": r["content"][:300]}
                for r in results.get("results", [])
            ]
            return json.dumps({"query": query, "results": formatted, "count": len(formatted)})
        except Exception as e:
            return json.dumps({"error": f"Web search failed: {str(e)}"})

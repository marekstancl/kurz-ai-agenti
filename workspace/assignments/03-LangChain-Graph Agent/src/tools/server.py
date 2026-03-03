import os
import sys

# Ensure project root is on sys.path when run as subprocess
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("trading-tools", instructions="Financial market data and analysis tools for trading research.")

from src.tools.crypto import register_crypto_tools
from src.tools.markets import register_market_tools
from src.tools.macro import register_macro_tools
from src.tools.search import register_search_tools
from src.tools.analysis import register_analysis_tools

register_crypto_tools(mcp)
register_market_tools(mcp)
register_macro_tools(mcp)
register_search_tools(mcp)
register_analysis_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")

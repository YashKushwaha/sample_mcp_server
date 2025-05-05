# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo",host="0.0.0.0", port=8000)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add an addition tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    transport = "sse"  # or set from ENV if needed
    print(f"Running server with {transport} transport")
    if transport in ["stdio", "sse", "http", "websocket"]:
        mcp.run(transport=transport)
    else:
        raise ValueError(f"Unknown transport: {transport}")

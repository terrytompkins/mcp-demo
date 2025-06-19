from mcp.server.fastmcp import FastMCP
import requests
import json

# Create an MCP server
mcp = FastMCP("MCP Proxy Server")

# FastAPI server URLs
SERVERS = {
    "api": "http://localhost:8001",
    "files": "http://localhost:8002",
}

def get_tools_from_server(server_url: str):
    """Get tools from a FastAPI server."""
    try:
        r = requests.post(f"{server_url}/list", json={})
        r.raise_for_status()
        return r.json()["tools"]
    except Exception as e:
        print(f"Error getting tools from {server_url}: {e}")
        return []

def call_tool_on_server(server_url: str, tool_name: str, args: dict):
    """Call a tool on a FastAPI server."""
    try:
        payload = {"tool_name": tool_name, "args": args}
        r = requests.post(f"{server_url}/call", json=payload)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}

# Register tools from all servers
for server_id, server_url in SERVERS.items():
    tools = get_tools_from_server(server_url)
    for tool in tools:
        tool_name = tool["name"]
        description = tool["description"]
        args_schema = tool.get("args_schema", {})
        
        # Create a closure to capture the server info
        def make_tool_function(server_url, tool_name):
            def tool_function(**kwargs):
                result = call_tool_on_server(server_url, tool_name, kwargs)
                if "result" in result:
                    return result["result"]
                elif "error" in result:
                    raise Exception(result["error"])
                else:
                    return str(result)
            return tool_function
        
        # Register the tool with MCP
        func = make_tool_function(server_url, tool_name)
        func.__name__ = f"{server_id}_{tool_name}"
        func.__doc__ = description
        
        # Register with MCP
        mcp.tool()(func)

# Run the server
if __name__ == "__main__":
    mcp.run() 
import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from mcp.types import Tool

class MCPClient:
    def __init__(self, server_id: str, server_path: str):
        self.server_id = server_id
        self.server_path = server_path
        self.session = None

    async def connect(self):
        """Connect to the MCP server."""
        if self.session is None:
            transport = await stdio_client(self.server_path)
            self.session = ClientSession(transport)
            await self.session.initialize()

    async def list_tools(self):
        """List available tools from the server."""
        await self.connect()
        tools = await self.session.list_tools()
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "args_schema": {param.name: "string" for param in tool.inputSchema.properties.values()}
            }
            for tool in tools.tools
        ]

    async def call_tool(self, tool_name: str, **kwargs):
        """Call a tool on the server."""
        await self.connect()
        result = await self.session.call_tool(tool_name, kwargs)
        return {"result": result.content[0].text}

    def list_tools_sync(self):
        """Synchronous wrapper for list_tools."""
        return asyncio.run(self.list_tools())

    def call_tool_sync(self, tool_name: str, **kwargs):
        """Synchronous wrapper for call_tool."""
        return asyncio.run(self.call_tool(tool_name, **kwargs)) 
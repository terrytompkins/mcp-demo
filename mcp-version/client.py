import requests

class MCPClient:
    def __init__(self, server_id: str, base_url: str):
        self.server_id = server_id
        self.base_url = base_url.rstrip("/")

    def list_tools(self):
        r = requests.post(f"{self.base_url}/list", json={})
        r.raise_for_status()
        return r.json()["tools"]

    def call_tool(self, tool_name: str, **kwargs):
        payload = {"tool_name": tool_name, "args": kwargs}
        r = requests.post(f"{self.base_url}/call", json=payload)
        r.raise_for_status()
        return r.json()

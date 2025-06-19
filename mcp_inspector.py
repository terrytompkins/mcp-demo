import streamlit as st
import requests
import json

st.title("MCP Inspector")

# FastAPI server URLs
SERVERS = {
    "api": "http://localhost:8001",
    "files": "http://localhost:8002",
}

# Get tools from all servers
all_tools = {}
for server_id, server_url in SERVERS.items():
    try:
        r = requests.post(f"{server_url}/list", json={})
        r.raise_for_status()
        tools = r.json()["tools"]
        all_tools[server_id] = tools
    except Exception as e:
        st.error(f"Failed to connect to {server_id} server: {e}")
        all_tools[server_id] = []

# Display server status
st.header("Server Status")
for server_id, server_url in SERVERS.items():
    try:
        r = requests.post(f"{server_url}/list", json={})
        if r.status_code == 200:
            st.success(f"✅ {server_id} server ({server_url}) - Connected")
        else:
            st.error(f"❌ {server_id} server ({server_url}) - Error {r.status_code}")
    except Exception as e:
        st.error(f"❌ {server_id} server ({server_url}) - Connection failed: {e}")

# Display available tools
st.header("Available Tools")
for server_id, tools in all_tools.items():
    if tools:
        st.subheader(f"{server_id} Server")
        for tool in tools:
            with st.expander(f"🔧 {tool['name']} - {tool['description']}"):
                st.write(f"**Description:** {tool['description']}")
                if tool.get("args_schema"):
                    st.write("**Parameters:**")
                    for param_name, param_type in tool["args_schema"].items():
                        st.write(f"  - `{param_name}`: {param_type}")
                
                # Test the tool
                st.write("**Test Tool:**")
                if tool.get("args_schema"):
                    # Build form for parameters
                    test_args = {}
                    for param_name, param_type in tool["args_schema"].items():
                        if param_type == "string":
                            test_args[param_name] = st.text_input(f"Enter {param_name}:", key=f"{server_id}_{tool['name']}_{param_name}")
                    
                    if st.button(f"Test {tool['name']}", key=f"test_{server_id}_{tool['name']}"):
                        try:
                            payload = {"tool_name": tool["name"], "args": test_args}
                            r = requests.post(f"{SERVERS[server_id]}/call", json=payload)
                            r.raise_for_status()
                            result = r.json()
                            st.json(result)
                        except Exception as e:
                            st.error(f"Error calling tool: {e}")
                else:
                    # No parameters needed
                    if st.button(f"Test {tool['name']}", key=f"test_{server_id}_{tool['name']}"):
                        try:
                            payload = {"tool_name": tool["name"], "args": {}}
                            r = requests.post(f"{SERVERS[server_id]}/call", json=payload)
                            r.raise_for_status()
                            result = r.json()
                            st.json(result)
                        except Exception as e:
                            st.error(f"Error calling tool: {e}")

# Server logs
st.header("Server Logs")
if st.button("Refresh Logs"):
    st.info("Logs would be displayed here if the servers provided logging endpoints")

# Connection info
st.header("Connection Information")
st.code(f"""
MCP Inspector URL: http://localhost:8501
API Server: http://localhost:8001
Files Server: http://localhost:8002

To use with MCP clients, configure them to connect to:
- API Server: http://localhost:8001
- Files Server: http://localhost:8002
""") 
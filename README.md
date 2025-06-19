# Python MCP Demo

A demonstration of Model Context Protocol (MCP) using FastAPI servers and Streamlit interfaces.

## Features

- **FastAPI MCP Servers**: API and file operations servers
- **Streamlit Host**: AI-powered interface for interacting with MCP tools
- **MCP Inspector**: Web-based tool for inspecting and testing MCP capabilities
- **File Operations**: List, read, and write files in a sandbox directory
- **Random Facts API**: Get random interesting facts

## Setup

1. **Create virtual environment and install dependencies:**
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2. **Set your OpenAI API key:**
```bash
export OPENAI_API_KEY="sk-..."
```

## Running the Application

### Option 1: Start Everything Manually

1. **Start the API server:**
```bash
uvicorn server_api:app --port 8001 --reload
```

2. **Start the files server:**
```bash
uvicorn server_files:app --port 8002 --reload
```

3. **Start the Streamlit host:**
```bash
streamlit run host_streamlit.py
```

4. **Start the MCP Inspector (optional):**
```bash
streamlit run mcp_inspector.py --server.port 8503
```

### Option 2: Quick Start Script

Create a start script to launch everything at once:

```bash
#!/bin/bash
# start_all.sh

# Start API server
uvicorn server_api:app --port 8001 --reload &
API_PID=$!

# Start files server  
uvicorn server_files:app --port 8002 --reload &
FILES_PID=$!

# Wait for servers to start
sleep 3

# Start Streamlit host
streamlit run host_streamlit.py &
HOST_PID=$!

# Start MCP Inspector
streamlit run mcp_inspector.py --server.port 8503 &
INSPECTOR_PID=$!

echo "All services started!"
echo "Streamlit Host: http://localhost:8502"
echo "MCP Inspector: http://localhost:8503"
echo "API Server: http://localhost:8001"
echo "Files Server: http://localhost:8002"

# Wait for user to stop
read -p "Press Enter to stop all services..."

# Cleanup
kill $API_PID $FILES_PID $HOST_PID $INSPECTOR_PID
echo "All services stopped."
```

Make it executable and run:
```bash
chmod +x start_all.sh
./start_all.sh
```

## Accessing the Applications

Once everything is running, you can access:

- **Streamlit Host**: http://localhost:8502
  - AI-powered interface for interacting with MCP tools
  - Ask questions like "Read the README.md file" or "Get a random fact"

- **MCP Inspector**: http://localhost:8503
  - Web-based tool for inspecting server status
  - Test individual MCP tools directly
  - View server connections and tool documentation

- **API Server**: http://localhost:8001
  - FastAPI server with random facts tool
  - API docs available at http://localhost:8001/docs

- **Files Server**: http://localhost:8002
  - FastAPI server with file operations
  - API docs available at http://localhost:8002/docs

## Available Tools

### API Server (port 8001)
- `get_random_fact`: Returns a random interesting fact

### Files Server (port 8002)
- `list_files`: Lists files in the sandbox directory
- `read_file`: Reads the contents of a specific file
- `write_file`: Writes content to a file

## Usage Examples

### In the Streamlit Host:
- "List the files in the files directory"
- "Read the README.md file"
- "Show me the contents of requirements.txt"
- "Get a random fact"
- "Write a file called test.txt with content 'Hello World'"

### In the MCP Inspector:
- View server status and connections
- Test tools directly with parameters
- See tool documentation and schemas

## Troubleshooting

1. **Servers not connecting**: Make sure both uvicorn servers are running on ports 8001 and 8002
2. **OpenAI API errors**: Verify your API key is set correctly
3. **Port conflicts**: If ports are in use, modify the port numbers in the commands
4. **File operations**: Files are stored in the `files/` directory relative to the project root

## Project Structure

```
mcp-demo/
├── server_api.py          # API server with random facts
├── server_files.py        # Files server with file operations
├── host_streamlit.py      # Main Streamlit interface
├── mcp_inspector.py       # MCP Inspector interface
├── client.py              # MCP client for FastAPI servers
├── files/                 # Sandbox directory for file operations
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

#!/bin/bash

echo "Stopping all MCP demo processes..."

# Kill uvicorn servers
echo "Stopping uvicorn servers..."
pkill -f "uvicorn server_api" 2>/dev/null
pkill -f "uvicorn server_files" 2>/dev/null

# Kill streamlit apps
echo "Stopping streamlit apps..."
pkill -f "streamlit run" 2>/dev/null

# Kill by ports as backup
echo "Killing processes on ports 8001, 8002, 8502, 8503..."
lsof -ti:8001 2>/dev/null | xargs kill -9 2>/dev/null
lsof -ti:8002 2>/dev/null | xargs kill -9 2>/dev/null
lsof -ti:8502 2>/dev/null | xargs kill -9 2>/dev/null
lsof -ti:8503 2>/dev/null | xargs kill -9 2>/dev/null

# Check if any processes are still running
echo "Checking for remaining processes..."
REMAINING=$(ps aux | grep -E "(uvicorn|streamlit)" | grep -v grep | grep -v stop_all.sh)

if [ -z "$REMAINING" ]; then
    echo "✅ All MCP demo processes stopped successfully!"
else
    echo "⚠️  Some processes may still be running:"
    echo "$REMAINING"
    echo "You may need to manually kill them with: kill -9 <PID>"
fi 
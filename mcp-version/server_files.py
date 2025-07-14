from fastapi import FastAPI
import sys
import pathlib

# Add the shared directory to the path
shared_path = pathlib.Path(__file__).parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from file_operations import FileOperations

app = FastAPI(title="File Ops MCP Server")

# Initialize file operations with the shared files directory
file_ops = FileOperations()

@app.post("/list")
def list_tools():
    return {
        "tools": [
            {"name": "list_files", "description": "List files in sandbox dir.", "args_schema": {}},
            {"name": "read_file", "description": "Read a file.", "args_schema": {"filename": "string"}},
            {"name": "write_file", "description": "Write a file.", "args_schema": {"filename": "string", "content": "string"}},
        ]
    }

@app.post("/call")
def call_tool(payload: dict):
    tool = payload.get("tool_name")
    args = payload.get("args", {})
    
    if tool == "list_files":
        return {"result": file_ops.list_files()}
    elif tool == "read_file":
        result = file_ops.read_file(args.get("filename", ""))
        return result
    elif tool == "write_file":
        result = file_ops.write_file(args.get("filename", ""), args.get("content", ""))
        return result
    return {"error": "unknown"}

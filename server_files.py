from fastapi import FastAPI
import os, pathlib

ROOT = pathlib.Path(__file__).parent / "files"
ROOT.mkdir(exist_ok=True)

app = FastAPI(title="File Ops MCP Server")

def _safe_path(name: str):
    return ROOT / pathlib.Path(name).name

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
        return {"result": os.listdir(ROOT)}
    elif tool == "read_file":
        p = _safe_path(args.get("filename", ""))
        if not p.exists():
            return {"error": "not found"}
        return {"result": p.read_text()}
    elif tool == "write_file":
        p = _safe_path(args.get("filename", ""))
        p.write_text(args.get("content", ""))
        return {"result": "ok"}
    return {"error": "unknown"}

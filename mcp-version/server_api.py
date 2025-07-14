from fastapi import FastAPI
import sys
import pathlib

# Add the shared directory to the path
shared_path = pathlib.Path(__file__).parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from random_facts import RandomFacts

app = FastAPI(title="Random Fact MCP Server")

# Initialize random facts
random_facts = RandomFacts()

@app.post("/list")
def list_tools():
    return {
        "tools": [{
            "name": "get_random_fact",
            "description": "Return a random fun fact.",
            "args_schema": {}
        }]
    }

@app.post("/call")
def call_tool(payload: dict):
    if payload.get("tool_name") == "get_random_fact":
        return {"result": random_facts.get_random_fact()}
    return {"error": "unknown tool"}

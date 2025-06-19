from fastapi import FastAPI
import random

app = FastAPI(title="Random Fact MCP Server")

FACTS = [
    "Cats have five toes on their front paws, but only four on their back paws.",
    "Bananas are berries, but strawberries are not.",
    "The unicorn is the national animal of Scotland."
]

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
        return {"result": random.choice(FACTS)}
    return {"error": "unknown tool"}

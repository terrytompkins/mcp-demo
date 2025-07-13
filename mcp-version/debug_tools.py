import os, json
from client import MCPClient

SERVERS = {
    "api": "http://localhost:8001",
    "files": "http://localhost:8002",
}

clients, registry = [], {}
for sid, url in SERVERS.items():
    c = MCPClient(sid, url)
    clients.append(c)
    for tool in c.list_tools():
        fq = f"{sid}.{tool['name']}"
        registry[fq] = (c, tool)

print("Registered tools:")
for fq, (_, meta) in registry.items():
    print(f"  {fq} — {meta['description']}")

def to_openai_fn(sid, meta):
    return {
        "name": f"{sid}_{meta['name']}",
        "description": meta["description"],
        "parameters": {"type":"object", "properties": {k: {"type":"string"} for k in meta.get("args_schema", {})}},
    }

fns = [to_openai_fn(sid, meta) for fq, (c, meta) in registry.items() for sid in [fq.split('.', 1)[0]]]

print("\nGenerated function names:")
for fn in fns:
    print(f"  {fn['name']} — {fn['description']}") 
import os, json, streamlit as st
import openai

from client import MCPClient

openai.api_key = os.getenv("OPENAI_API_KEY", "")

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

st.title("MCP Host Demo")

with st.expander("Tools"):
    for fq, (_, meta) in registry.items():
        st.write(f"**{fq}** — {meta['description']}")

q = st.text_input("Ask something:")
if not q:
    st.stop()
if not openai.api_key:
    st.error("Set OPENAI_API_KEY.")
    st.stop()

def to_openai_fn(sid, meta):
    return {
        "name": f"{sid}_{meta['name']}",
        "description": meta["description"],
        "parameters": {"type":"object", "properties": {k: {"type":"string"} for k in meta.get("args_schema", {})}},
    }

fns = [to_openai_fn(sid, meta) for fq, (c, meta) in registry.items() for sid in [fq.split('.', 1)[0]]]

system_prompt = """You are a helpful assistant with access to file operations. Use the appropriate tool based on the user's request:

- Use files_list_files when the user wants to see what files are available
- Use files_read_file when the user wants to read the contents of a specific file
- Use files_write_file when the user wants to create or modify a file
- Use api_get_random_fact when the user asks for a random fact

If the user asks to read a specific file, use files_read_file directly - do not list files first."""

msgs=[{"role":"system","content":system_prompt},
      {"role":"user","content":q}]
resp=openai.ChatCompletion.create(model="gpt-4o-mini",messages=msgs,functions=fns,function_call="auto")
msg=resp.choices[0].message

if msg.get("function_call"):
    name=msg["function_call"]["name"]
    args=json.loads(msg["function_call"]["arguments"] or "{}")
    sid, tool = name.split("_",1)
    fq=f"{sid}.{tool}"
    client,_=registry[fq]
    result=client.call_tool(tool,**args)
    st.json(result)
else:
    st.write(msg.content)

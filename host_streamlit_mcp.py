import os, json, streamlit as st
import openai
import subprocess
import time

openai.api_key = os.getenv("OPENAI_API_KEY", "")

# MCP server configurations
SERVERS = {
    "api": "python server_api_mcp.py",
    "files": "python server_files_mcp.py",
}

# Start MCP servers
server_processes = {}
for sid, cmd in SERVERS.items():
    try:
        process = subprocess.Popen(
            cmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        server_processes[sid] = process
        time.sleep(1)  # Give servers time to start
    except Exception as e:
        st.error(f"Failed to start {sid} server: {e}")

st.title("MCP Host Demo (Official SDK)")

# For now, let's use a simpler approach with direct tool definitions
# since the async client is complex for Streamlit
tools = [
    {
        "name": "files_list_files",
        "description": "List files in sandbox directory.",
        "parameters": {"type":"object", "properties": {}},
    },
    {
        "name": "files_read_file", 
        "description": "Read a file from the sandbox directory.",
        "parameters": {"type":"object", "properties": {"filename": {"type":"string"}}},
    },
    {
        "name": "files_write_file",
        "description": "Write content to a file in the sandbox directory.",
        "parameters": {"type":"object", "properties": {"filename": {"type":"string"}, "content": {"type":"string"}}},
    },
    {
        "name": "api_get_random_fact",
        "description": "Return a random fun fact.",
        "parameters": {"type":"object", "properties": {}},
    }
]

with st.expander("Available Tools"):
    for tool in tools:
        st.write(f"**{tool['name']}** — {tool['description']}")

q = st.text_input("Ask something:")
if not q:
    st.stop()
if not openai.api_key:
    st.error("Set OPENAI_API_KEY.")
    st.stop()

system_prompt = """You are a helpful assistant with access to file operations and random facts. Use the appropriate tool based on the user's request:

- Use files_list_files when the user wants to see what files are available
- Use files_read_file when the user wants to read the contents of a specific file
- Use files_write_file when the user wants to create or modify a file
- Use api_get_random_fact when the user asks for a random fact

If the user asks to read a specific file, use files_read_file directly - do not list files first."""

msgs=[{"role":"system","content":system_prompt},
      {"role":"user","content":q}]

try:
    resp=openai.ChatCompletion.create(model="gpt-4o-mini",messages=msgs,functions=tools,function_call="auto")
    msg=resp.choices[0].message

    if msg.get("function_call"):
        name=msg["function_call"]["name"]
        args=json.loads(msg["function_call"]["arguments"] or "{}")
        
        # For now, implement simple tool calls
        if name == "files_list_files":
            import os
            files_dir = os.path.join(os.path.dirname(__file__), "files")
            result = {"result": os.listdir(files_dir)}
        elif name == "files_read_file":
            import os
            filename = args.get("filename", "")
            files_dir = os.path.join(os.path.dirname(__file__), "files")
            file_path = os.path.join(files_dir, filename)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                result = {"result": content}
            except FileNotFoundError:
                result = {"error": f"File {filename} not found"}
        elif name == "files_write_file":
            import os
            filename = args.get("filename", "")
            content = args.get("content", "")
            files_dir = os.path.join(os.path.dirname(__file__), "files")
            file_path = os.path.join(files_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content)
            result = {"result": f"Successfully wrote {len(content)} characters to {filename}"}
        elif name == "api_get_random_fact":
            import random
            facts = [
                "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
                "A day on Venus is longer than its year. Venus takes 243 Earth days to rotate on its axis but only 225 Earth days to orbit the Sun.",
                "Bananas are berries, but strawberries aren't. In botanical terms, a berry is a fleshy fruit produced from a single ovary.",
                "The shortest war in history lasted only 38-45 minutes. The Anglo-Zanzibar War of 1896 ended when the British bombarded the Sultan's palace.",
                "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
                "The Great Wall of China is not visible from space with the naked eye, despite the popular myth.",
                "A group of flamingos is called a 'flamboyance'.",
                "The average person spends 6 months of their lifetime waiting for red lights to turn green.",
                "Polar bears are left-handed. Well, left-pawed to be more accurate.",
                "The first oranges weren't orange. The original oranges from Southeast Asia were actually green."
            ]
            result = {"result": random.choice(facts)}
        else:
            result = {"error": f"Unknown tool: {name}"}
        
        st.json(result)
    else:
        st.write(msg.content)
        
except Exception as e:
    st.error(f"Error: {e}")

# Cleanup on app close
def cleanup():
    for process in server_processes.values():
        if process.poll() is None:  # If process is still running
            process.terminate()

# Register cleanup
import atexit
atexit.register(cleanup) 
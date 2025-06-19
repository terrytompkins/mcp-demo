import openai
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY", "")

# Define the functions exactly as they appear in the Streamlit app
fns = [
    {
        "name": "files_list_files",
        "description": "List files in sandbox dir.",
        "parameters": {"type":"object", "properties": {}},
    },
    {
        "name": "files_read_file", 
        "description": "Read a file.",
        "parameters": {"type":"object", "properties": {"filename": {"type":"string"}}},
    }
]

system_prompt = """You are a helpful assistant with access to file operations. Use the appropriate tool based on the user's request:

- Use files_list_files when the user wants to see what files are available
- Use files_read_file when the user wants to read the contents of a specific file
- Use files_write_file when the user wants to create or modify a file
- Use api_get_random_fact when the user asks for a random fact

If the user asks to read a specific file, use files_read_file directly - do not list files first."""

# Test different prompts
test_prompts = [
    "Read the README.md file",
    "Show me the contents of README.md", 
    "Read file README.md",
    "What's in the README.md file?"
]

for prompt in test_prompts:
    print(f"\n=== Testing prompt: '{prompt}' ===")
    
    msgs = [
        {"role":"system","content":system_prompt},
        {"role":"user","content":prompt}
    ]
    
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=msgs,
            functions=fns,
            function_call="auto"
        )
        msg = resp.choices[0].message
        
        if msg.get("function_call"):
            print(f"Function called: {msg['function_call']['name']}")
            print(f"Arguments: {msg['function_call']['arguments']}")
        else:
            print(f"No function called. Response: {msg.content}")
            
    except Exception as e:
        print(f"Error: {e}") 
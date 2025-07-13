# MCP Version

This directory contains the Model Context Protocol (MCP) implementation of the file operations and random facts demo.

## Architecture

- **Multiple FastAPI servers**: Separate servers for different functionalities
- **Streamlit frontend**: Web interface with OpenAI integration
- **AI-powered**: Uses OpenAI GPT to understand natural language requests
- **Distributed**: Components communicate via HTTP APIs

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Running

1. Start the API server (random facts):
   ```bash
   uvicorn server_api:app --port 8001
   ```

2. Start the files server:
   ```bash
   uvicorn server_files:app --port 8002
   ```

3. Start the Streamlit frontend:
   ```bash
   streamlit run host_streamlit.py
   ```

## Usage

Open the Streamlit app in your browser and ask questions like:
- "Show me the available files"
- "Read the hydra-README.md file"
- "Tell me a random fact"
- "Create a new file called test.txt with content 'Hello World'"

The AI will understand your request and call the appropriate MCP tools. 
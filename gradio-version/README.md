# Gradio Version

This directory contains a simpler implementation of the file operations and random facts demo using Gradio.

## Architecture

- **Single application**: Everything runs in one process
- **Direct UI**: Native Gradio components for each operation
- **No AI required**: Direct function calls, no OpenAI integration needed
- **Simpler setup**: Only one command to run

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running

Simply run the Gradio app:
```bash
python app.py
```

The app will start and provide a URL (usually http://localhost:7860) where you can access the interface.

## Usage

The interface has two main tabs:

### Random Facts Tab
- Click "Get Random Fact" to see a random fun fact

### File Operations Tab
- **List Files**: Click to see all files in the shared files directory
- **Read File**: Enter a filename and click "Read File" to see its contents
- **Write File**: Enter a filename and content, then click "Write File" to create/modify a file

## Comparison with MCP Version

This Gradio version provides the same functionality as the MCP version but with:
- **Simpler architecture**: No separate servers needed
- **Direct interface**: No AI interpretation required
- **Easier setup**: Single command to run
- **Less dependencies**: Only Gradio needed 
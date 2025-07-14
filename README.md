# MCP Demo Project

This project demonstrates the same functionality implemented in two different ways:
1. **MCP Version**: Using Model Context Protocol with multiple servers and AI integration
2. **Gradio Version**: Using Gradio with a simpler, direct interface

## Project Structure

```
mcp-demo/
├── mcp-version/           # MCP implementation with FastAPI servers + Streamlit
├── gradio-version/        # Gradio implementation (simpler)
├── shared/                # Common functionality used by both versions
│   ├── file_operations.py
│   └── random_facts.py
├── files/                 # Shared files directory (operated on by both versions)
└── README.md
```

## Functionality

Both versions provide:
- **File Operations**: List, read, and write files in a sandbox directory
- **Random Facts**: Get random fun facts from a curated collection

## Quick Start

### For MCP Version (Complex)
```bash
cd mcp-version
pip install -r requirements.txt
export OPENAI_API_KEY="your-key"
# Start servers and Streamlit (see mcp-version/README.md)
```

### For Gradio Version (Simple)
```bash
cd gradio-version
pip install -r requirements.txt
python app.py
```

## Architecture Comparison

| Aspect | MCP Version | Gradio Version |
|--------|-------------|----------------|
| **Architecture** | Multiple FastAPI servers + Streamlit | Single Gradio app |
| **AI Integration** | OpenAI GPT for natural language | Direct UI components |
| **Setup Complexity** | High (3 processes) | Low (1 process) |
| **Dependencies** | FastAPI, Streamlit, OpenAI, Requests | Gradio only |
| **Use Case** | AI-powered, distributed systems | Simple, direct interface |

## Shared Components

The `shared/` directory contains reusable logic:
- `file_operations.py`: Core file handling functionality
- `random_facts.py`: Random facts data and selection logic

Both versions use these shared components, ensuring consistent behavior while demonstrating different architectural approaches.

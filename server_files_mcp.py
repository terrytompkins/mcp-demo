from mcp.server.fastmcp import FastMCP
import os
import pathlib

ROOT = pathlib.Path(__file__).parent / "files"
ROOT.mkdir(exist_ok=True)

# Create an MCP server
mcp = FastMCP("File Operations Server")

def _safe_path(name: str):
    return ROOT / pathlib.Path(name).name

@mcp.tool()
def list_files() -> list[str]:
    """List files in sandbox directory."""
    return os.listdir(ROOT)

@mcp.tool()
def read_file(filename: str) -> str:
    """Read a file from the sandbox directory."""
    p = _safe_path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File {filename} not found")
    return p.read_text()

@mcp.tool()
def write_file(filename: str, content: str) -> str:
    """Write content to a file in the sandbox directory."""
    p = _safe_path(filename)
    p.write_text(content)
    return f"Successfully wrote {len(content)} characters to {filename}"

# Run the server
if __name__ == "__main__":
    mcp.run() 
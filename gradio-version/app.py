import gradio as gr
import sys
import pathlib

# Add the shared directory to the path
shared_path = pathlib.Path(__file__).parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from file_operations import FileOperations
from random_facts import RandomFacts

# Initialize shared components
file_ops = FileOperations()
random_facts = RandomFacts()

def get_random_fact():
    """Get a random fact."""
    return random_facts.get_random_fact()

def list_files():
    """List all files in the files directory."""
    files = file_ops.list_files()
    if files:
        return "\n".join(files)
    else:
        return "No files found."

def read_file(filename):
    """Read a specific file."""
    if not filename:
        return "Please enter a filename."
    
    result = file_ops.read_file(filename)
    if "error" in result:
        return f"Error: {result['error']}"
    return result["result"]

def write_file(filename, content):
    """Write content to a file."""
    if not filename:
        return "Please enter a filename."
    
    result = file_ops.write_file(filename, content)
    if "error" in result:
        return f"Error: {result['error']}"
    return result["result"]

# Create the Gradio interface
with gr.Blocks(title="File Operations & Random Facts Demo") as demo:
    gr.Markdown("# File Operations & Random Facts Demo")
    gr.Markdown("This is a simpler implementation using Gradio instead of MCP servers.")
    
    with gr.Tab("Random Facts"):
        gr.Markdown("## Get Random Facts")
        fact_button = gr.Button("Get Random Fact")
        fact_output = gr.Textbox(label="Random Fact", lines=3, interactive=False)
        fact_button.click(fn=get_random_fact, outputs=fact_output)
    
    with gr.Tab("File Operations"):
        gr.Markdown("## File Operations")
        
        with gr.Row():
            with gr.Column():
                gr.Markdown("### List Files")
                list_button = gr.Button("List Files")
                list_output = gr.Textbox(label="Files", lines=5, interactive=False)
                list_button.click(fn=list_files, outputs=list_output)
            
            with gr.Column():
                gr.Markdown("### Read File")
                read_filename = gr.Textbox(label="Filename to read")
                read_button = gr.Button("Read File")
                read_output = gr.Textbox(label="File Content", lines=20, interactive=False, max_lines=20)
                read_button.click(fn=read_file, inputs=read_filename, outputs=read_output)
        
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Write File")
                write_filename = gr.Textbox(label="Filename to write")
                write_content = gr.Textbox(label="Content", lines=5)
                write_button = gr.Button("Write File")
                write_output = gr.Textbox(label="Result", lines=2, interactive=False)
                write_button.click(fn=write_file, inputs=[write_filename, write_content], outputs=write_output)

if __name__ == "__main__":
    demo.launch() 
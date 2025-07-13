import os
import pathlib
from typing import List, Dict, Union

class FileOperations:
    def __init__(self, root_dir: str = None):
        """Initialize file operations with a root directory.
        
        Args:
            root_dir: Path to the root directory for file operations.
                     If None, uses the 'files' directory relative to this module.
        """
        if root_dir is None:
            # Default to the 'files' directory at project root
            current_dir = pathlib.Path(__file__).parent
            self.root = current_dir.parent / "files"
        else:
            self.root = pathlib.Path(root_dir)
        
        # Ensure the directory exists
        self.root.mkdir(exist_ok=True)
    
    def _safe_path(self, filename: str) -> pathlib.Path:
        """Create a safe path within the root directory.
        
        Args:
            filename: The filename to create a path for
            
        Returns:
            Path object within the root directory
        """
        return self.root / pathlib.Path(filename).name
    
    def list_files(self) -> List[str]:
        """List all files in the root directory.
        
        Returns:
            List of filenames
        """
        try:
            return os.listdir(self.root)
        except OSError:
            return []
    
    def read_file(self, filename: str) -> Dict[str, Union[str, None]]:
        """Read a file from the root directory.
        
        Args:
            filename: Name of the file to read
            
        Returns:
            Dictionary with 'result' containing file content or 'error' if file not found
        """
        file_path = self._safe_path(filename)
        if not file_path.exists():
            return {"error": "File not found"}
        
        try:
            content = file_path.read_text()
            return {"result": content}
        except Exception as e:
            return {"error": f"Error reading file: {str(e)}"}
    
    def write_file(self, filename: str, content: str) -> Dict[str, str]:
        """Write content to a file in the root directory.
        
        Args:
            filename: Name of the file to write
            content: Content to write to the file
            
        Returns:
            Dictionary with 'result' indicating success or 'error' if failed
        """
        try:
            file_path = self._safe_path(filename)
            file_path.write_text(content)
            return {"result": "File written successfully"}
        except Exception as e:
            return {"error": f"Error writing file: {str(e)}"} 
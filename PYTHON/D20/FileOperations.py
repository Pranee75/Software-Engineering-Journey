# File operation

from pathlib import Path
import shutil

class FileOperations:
    @staticmethod
    def create_and_write_file(file_path: str, content: str) -> None:
        """Creates a file (and parent directories if missing) and writes text to it."""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        print(f"[SUCCESS] Written to file: {path}")

    @staticmethod
    def read_file(file_path: str) -> str:
        """Reads and returns the contents of a file."""
        path = Path(file_path)
        if path.exists() and path.is_file():
            content = path.read_text(encoding='utf-8')
            print(f"[SUCCESS] Read content from: {path}")
            return content
        print(f"[ERROR] File not found: {path}")
        return ""

    @staticmethod
    def append_to_file(file_path: str, content: str) -> None:
        """Appends text to the end of an existing file."""
        path = Path(file_path)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content)
        print(f"[SUCCESS] Appended content to: {path}")

    @staticmethod
    def copy_file(source_path: str, destination_path: str) -> None:
        """Copies a file from source to destination."""
        src = Path(source_path)
        dest = Path(destination_path)
        if src.exists():
            shutil.copy(src, dest)
            print(f"[SUCCESS] Copied {src} to {dest}")
        else:
            print(f"[ERROR] Source file does not exist: {src}")

    @staticmethod
    def delete_file(file_path: str) -> None:
        """Deletes a specific file."""
        path = Path(file_path)
        if path.exists() and path.is_file():
            path.unlink()
            print(f"[SUCCESS] Deleted file: {path}")
        else:
            print(f"[ERROR] File not found or is a directory: {path}")

# --- Sample Execution ---
if __name__ == "__main__":
    target_file = "sample_dir/test.txt"
    
    FileOperations.create_and_write_file(target_file, "Hello, Python!\n")
    FileOperations.append_to_file(target_file, "Adding a new line of text.\n")
    FileOperations.read_file(target_file)
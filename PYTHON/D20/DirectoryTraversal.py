# Directory Traversal

from pathlib import Path

class DirectoryTraversal:
    @staticmethod
    def list_directory_contents(dir_path: str) -> None:
        """Lists all files and subdirectories in a given directory."""
        path = Path(dir_path)
        if not path.exists() or not path.is_dir():
            print(f"[ERROR] Directory not found: {path}")
            return
        
        print(f"--- Contents of {path.resolve()} ---")
        for item in path.iterdir():
            item_type = "DIR " if item.is_dir() else "FILE"
            print(f"[{item_type}] {item.name}")

    @staticmethod
    def find_files_by_pattern(dir_path: str, pattern: str) -> list:
        """Recursively searches for files matching a pattern (e.g., '*.txt')."""
        path = Path(dir_path)
        if not path.exists():
            print(f"[ERROR] Directory not found: {path}")
            return []
        
        matches = list(path.rglob(pattern))
        print(f"--- Found {len(matches)} match(es) for '{pattern}' ---")
        for match in matches:
            print(match)
        return matches

    @staticmethod
    def create_directory(dir_path: str, recursive: bool = True) -> None:
        """Creates a new directory (along with parents if recursive=True)."""
        path = Path(dir_path)
        path.mkdir(parents=recursive, exist_ok=True)
        print(f"[SUCCESS] Directory ready: {path.resolve()}")

    @staticmethod
    def remove_directory(dir_path: str) -> None:
        """Removes an empty directory."""
        path = Path(dir_path)
        try:
            path.rmdir()
            print(f"[SUCCESS] Removed empty directory: {path}")
        except Exception as e:
            print(f"[ERROR] Could not remove directory: {e}")

# --- Sample Execution ---
if __name__ == "__main__":
    test_dir = "sample_dir/sub_folder"
    
    DirectoryTraversal.create_directory(test_dir)
    DirectoryTraversal.list_directory_contents("sample_dir")
    DirectoryTraversal.find_files_by_pattern(".", "*.txt")
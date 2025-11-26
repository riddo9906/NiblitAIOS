# utils/file_manager.py
from pathlib import Path

class FileManager:

    @staticmethod
    def write(path, data):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)

    @staticmethod
    def read(path):
        path = Path(path)
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

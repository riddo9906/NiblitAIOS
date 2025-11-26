# config.py

DEFAULT_CONFIG = {
    "version": "0.1",
    "debug": True,
    "hardware_enabled": True,
    "ai_enabled": True,
    "storage_path": "/data/data/com.termux/files/home/NiblitAIOS/storage"
}

class Config:
    def __init__(self):
        self.data = DEFAULT_CONFIG.copy()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

# Global config instance
config = Config()

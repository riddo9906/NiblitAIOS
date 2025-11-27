# NiblitCore/config.py
import os

# Basic config object. Extend as needed.
class _Config:
    def __init__(self):
        self.env = os.environ.get("NIBLIT_ENV", "development")
        self.data_dir = os.environ.get("NIBLIT_DATA_DIR", os.path.expanduser("~/NiblitAIOS/data"))
        self.log_level = os.environ.get("NIBLIT_LOG_LEVEL", "INFO")
        self.debug = self.env == "development"
        # add network, llm, persistence settings etc.
        self.persistence_file = os.path.join(self.data_dir, "niblit_state.json")

config = _Config()

# core_config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Auto-load .env if exists
ENV_PATH = Path(__file__).parent.parent / ".env"
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)

class CoreConfig:
    NAME = "Niblit AIOS"
    VERSION = "0.1.0"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    DATA_PATH = Path(os.getenv("DATA_PATH", str(Path.home() / "niblit_data")))
    LOG_PATH = DATA_PATH / "logs"

    @staticmethod
    def ensure_paths():
        CoreConfig.DATA_PATH.mkdir(exist_ok=True)
        CoreConfig.LOG_PATH.mkdir(exist_ok=True)

# utils/logger.py
import logging
from pathlib import Path
from core_config import CoreConfig

CoreConfig.ensure_paths()
LOG_FILE = CoreConfig.LOG_PATH / "niblit.log"

logging.basicConfig(
    level=logging.DEBUG if CoreConfig.DEBUG else logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ]
)

logger = logging.getLogger("Niblit")

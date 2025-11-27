# NiblitCore/utils/logger.py
import logging
import sys
import os

def get_logger(name: str):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    # basic console handler
    log_level = os.environ.get("NIBLIT_LOG_LEVEL", "INFO").upper()
    handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter("[%(asctime)s] %(name)s %(levelname)s: %(message)s", "%H:%M:%S")
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, log_level, logging.INFO))
    return logger

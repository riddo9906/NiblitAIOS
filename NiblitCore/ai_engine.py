# ai_engine.py
from utils.logger import logger

class AIEngine:

    def __init__(self):
        logger.info("AIEngine initialized.")

    def respond(self, text):
        logger.info(f"AI received: {text}")
        return f"[Niblit AI] You said: {text}"

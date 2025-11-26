# system_manager.py
from utils.logger import logger
from core_config import CoreConfig
from ai_engine import AIEngine
from event_bus import EventBus

class SystemManager:

    def __init__(self):
        logger.info(f"{CoreConfig.NAME} starting…")
        self.ai = AIEngine()

    def start(self):
        logger.info("SystemManager boot sequence complete.")
        EventBus.emit("system_started")

    def handle_input(self, text):
        return self.ai.respond(text)

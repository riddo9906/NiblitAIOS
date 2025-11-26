# event_bus.py
from utils.logger import logger

class EventBus:
    listeners = {}

    @staticmethod
    def subscribe(event_name, callback):
        EventBus.listeners.setdefault(event_name, []).append(callback)
        logger.info(f"Subscribed to event: {event_name}")

    @staticmethod
    def emit(event_name, data=None):
        logger.info(f"Event emitted: {event_name} | Data: {data}")
        for callback in EventBus.listeners.get(event_name, []):
            try:
                callback(data)
            except Exception as e:
                logger.error(f"Callback error for event {event_name}: {e}")

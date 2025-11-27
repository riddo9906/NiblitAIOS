# NiblitCore/events.py
import threading
from collections import defaultdict
from .utils.logger import get_logger

log = get_logger("Events")

class EventEmitter:
    def __init__(self):
        self._subs = defaultdict(list)
        self._lock = threading.Lock()

    def on(self, event_name: str, handler):
        with self._lock:
            self._subs[event_name].append(handler)
        log.debug(f"Handler added to event '{event_name}'")

    def off(self, event_name: str, handler):
        with self._lock:
            try:
                self._subs[event_name].remove(handler)
            except ValueError:
                pass

    def emit(self, event_name: str, payload=None):
        handlers = list(self._subs.get(event_name, []))
        log.debug(f"Emitting event '{event_name}' to {len(handlers)} handlers")
        for h in handlers:
            try:
                h(payload)
            except Exception as e:
                log.exception(f"Event handler error for '{event_name}': {e}")

# singleton
events = EventEmitter()

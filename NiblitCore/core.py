# core.py

from .registry import ModuleRegistry
from .config import config
from .events import events

class NiblitCore:
    def __init__(self):
        self.registry = ModuleRegistry()
        self.running = False

    def init(self):
        print("[NiblitCore] Initializing core...")

        # fire initialization event
        events.emit("core_init", {"status": "starting"})

        self.running = True

    def load_module(self, name, path):
        self.registry.register(name, path)
        module = self.registry.load(name)

        if module:
            print(f"[Core] Loaded module: {name}")
        else:
            print(f"[Core] Failed to load module: {name}")

    def start(self):
        print("[NiblitCore] Starting system...")
        events.emit("core_start", {"running": True})

    def shutdown(self):
        print("[NiblitCore] Shutting down...")
        events.emit("core_shutdown", {})
        self.running = False

# Global instance for system-wide access
core = NiblitCore()

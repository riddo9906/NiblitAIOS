# NiblitCore/core.py
from .registry import ModuleRegistry
from .events import events
from .config import config
from .utils.logger import get_logger

log = get_logger("NiblitCore")

class NiblitCore:
    def __init__(self):
        self.registry = ModuleRegistry()
        self.running = False

    def init(self):
        log.info("Initializing NiblitCore...")
        events.emit("core_init", {"status": "starting"})
        self.running = True

    def load_module(self, name, path):
        """Register + load a module by name and path."""
        self.registry.register(name, path)
        module = self.registry.load(name)
        if module:
            log.info(f"Loaded module: {name}")
            events.emit("module_loaded", {"name": name})
            return module
        else:
            log.warning(f"Failed to load module: {name}")
            return None

    def start(self):
        log.info("Starting NiblitCore...")
        events.emit("core_start", {"running": True})

    def shutdown(self):
        log.info("Shutting down NiblitCore...")
        events.emit("core_shutdown", {})
        self.running = False

# exported singleton
core = NiblitCore()

# NiblitCore/registry.py
import importlib.util
import importlib
import sys
from types import ModuleType
from .utils.logger import get_logger

log = get_logger("ModuleRegistry")

class ModuleRegistry:
    def __init__(self):
        self._modules = {}       # name -> module object or path
        self._paths = {}         # name -> path

    def register(self, name: str, path: str):
        """Register a module by name and filesystem path or dotted name."""
        self._paths[name] = path
        log.debug(f"Registered module '{name}' -> '{path}'.")

    def load(self, name: str) -> ModuleType | None:
        """Load module from path (filesystem) or dotted import path."""
        path = self._paths.get(name)
        if not path:
            log.error(f"No registered path for module '{name}'")
            return None

        # if path looks like a file, load from file
        if path.endswith(".py"):
            try:
                spec = importlib.util.spec_from_file_location(name, path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[name] = module
                spec.loader.exec_module(module)
                self._modules[name] = module
                log.info(f"Loaded module file: {path}")
                return module
            except Exception as e:
                log.exception(f"Failed to load module file '{path}': {e}")
                return None
        else:
            # dotted import
            try:
                module = importlib.import_module(path)
                self._modules[name] = module
                log.info(f"Imported module: {path}")
                return module
            except Exception as e:
                log.exception(f"Failed to import module '{path}': {e}")
                return None

    def get(self, name: str):
        return self._modules.get(name)

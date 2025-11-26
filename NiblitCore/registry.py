# registry.py
import importlib
import traceback

class ModuleRegistry:
    def __init__(self):
        self.modules = {}
        self.loaded = {}

    def register(self, name, module_path):
        self.modules[name] = module_path

    def load(self, name):
        if name not in self.modules:
            raise Exception(f"Module '{name}' not registered.")

        try:
            module = importlib.import_module(self.modules[name])
            if hasattr(module, "init_module"):
                module.init_module()
            self.loaded[name] = module
            return module
        except Exception as e:
            print(f"[Registry] Failed to load {name}: {e}")
            traceback.print_exc()
            return None

    def get(self, name):
        return self.loaded.get(name)

    def unload(self, name):
        if name in self.loaded:
            if hasattr(self.loaded[name], "shutdown"):
                self.loaded[name].shutdown()
            del self.loaded[name]

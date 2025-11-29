#!/data/data/com.termux/files/usr/bin/python3
"""
Project One Unified Launcher
Author: Riyaad Behardien
Date: 2025-11-30
Description: Unified runtime for NiblitAIOS integrating NiblitCore, NiblitPro, Vercel engine, sensors, memory, and event handling.
"""

import sys, os, time, threading, psutil

# ------------------------------
# Add module paths
# ------------------------------
module_paths = [
    os.path.expanduser("~/NiblitAIOS/Niblit-Modules/Niblit-apk"),
    os.path.expanduser("~/NiblitAIOS/Niblit-Modules/niblit-vercel-fresh"),
    os.path.expanduser("~/NiblitAIOS/Niblit-Modules/GitHub")
]

for path in module_paths:
    if path not in sys.path:
        sys.path.append(path)

# ------------------------------
# Event Dispatcher
# ------------------------------
class Dispatcher:
    def __init__(self):
        self.listeners = {}

    def on(self, event, func):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(func)

    def dispatch(self, event, data=None):
        for func in self.listeners.get(event, []):
            func(data)

dispatcher = Dispatcher()

# ------------------------------
# Import Core Modules
# ------------------------------
try:
    import main_refactor as NiblitPro        # From Niblit-apk
    from NiblitCore import NiblitCore       # Core NiblitCore
    import core.main as engine               # Vercel engine
except ModuleNotFoundError as e:
    print("[ERROR] Missing module:", e)

# ------------------------------
# Initialize Core
# ------------------------------
print("[INFO] Initializing Niblit core...")
core_instance = NiblitCore()
core_instance.initialize()  # Custom init if exists
print("[INFO] NiblitCore Initialized successfully.")

# Initialize NiblitPro (optional features like dashboard, AI memory)
NiblitPro.initialize() if hasattr(NiblitPro, 'initialize') else None
print("[INFO] NiblitPro modules loaded.")

# Initialize Vercel engine modules
engine.initialize() if hasattr(engine, 'initialize') else None
print("[INFO] Engine modules loaded.")

# ------------------------------
# Health Monitor Thread
# ------------------------------
def health_monitor():
    uptime = 0
    while True:
        memory = psutil.virtual_memory().used / 1024**2
        print(f"[HEALTH] Niblit alive | uptime_s={uptime} | memory={memory:.2f} MB")
        uptime += 1
        time.sleep(1)

health_thread = threading.Thread(target=health_monitor, daemon=True)
health_thread.start()

# ------------------------------
# Runtime Loop
# ------------------------------
def run():
    print("[INFO] Starting Project One runtime loop...")
    try:
        while True:
            # Vercel engine updates
            if hasattr(engine, 'update'):
                engine.update()

            # NiblitCore updates
            if hasattr(core_instance, 'update'):
                core_instance.update()

            # NiblitPro updates
            if hasattr(NiblitPro, 'update'):
                NiblitPro.update()

            # Dispatch example events
            dispatcher.dispatch("tick", {"time": time.time()})

            time.sleep(0.1)  # 10Hz loop
    except KeyboardInterrupt:
        print("[INFO] Runtime loop terminated by user.")
        exit(0)

# Example event subscription
def on_tick(data):
    print(f"[EVENT] Tick received: {data['time']}")

dispatcher.on("tick", on_tick)

# ------------------------------
# Main Execution
# ------------------------------
if __name__ == "__main__":
    print("[OK] Project One unified environment loaded.")
    run()

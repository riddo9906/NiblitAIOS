# NiblitCore/ai_engine.py
"""
Small AI engine adapter/stub. Replace methods with real LLM calls
or search adapters later. Keeps stateful context.
"""
from .utils.logger import get_logger

log = get_logger("AIEngine")

class AIEngine:
    def __init__(self):
        self.history = []

    def query(self, prompt: str, max_tokens: int = 256):
        # placeholder: simple echo + record. Replace with LLM adapter
        self.history.append({"prompt": prompt})
        response = f"[stub response] I heard: {prompt[:200]}"
        log.debug(f"AIEngine responding len={len(response)}")
        return response

    def summarize_history(self):
        return "\n".join(h["prompt"] for h in self.history[-20:])

# exported instance
engine = AIEngine()

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_FILE = os.path.join(BASE_DIR, "memory", "long_term.json")


def load_long_term_memory() -> dict:
    """Load long-term memory from disk."""
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # Corrupted or unreadable memory → start clean
        return {}


def save_long_term_memory(memory: dict) -> None:
    """Save long-term memory to disk."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)


def clear_long_term_memory() -> None:
    """Delete all stored long-term memory."""
    save_long_term_memory({})

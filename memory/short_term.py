from collections import deque

# How many conversation turns to remember
MAX_TURNS = 8

# Each item: {"role": "user" | "atlas", "text": "..."}
_short_term_memory = deque(maxlen=MAX_TURNS)

def _is_filler(text: str) -> bool:
    fillers = {"ok", "okay", "thanks", "thank you", "cool", "nice", "exit"}
    return text.lower().strip() in fillers


def add_user_message(text: str) -> None:
    if _is_filler(text):
        return
    _short_term_memory.append({
        "role": "user",
        "text": text
    })


def add_atlas_message(text: str) -> None:
    _short_term_memory.append({
        "role": "atlas",
        "text": text
    })


def get_context() -> str:
    """
    Returns formatted conversation context for the LLM.
    """
    if not _short_term_memory:
        return ""

    lines = ["Conversation so far:"]
    for item in _short_term_memory:
        speaker = "User" if item["role"] == "user" else "ATLAS"
        lines.append(f"{speaker}: {item['text']}")

    return "\n".join(lines) + "\n\n"


def clear_short_term_memory() -> None:
    _short_term_memory.clear()

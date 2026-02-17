import subprocess
import os
from datetime import datetime

from memory.short_term import get_context
from memory.long_term import load_long_term_memory
from core.coding_prompt import CODING_MODE_PROMPT  # 🧠 NEW

# ================= PATHS ==================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODES_DIR = os.path.join(BASE_DIR, "modes")

# ================= LLM ==================

def ask_atlas(prompt: str, mode: str = "chill", coding_mode: bool = False) -> str:
    # -------- Load personality --------
    mode_file = os.path.join(MODES_DIR, f"{mode}.txt")
    with open(mode_file, "r", encoding="utf-8") as f:
        system_prompt = f.read().strip()

    # -------- Coding Mode (ephemeral) --------
    if coding_mode:
        system_prompt = system_prompt + "\n\n" + CODING_MODE_PROMPT

    # -------- Load long-term memory --------
    long_term = load_long_term_memory()
    long_term_block = ""

    if long_term:
        lines = ["Known user facts:"]
        for key, value in long_term.items():
            lines.append(f"- {key}: {value}")
        long_term_block = "\n".join(lines) + "\n\n"

    # -------- Load short-term memory --------
    short_term_block = get_context()

    # -------- Date and Time --------
    now = datetime.now().strftime("%A, %B %d, %Y, %H:%M")
    time_block = f"Current date and time: {now}\n\n"

    # -------- Build final prompt --------
    full_prompt = (
        f"{system_prompt}\n\n"
        f"{time_block}"
        f"{long_term_block}"
        f"{short_term_block}"
        f"User: {prompt}\n"
        f"ATLAS:"
    )

    # -------- Call Ollama --------
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=full_prompt,
        text=True,
        capture_output=True,
        encoding="utf-8"
    )

    return result.stdout.strip()

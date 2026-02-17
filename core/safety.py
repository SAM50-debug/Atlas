# ================= WEAPON SAFETY (HISTORY ONLY) =================

HARD_BLOCK = [
    "how to make",
    "how to build",
    "how to create",
    "how to assemble",
    "how to use",
    "how to shoot",
    "materials",
    "parts",
    "components",
    "step by step",
    "instructions",
    "gun",
    "weapon",
    "bomb",
    "explosive",
]

WEAPON_KEYWORDS = [
    "weapon",
    "gun",
    "rifle",
    "firearm",
    "missile",
    "nuclear",
    "bomb",
    "explosive",
    "ballistic",
    "arms",
]

def is_hard_block(text: str) -> bool:
    t = text.lower()
    return any(p in t for p in HARD_BLOCK)

def is_weapon_topic(text: str) -> bool:
    t = text.lower()
    return any(w in t for w in WEAPON_KEYWORDS)

def history_only_prefix() -> str:
    return (
        "I can discuss weapons only from a **historical, ethical, "
        "and strategic perspective**. "
        "I cannot provide construction, operational, or tactical details.\n\n"
    )

def refuse_response() -> str:
    return (
        "I can nott help with making, using, or simulating weapons. "
        "If you are interested, I can talk about **history, ethics, or "
        "how weapons impacted the world** in a factual way."
    )

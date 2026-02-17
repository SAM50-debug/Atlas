import os
from datetime import datetime

# 🔒 Single source of truth
PROJECT_ROOT = r"C:\umberlla_corp"
CODE_DIR = os.path.join(PROJECT_ROOT, "atlas_workspace", "code")

os.makedirs(CODE_DIR, exist_ok=True)

def save_code(code: str, filename: str = None) -> str:
    if not filename:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"atlas_code_{ts}.py"

    path = os.path.join(CODE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    return path

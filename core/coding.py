import re

CODE_KEYWORDS = [
    "code", "coding", "script", "program",
    "debug", "error", "exception", "traceback",
    "function", "class", "method",
    "compile", "build", "run",
    "fix", "issue", "bug",
]

FILE_EXTENSIONS = [
    ".py", ".cpp", ".c", ".h",
    ".js", ".ts",
    ".java", ".go", ".rs",
    ".html", ".css",
    ".json", ".yaml", ".yml",
]

def is_coding_task(text: str) -> bool:
    text = text.lower()

    # 1️⃣ Code blocks (markdown)
    if "```" in text:
        return True

    # 2️⃣ Stack traces / errors
    if "traceback" in text or "exception" in text:
        return True

    # 3️⃣ File extensions
    for ext in FILE_EXTENSIONS:
        if ext in text:
            return True

    # 4️⃣ Keywords
    for kw in CODE_KEYWORDS:
        if re.search(rf"\b{kw}\b", text):
            return True

    return False

def needs_clarification(text: str) -> bool:
    vague_triggers = [
        "write the script",
        "write a script",
        "write python",
        "create code",
        "make a program",
        "build a script",
    ]

    missing_details = not any(
        kw in text for kw in [
            "python",
            "javascript",
            "file",
            "api",
            "class",
            "function",
            "factorial",
            "calculator",
            "sort",
            "database",
        ]
    )

    return any(v in text for v in vague_triggers) or missing_details


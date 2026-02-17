import re

def extract_code_blocks(text: str):
    """
    Returns (code, remaining_text)
    If no code block exists, code = None
    """
    matches = re.findall(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)

    if not matches:
        return None, text.strip()

    code = "\n\n".join(matches)

    # Remove code blocks from spoken text
    spoken = re.sub(r"```(?:\w+)?\n.*?```", "", text, flags=re.DOTALL).strip()

    return code.strip(), spoken

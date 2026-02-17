import subprocess
import tempfile
import os
import re
import time

PIPER_EXE = r"C:\umberlla_corp\piper\piper.exe"
VOICE_MODEL = r"C:\umberlla_corp\piper\voices\en_US-amy-medium.onnx"
FFPLAY_EXE = r"C:\ffmpeg\bin\ffplay.exe"

def sanitize_text(text: str) -> str:
    # 1️ Remove emojis and non-ascii characters (CRITICAL)
    text = text.encode("ascii", "ignore").decode()

    # 2️ Remove markdown / formatting artifacts
    for ch in ["*", "#", "•", "|", "`", "~"]:
        text = text.replace(ch, "")

    # 3️ Normalize punctuation (better speech flow)
    text = text.replace("...", ".")
    text = text.replace("..", ".")
    text = text.replace("--", "-")

    # 4️ Clean excessive whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

def speak(text):
    if not text:
        return

    print("🔊 Speaking (neural)...")

    clean_text = sanitize_text(text)
    if not clean_text:
        return

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wav_path = f.name

    try:
        # Generate speech
        subprocess.run(
            [
                PIPER_EXE,
                "-m", VOICE_MODEL,
                "-f", wav_path
            ],
            input=clean_text,
            text=True,
            check=True
        )

        # Play audio (BLOCKING)
        subprocess.run(
            [
                FFPLAY_EXE,
                "-autoexit",
                "-nodisp",
                wav_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    finally:
        try:
            os.remove(wav_path)
        except:
            pass

def speak_chunked(text, max_chars=220, pause=0.25):
    """
    Splits long responses into natural chunks
    and speaks them sequentially using Piper.
    """

    if not text:
        return

    # Reuse your sanitizer
    clean = sanitize_text(text)
    if not clean:
        return

    # Split on sentence boundaries
    sentences = re.split(r'(?<=[.!?])\s+', clean)

    buffer = ""
    for sentence in sentences:
        if len(buffer) + len(sentence) <= max_chars:
            buffer += " " + sentence
        else:
            speak(buffer.strip())
            time.sleep(pause)
            buffer = sentence

    # Speak remaining
    if buffer.strip():
        speak(buffer.strip())

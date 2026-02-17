import sounddevice as sd
import numpy as np
import librosa
from faster_whisper import WhisperModel

# ============== CONFIG =================

INPUT_RATE = 48000
MODEL_RATE = 16000
DURATION = 2.5          # short listen
MIC_DEVICE_INDEX = 9

WAKE_PHRASES = [
    "hey atlas",
    "hi atlas",
    "hello atlas"
]

# ============== MODEL ==================

model = WhisperModel(
    "tiny.en",
    device="cpu",
    compute_type="int8"
)

# =======================================

def listen_for_wake_word() -> bool:
    print("🎧 Wake listening...")

    audio = sd.rec(
        int(3.0 * INPUT_RATE),
        samplerate=INPUT_RATE,
        channels=1,
        device=MIC_DEVICE_INDEX,
        dtype="float32",
    )
    sd.wait()

    audio = np.squeeze(audio)

    max_amp = float(np.max(np.abs(audio)))
    print(f"🔊 Wake audio level: {max_amp:.6f}")

    if max_amp < 0.002:
        return False

    audio = librosa.resample(
        audio,
        orig_sr=INPUT_RATE,
        target_sr=MODEL_RATE
    )

    segments, _ = model.transcribe(
        audio,
        language="en",
        beam_size=1,
        temperature=0.0,
        vad_filter=True,
    )

    text = " ".join(s.text for s in segments).lower().strip()

    # Normalize whisper hallucinations
    text = (
        text.replace("at last", "atlas")
        .replace("he at least", "hey atlas")
        .replace("a plus", "atlas")
        .replace("ad last", "atlas")
        .replace(".", "")
        .replace(",", "")
    )

    print(f"🧠 Wake heard: '{text}'")

    return "atlas" in text or "hey atlas" in text

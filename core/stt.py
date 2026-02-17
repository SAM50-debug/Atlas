print("✅ stt.py LOADED")

import sounddevice as sd
import numpy as np
import librosa
import keyboard
from faster_whisper import WhisperModel

# ================= CONFIG =================

MIC_DEVICE_INDEX = 9        # your verified mic
INPUT_RATE = 48000          # native mic rate
MODEL_RATE = 16000          # Whisper expects this
FRAME_SIZE = 1024           # audio chunk size

# ================= MODEL ==================

model = WhisperModel(
    "small.en",
    device="cpu",
    compute_type="int8"
)

# =========================================

def listen_and_transcribe():
    print("🎤 Listening... (hold SPACE)")

    frames = []

    stream = sd.InputStream(
        samplerate=INPUT_RATE,
        channels=1,
        device=MIC_DEVICE_INDEX,
        dtype="float32",
        blocksize=FRAME_SIZE
    )

    with stream:
        # RECORD ONLY WHILE SPACE IS HELD
        while keyboard.is_pressed("space"):
            data, _ = stream.read(FRAME_SIZE)
            frames.append(data)

    if not frames:
        return ""

    # Flatten audio
    audio = np.concatenate(frames, axis=0).squeeze()

    # Downsample for Whisper
    audio = librosa.resample(
        audio,
        orig_sr=INPUT_RATE,
        target_sr=MODEL_RATE
    )

    # Silence guard
    if np.max(np.abs(audio)) < 0.001:
        return ""

    segments, _ = model.transcribe(audio)
    text = "".join(seg.text for seg in segments).strip().lower()

    # Small normalization
    text = text.replace("-", " ")
    text = text.replace(" a i", " ai")
    text = text.replace(" aar", " ai")

    return text

# ATLAS v1.0  
**Adaptive Technical Local Assistant System**

Atlas is a fully offline, voice-driven personal assistant that runs entirely on your local machine.  
It is designed to prioritize **privacy, control, and reliability** over cloud-based convenience.

> No internet. No telemetry. No hidden behavior.

This repository represents **Atlas v1.0 — a frozen, stable build**.

---

## ✨ Key Features

- 🧠 Fully offline LLM (via Ollama)
- 🎙️ Voice interaction with wake-word (“Hey Atlas”)
- 🗣️ Neural Text-to-Speech (Piper)
- 🎧 Push-to-talk input system
- 💤 Auto sleep & reactivation
- 🧾 Short-term conversational memory (session-based)
- 📌 Explicit long-term memory (user-approved only)
- 🛡️ Built-in safety layer (restricted content handling)
- ⏱️ Local date & time grounding
- 🔒 Zero internet access, zero telemetry

---

## 🧠 Design Philosophy

Atlas is built around strict principles:

- **Local-first** → Everything runs on-device  
- **Privacy-respecting** → No cloud APIs, no tracking  
- **Explicit memory** → Nothing is remembered without user consent  
- **Honest responses** → Atlas can say *“I don’t know”*  
- **Stability over features** → Predictable behavior over experimentation  

---

## 🗂️ Project Structure


atlas/
├── main.py # Entry point
│
├── core/
│ ├── llm.py # LLM interface (Ollama)
│ ├── stt.py # Speech-to-text (Whisper)
│ ├── tts.py # Neural TTS (Piper)
│ ├── wake.py # Wake word detection
│ └── safety.py # Safety layer
│
├── memory/
│ ├── short_term.py # Session memory
│ └── long_term.py # Persistent memory
│
├── modes/
│ ├── chill.txt
│ └── professional.txt
│
├── requirements.txt
├── VERSION.txt
└── README.md


---

## 🚀 Getting Started

### Requirements
- Windows 10 / 11  
- Python 3.10.x  
- Ollama (installed separately)  
- Piper TTS  
- FFmpeg / FFplay  
- Microphone  
- (Optional) NVIDIA GPU  

---

### Run Atlas

```bash
python main.py
💻 Coding Mode

Atlas includes a controlled coding interaction mode:

Code is never spoken aloud

Output is written to:

atlas_workspace/code/
Responses remain concise and explanatory
Ambiguous prompts trigger clarification
No execution or external system changes

Coding mode is temporary and request-based.

🔒 Privacy & Safety

Atlas enforces strict guarantees:

Fully offline operation
No telemetry or background tracking
No hidden or automatic memory
No autonomous actions
Restricted topics handled safely (non-operational responses only)
🧠 System Overview
Voice → STT → Safety → Memory → LLM → TTS → Output

For detailed system design, see:

Architecture
❄️ Stability Status

Atlas v1.0 is a frozen build:

No feature changes
Only bug fixes and documentation updates
Behavior is locked and deterministic
🧪 Tested Environment
Windows 11
Python 3.10.x
Ollama (local)
Piper TTS
FFmpeg
NVIDIA GPU (optional)
📜 License

Private / Research / Educational use only

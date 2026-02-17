# ATLAS v1.0  
**Adaptive Technical Local Assistant System**

Atlas is a fully offline, voice-driven personal assistant designed to run locally on a user’s machine.  
It prioritizes privacy, control, reliability, and ethical guardrails over cloud dependency.

This repository represents **Atlas v1.0 — a frozen, stable build**.

-----------------------------------------------------------------------------------------------------

## ✨ Features

- Fully **offline** Large Language Model (via Ollama)
- **Neural text-to-speech** (Piper) with natural sentence chunking
- **Wake-word activation** (“Hey Atlas”)
- **Push-to-talk** interaction
- Automatic **sleep and re-wake**
- Short-term conversational memory (session-based)
- Explicit long-term memory (user-approved only)
- Safety layer with non-operational weapon handling
- Accurate **local date/time grounding**
- No internet access
- No background surveillance

-----------------------------------------------------------------------------------------------------

## 🧠 Design Philosophy

- **Local-first**: All processing happens on the user’s system
- **Privacy-respecting**: No cloud APIs, no telemetry
- **Explicit memory**: Atlas remembers only what the user asks it to
- **Honest responses**: Atlas is allowed to say “I don’t know”
- **Behavior before features**: Stability over novelty

-----------------------------------------------------------------------------------------------------

## 🗂️ Project Structure

atlas/
├── main.py # Entry point
├── core/
│ ├── llm.py # LLM interface (Ollama)
│ ├── stt.py # Speech-to-text (Whisper)
│ ├── tts.py # Neural TTS (Piper)
│ ├── wake.py # Wake word detection
│ └── safety.py # Safety & refusal logic
│
├── memory/
│ ├── short_term.py # Session memory
│ └── long_term.py # Persistent memory
│
├── modes/
│ ├── chill.txt # Casual system prompt
│ └── professional.txt # Formal system prompt
│
├── requirements.txt
├── VERSION.txt
└── README.md


-----------------------------------------------------------------------------------------------------

## 🛠️ System Requirements

- Windows 10 / 11
- Python 3.10.x
- Ollama (installed separately)
- Piper TTS binary
- FFmpeg / FFplay
- Microphone
- (Optional) NVIDIA GPU with CUDA

-----------------------------------------------------------------------------------------------------

## 🚀 Usage

1. Start Ollama server
2. Activate Python virtual environment
3. Run Atlas:
   ```bash
   python main.py

-----------------------------------------------------------------------------------------------------

## Coding Mode (v1.0)
1. When ATLAS detects a coding-related task:
- It does not speak raw code
2. Code is written to a local workspace directory:
- atlas_workspace/code/
- Spoken output is concise and explanatory
- Ambiguous prompts trigger clarification questions
- No execution, no compilation, no external writes
- Coding Mode is ephemeral
- It activates per request and does not alter ATLAS’s global personality.

-----------------------------------------------------------------------------------------------------

## Privacy & Ethics
1. Fully offline by default
2. No telemetry
3. No hidden memory
4. No autonomous action
5. Weapon-related queries are strictly restricted to historical or descriptive context

-----------------------------------------------------------------------------------------------------

## Status: Frozen
1. ATLAS **v1.0** is a frozen build.
2. Only documentation updates and bug fixes are allowed.
3. No behavioral drift is permitted.

-----------------------------------------------------------------------------------------------------

## Tested Environment
1. Windows 11
2. Python 3.10.x
3. NVIDIA GPU (optional)
4. Piper TTS
5. FFmpeg
6. Ollama (local)

-----------------------------------------------------------------------------------------------------

## License
- Private / Research / Educational use only
# ATLAS v1.0 — System Architecture

This document explains how Atlas is structured internally and how its components interact.

-----------------------------------------------------------------------------------------------------

## 🧠 High-Level Architecture

User (Voice)
↓
Microphone
↓
Wake Word Detector
↓
Push-to-Talk Controller
↓
Speech-to-Text (Whisper)
↓
Safety Layer
↓
Memory Layer
↓
Language Model (Ollama)
↓
Text-to-Speech (Piper)
↓
Speaker Output


-----------------------------------------------------------------------------------------------------


## 🔹 Core Components

### 1. Wake System (`core/wake.py`)
- Listens for a predefined wake phrase
- Activates Atlas exactly once per session
- Re-used after auto-sleep
- No continuous background recording

-----------------------------------------------------------------------------------------------------

### 2. Speech-to-Text (`core/stt.py`)
- Uses Faster-Whisper (offline)
- Audio normalization and resampling
- Silence detection prevents false triggers
- Push-to-talk ensures intentional input

-----------------------------------------------------------------------------------------------------

### 3. Safety Layer (`core/safety.py`)
- Detects restricted topics (e.g., weapons)
- Enforces refusal or historical-only responses
- Prevents operational harm
- Applies **before** LLM invocation

-----------------------------------------------------------------------------------------------------

### 4. Memory System

#### Short-Term Memory (`memory/short_term.py`)
- Session-only
- Cleared on sleep or exit
- Stores recent conversational context

#### Long-Term Memory (`memory/long_term.py`)
- Explicit only (via “remember …”)
- User can list or clear memory at any time
- Stored locally in plain format

-----------------------------------------------------------------------------------------------------

### 5. LLM Interface (`core/llm.py`)
- Communicates with Ollama runtime
- Injects:
  - System persona
  - Current date & time
  - Short-term context
  - Approved long-term memory
- No internet access

-----------------------------------------------------------------------------------------------------

### 6. Text-to-Speech (`core/tts.py`)
- Piper neural TTS (offline)
- Sentence chunking for natural prosody
- Sanitization prevents crashes and artifacts
- Blocking playback for correctness

-----------------------------------------------------------------------------------------------------

## 🔄 State Management

Atlas operates in three states:

1. **Sleep**
   - Waiting for wake word
2. **Active**
   - Push-to-talk conversation
3. **Auto-Sleep**
   - Triggered after inactivity
   - Clears short-term memory only

Transitions are deterministic and explicit.

-----------------------------------------------------------------------------------------------------

## 🛡️ Ethical & Safety Guarantees

- No self-ownership claims
- No company identity leakage
- No emotional dependency modeling
- Honest uncertainty handling
- User-controlled memory

-----------------------------------------------------------------------------------------------------

## ⚙️ Performance Characteristics

- GPU only used for LLM (optional)
- Audio processing is lightweight (CPU)
- No background polling loops
- Designed for laptops and desktops

-----------------------------------------------------------------------------------------------------

## ❄️ Stability Policy

This architecture reflects **Atlas v1.0 (Frozen)**.
Future versions may extend components but must preserve:
- Explicit memory control
- Offline-first design
- User agency

-----------------------------------------------------------------------------------------------------

## ATLAS Architecture Overview
ATLAS is designed as a deterministic, modular, offline-first system.

-----------------------------------------------------------------------------------------------------

## Core Layers
[ User Voice ]
      ↓
[ Wake System ]
      ↓
[ STT ]
      ↓
[ Intent & Safety Layer ]
      ↓
[ LLM Prompt Builder ]
      ↓
[ Response Router ]
      ↓
[ TTS / Workspace Output ]

Core Modules
core.wake
Passive listening loop
Activates ATLAS once per session

-----------------------------------------------------------------------------------------------------

## core.stt
1. Records only during push-to-talk
2. No background recording

-----------------------------------------------------------------------------------------------------

## core.llm
1. Builds prompt from:
2. Mode personality
3. Date/time
4. Short-term context
5. Explicit long-term memory
6. Sends prompt to Ollama (local only)

-----------------------------------------------------------------------------------------------------

## core.coding
1. Detects programming intent
2. Flags ambiguity
3. Never executes code

-----------------------------------------------------------------------------------------------------

## core.workspace
1. Writes code output only
2. Path is fixed and controlled:
3. atlas_workspace/code/

-----------------------------------------------------------------------------------------------------

## core.tts
1. Chunked neural speech
2. Sanitized output only
3. Blocking playback (no overlap)
4. Memory Design
5. Short-Term
6. Session-only
7. Automatically cleared on sleep or exit

-----------------------------------------------------------------------------------------------------

## Long-Term
1. Explicit user-approved facts
2. Never inferred
3. Never modified automatically

-----------------------------------------------------------------------------------------------------

## Safety Model
1. Hard refusal for restricted content
2. Historical-only fallback for sensitive topics
3. No self-claims about creators, training sources, or identity beyond system definition

-----------------------------------------------------------------------------------------------------

## Frozen Contract
1. No background autonomy
2. No self-modifying behavior
3. No internet access
4. No hidden memory
5. No silent execution
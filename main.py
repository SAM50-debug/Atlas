import time
import keyboard

from core.wake import listen_for_wake_word
from core.stt import listen_and_transcribe
from core.llm import ask_atlas
from core.tts import speak_chunked

from core.coding import is_coding_task, needs_clarification
from core.workspace import save_code
from core.code_extract import extract_code_blocks   # ✅ NOW USED

from core.safety import (
    is_hard_block,
    is_weapon_topic,
    history_only_prefix,
    refuse_response,
)

from memory.short_term import (
    add_user_message,
    add_atlas_message,
    clear_short_term_memory,
)

from memory.long_term import (
    load_long_term_memory,
    save_long_term_memory,
    clear_long_term_memory,
)

# ================= CONFIG ==================

mode = "chill"
PUSH_KEY = "space"
AUTO_SLEEP_SECONDS = 300  # 5 minutes

# ================= UI ==================

print("\nATLAS is online")
print("Say 'Hey Atlas' to activate")
print("Then use push-to-talk\n")

print("Commands:")
print("• mode chill")
print("• mode professional")
print("• remember ...")
print("• what do you remember about me")
print("• forget everything about me")
print("• exit\n")

# ================= STATE ==================

last_interaction_time = time.time()

# ================= WAKE PHASE ==================

def wait_for_wake():
    print("🕒 Waiting for wake word...")
    while True:
        if listen_for_wake_word():
            speak_chunked("Yes?")
            time.sleep(0.2)
            print("✅ Atlas activated\n")
            return
        time.sleep(0.2)

# ================= START ==================

try:
    wait_for_wake()
except KeyboardInterrupt:
    print("\n🛑 Atlas stopped by user.")
    exit(0)

# ================= ACTIVE PHASE ==================

print("🎧 Atlas is ACTIVE")
print("Hold [SPACE] to talk\n")

while True:
    try:
        # ---------- AUTO SLEEP ----------
        if time.time() - last_interaction_time > AUTO_SLEEP_SECONDS:
            speak_chunked("Going to sleep.")
            clear_short_term_memory()
            print("💤 Atlas sleeping\n")
            wait_for_wake()
            print("🎧 Atlas is ACTIVE again\n")
            last_interaction_time = time.time()

        print("🕒 Idle — hold [SPACE] to talk")
        keyboard.wait(PUSH_KEY)

        user_input = listen_and_transcribe()

        while keyboard.is_pressed(PUSH_KEY):
            time.sleep(0.01)

        if not user_input:
            continue

        last_interaction_time = time.time()

        print(f"🗣️ Heard: '{user_input}'")
        text = user_input.lower().strip()

        # ---------- CODING MODE DETECTION ----------
        coding_task = is_coding_task(text)
        if coding_task:
            print("🧠 Coding task detected")

        # ---------- EXIT ----------
        if "exit" in text:
            speak_chunked("Shutting down. Goodbye.")
            time.sleep(0.3)
            break

        # ---------- MODE SWITCH ----------
        if "professional" in text:
            mode = "professional"
            speak_chunked("Switched to professional mode.")
            continue

        if "chill" in text:
            mode = "chill"
            speak_chunked("Switched to chill mode.")
            continue

        # ---------- MEMORY READ ----------
        if "what do you remember about me" in text:
            memory = load_long_term_memory()
            if not memory:
                response = "I do not remember anything about you yet."
            else:
                lines = ["Here is what I remember about you."]
                for _, v in memory.items():
                    lines.append(f"You mentioned that {v}.")
                response = " ".join(lines)

            speak_chunked(response)
            add_atlas_message(response)
            continue

        # ---------- MEMORY CLEAR ----------
        if "forget everything about me" in text:
            clear_long_term_memory()
            speak_chunked("I have cleared everything I remembered about you.")
            continue

        # ---------- MEMORY WRITE ----------
        if text.startswith("remember"):
            fact = text.replace("remember", "").strip()
            if fact:
                memory = load_long_term_memory()
                memory[f"fact_{len(memory) + 1}"] = fact
                save_long_term_memory(memory)
                speak_chunked("Okay. I will remember that.")
            else:
                speak_chunked("What would you like me to remember?")
            continue

        # ---------- CODING CLARIFICATION GUARD ----------
        if coding_task and needs_clarification(text):
            response = (
                "I need a bit more detail to help correctly. "
                "What language, environment, or problem are you working on?"
            )
            print(f"\nATLAS ({mode}): {response}\n")
            speak_chunked(response)
            continue

        # ---------- NORMAL FLOW ----------
        add_user_message(user_input)

        if is_hard_block(text):
            response = refuse_response()

        elif is_weapon_topic(text):
            response = history_only_prefix() + ask_atlas(
                user_input, mode, coding_mode=coding_task
            )

        else:
            response = ask_atlas(
                user_input, mode, coding_mode=coding_task
            )

        add_atlas_message(response)

        print(f"\nATLAS ({mode}):\n{response}\n")

        # ---------- CODING OUTPUT HANDLING ----------
        if coding_task:
            code, spoken = extract_code_blocks(response)

            if code:
                file_path = save_code(code)
                print(f"📁 Code saved to: {file_path}")
                speak_chunked(
                    "I have written the code to your workspace. "
                    "I can explain it or make changes."
                )
            else:
                speak_chunked(spoken)

        else:
            speak_chunked(response)

        last_interaction_time = time.time()
        time.sleep(0.3)

    except KeyboardInterrupt:
        print("\n🛑 Atlas stopped by user.")
        break

# ================= CLEAN EXIT ==================

clear_short_term_memory()

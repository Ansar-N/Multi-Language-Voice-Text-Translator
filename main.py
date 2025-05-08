import customtkinter as ctk
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import os
import playsound
import threading
from datetime import datetime

# Setup Appearance
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

# App Init
app = ctk.CTk()
app.title("🌍 Multi-Language Voice & Text Translator")
app.geometry("700x700")
app.resizable(False, False)

# Language options
LANGUAGE_OPTIONS = {
    "Auto-Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Malayalam": "ml",
    "Telugu": "te",
    "Hindi": "hi",
    "French": "fr"
}

# ===== Functions =====

def update_status(msg, color="gray"):
    status_label.configure(text=msg, text_color=color)

def voice_to_voice():
    threading.Thread(target=process_voice_to_voice).start()

def process_voice_to_voice():
    try:
        source_lang = LANGUAGE_OPTIONS[input_lang_var.get()]
        target_lang = LANGUAGE_OPTIONS[output_lang_var.get()]

        update_status(f"🎤 Listening in {input_lang_var.get()}...", "blue")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        update_status("🧠 Recognizing speech...", "orange")
        text = recognizer.recognize_google(audio, language="en" if source_lang == "auto" else source_lang)
        input_box.delete(0, 'end')
        input_box.insert(0, text)

        process_translation(text, source_lang, target_lang)

    except sr.UnknownValueError:
        update_status("❌ Couldn't understand your voice.", "red")
    except sr.RequestError:
        update_status("❌ Network issue with speech service.", "red")
    except Exception as e:
        update_status(f"❌ Error: {e}", "red")

def text_to_text():
    threading.Thread(target=process_text_to_text).start()

def process_text_to_text():
    text = input_box.get()
    if text.strip():
        source_lang = LANGUAGE_OPTIONS[input_lang_var.get()]
        target_lang = LANGUAGE_OPTIONS[output_lang_var.get()]
        process_translation(text, source_lang, target_lang)

def process_translation(text, source_lang, target_lang):
    try:
        update_status("🌐 Translating...", "orange")
        translator = Translator()
        result = translator.translate(text, src=source_lang, dest=target_lang)
        translated = result.text
        output_box.delete(0, 'end')
        output_box.insert(0, translated)

        update_status("🔊 Speaking...", "green")
        tts = gTTS(text=translated, lang=target_lang)
        filename = "translated_voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

        update_status("✅ Done!", "green")
    except Exception as e:
        update_status(f"❌ Translation error: {e}", "red")

def save_to_file():
    input_text = input_box.get()
    output_text = output_box.get()
    if input_text and output_text:
        with open("translations.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}]\nInput: {input_text}\nOutput: {output_text}\n\n")
        update_status("💾 Saved to translations.txt", "green")
    else:
        update_status("⚠ Nothing to save!", "orange")

def swap_languages():
    current_input = input_lang_var.get()
    current_output = output_lang_var.get()
    input_lang_var.set(current_output)
    output_lang_var.set(current_input)

# ===== UI Layout =====

title = ctk.CTkLabel(app, text="🌍 Voice & Text Translator", font=("Helvetica", 22, "bold"))
title.pack(pady=15)

# Language selectors
input_lang_var = ctk.StringVar(value="English")
output_lang_var = ctk.StringVar(value="Tamil")

lang_frame = ctk.CTkFrame(app)
lang_frame.pack(pady=5)

input_lang_menu = ctk.CTkOptionMenu(lang_frame, values=list(LANGUAGE_OPTIONS.keys()), variable=input_lang_var, width=200)
output_lang_menu = ctk.CTkOptionMenu(lang_frame, values=list(LANGUAGE_OPTIONS.keys()), variable=output_lang_var, width=200)

input_lang_menu.grid(row=0, column=0, padx=10, pady=5)
swap_btn = ctk.CTkButton(lang_frame, text="🔁 Swap", command=swap_languages, width=80)
swap_btn.grid(row=0, column=1, padx=10)
output_lang_menu.grid(row=0, column=2, padx=10, pady=5)

input_box = ctk.CTkEntry(app, placeholder_text="🗣 Speak or type here...", width=580, height=40, font=("Arial", 14))
input_box.pack(pady=10)

output_box = ctk.CTkEntry(app, placeholder_text="📜 Translated output...", width=580, height=40, font=("Arial", 14))
output_box.pack(pady=10)

# Buttons
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=15)

voice_btn = ctk.CTkButton(btn_frame, text="🎤 Voice Translate", command=voice_to_voice, width=160)
text_btn = ctk.CTkButton(btn_frame, text="✍ Text Translate", command=text_to_text, width=160)
save_btn = ctk.CTkButton(btn_frame, text="💾 Save Translation", command=save_to_file, width=160)

voice_btn.grid(row=0, column=0, padx=10, pady=5)
text_btn.grid(row=0, column=1, padx=10, pady=5)
save_btn.grid(row=0, column=2, padx=10, pady=5)

# Status
status_label = ctk.CTkLabel(app, text="", font=("Arial", 13), text_color="gray")
status_label.pack(pady=10)

# ===== Run App =====
app.mainloop()

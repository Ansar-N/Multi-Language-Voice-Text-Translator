# 🗣️ Voice & Text Translator with Language Support

A sleek, modern, and multilingual translator application built with Python. Translate voice or text input between multiple languages in real time using a responsive and threaded UI powered by CustomTkinter.

---

## 🎯 Overview

- **Dual Translation Modes:**  
  - **Voice-to-Voice:** Speak your input and listen to the translated output.
  - **Text-to-Text:** Type your input and view the translated text instantly.

- **Multilingual Support:**  
  Supports languages like English, Tamil, Malayalam, Telugu, Hindi, and French with natural dialogue-style text display.

- **Real-Time Feedback:**  
  Uses gTTS for immediate speech output and offers smooth theme transitions (dark/light mode).

- **User-Friendly Interface:**  
  Designed for a modern and intuitive experience with a clean UI and accessible controls.

---

## 🌟 Features

- **Speech Recognition:** Convert spoken words to text.
- **Text Translation:** Instant translation across multiple languages.
- **Speech Output:** Listen to the translated text.
- **Theme Toggle:** Easily switch between dark and light themes.
- **History:** Save translations with timestamps for future reference.
- **Threaded Operations:** Enjoy a responsive interface without freezing.

---

## 📸 Screenshots

Replace the image URLs below with your actual screenshot URLs or local image paths if working offline:

- **Dark Mode:**  
  ![Dark Mode](your_dark_mode_screenshot.png)
- **Light Mode:**  
  ![Light Mode](your_light_mode_screenshot.png)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

Open your terminal (Command Prompt or PowerShell) and run:

```bash
git clone https://github.com/Ansar-N/Multi-Language-Voice-Text-Translator.git
cd Multi-Language-Voice-Text-Translator
```

### 2️⃣ Create a Virtual Environment

Create and activate the virtual environment:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies

Install the required libraries:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

Launch the app with:

```bash
python main.py
```

Once launched, you can:

- **Tap the mic icon** to start speaking.
- **Type in the text field** to enter your content.
- **Select input/output languages** using the dropdown menus.
- **Toggle between dark and light themes** for your preferred view.
- **Save translations** for later reference with a single click.

---

## ⚙️ Tech Stack

| Purpose              | Library                  |
|----------------------|--------------------------|
| **GUI Framework**    | customtkinter            |
| **Voice Recognition**| speechrecognition        |
| **Text-to-Speech**   | gTTS                     |
| **Translation**      | googletrans==4.0.0rc1     |
| **Sound Playback**   | playsound                |

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions, suggestions, and pull requests are welcome!  
Feel free to fork the repository and improve the project. For major changes, open an issue first to discuss what you would like to change.

---

Happy Translating!  

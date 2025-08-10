# 🗣️ AI Voice Assistant in Python

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

A **smart voice assistant** built in Python that listens to your commands 🎙️, understands them in **Russian**, and performs various tasks — from opening websites 🌐 to chatting with **Google Gemini AI** 🤖.  
It’s like Jarvis, but written in Python.

---

## ✨ Features

- 🔊 **Text-to-Speech (TTS)** — Natural speech output using `pyttsx3`.
- 🧠 **Voice Recognition** — Google Speech Recognition API.
- 🎯 **Fuzzy Command Matching** — Tolerates typos and variations with `fuzzywuzzy`.
- 🤖 **Google Gemini AI Integration** — Chat with AI.
- 📷 **Screenshots** — Capture your screen instantly.
- 📅 **Date & Time Announcements** — Get current date, day, and time.
- ✅ **Voice-Controlled Todo List** — Add and manage notes hands-free.
- 🌐 **Web Shortcuts** — Open YouTube, GitHub, Google, and more.
- 🔉 **Feedback Sounds** — Interaction confirmation.
- 👋 **Personalized Greetings** — Custom welcome and goodbye messages.

---

## 📂 Project Structure

```
📦 AI-Voice-Assistant
 ┣ 📜 main.py                # Main assistant code
 ┣ 📜 commands.py            # Command definitions and settings
 ┣ 📜 sounds/                 # Sound effects for feedback
 ┗ 📜 README.md               # Project documentation
```

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/username/ai-voice-assistant.git
cd ai-voice-assistant
```

### 2️⃣ Install dependencies
```bash
pip install pyttsx3 speechrecognition playsound3 fuzzywuzzy python-Levenshtein google-generativeai pyautogui
```

### 3️⃣ (Optional) Install additional system dependencies
- **Windows**: Works out of the box.
- **Linux**: May require `portaudio` and `espeak`  
  ```bash
  sudo apt install portaudio19-dev espeak
  ```

---

## 🚀 Usage

Run the assistant:
```bash
python main.py
```

Then:
1. Say a command in **Russian** 🎤.
2. The assistant will recognize and execute it.
3. Enjoy hands-free automation!

---

## 🎙 Example Commands

| Command (Russian)                  | Action                                  |
|------------------------------------|------------------------------------------|
| "Открой YouTube"                   | Opens YouTube in browser                 |
| "Сделай скриншот"                  | Saves a screenshot                       |
| "Какое сегодня число?"             | Announces today's date                   |
| "Добавь в заметки купить молоко"   | Adds a todo item                         |
| "Скажи время"                      | Speaks the current time                  |
| "Привет"                           | Responds with a greeting                 |
| "Пока"                             | Says goodbye and exits                   |

---

## ⚙ Configuration

All customizable settings (voice, rate, volume, commands, sounds) are stored in:
```
commands.py
```

---

## 🛠 Technologies Used

- [Python](https://www.python.org/) 🐍
- [pyttsx3](https://pypi.org/project/pyttsx3/) — Text-to-Speech
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — Voice input
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/) — Command similarity matching
- [Google Generative AI](https://ai.google/) — AI responses
- [pyautogui](https://pyautogui.readthedocs.io/) — Screenshots & automation



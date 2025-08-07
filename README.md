# 🗣️ AI Voice Assistant on Python

This project is a smart voice assistant built in Python. It listens for voice commands in Russian, recognizes and executes them using predefined logic and integrates with various services such as YouTube, GitHub, Google Gemini, and more.

## 🎯 Features

- 🔊 Text-to-speech (TTS) via `pyttsx3`
- 🧠 Voice recognition using Google Speech Recognition API
- 🤖 Fuzzy matching for commands (with `fuzzywuzzy`)
- 💬 Integration with Gemini AI (Google Generative AI)
- 📷 Take screenshots
- 📅 Announce current time/date/day
- ✅ Todo-list notes by voice
- 🌐 Open popular websites
- 🔉 Feedback sounds for interaction
- 👋 Personalized greetings and exit sounds

## 📦 Dependencies

Install the required packages with:

```bash
pip install pyttsx3 speechrecognition playsound3 fuzzywuzzy python-Levenshtein google-generativeai pyautogui 

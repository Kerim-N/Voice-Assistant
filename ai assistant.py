# ===================== LIBRARIES =======================
import sys, os
import datetime
import random
import webbrowser
import pyautogui
import speech_recognition as sr
import pyttsx3
from playsound3 import playsound
from fuzzywuzzy import fuzz
import google.generativeai as genai
from commads import config, sounds  # your custom configuration module

# ===================== TEXT-TO-SPEECH SETUP =======================
engine = pyttsx3.init(driverName='sapi5')  # Initialize TTS engine (Windows SAPI5)
voices = engine.getProperty('voices')      # Get available voices
engine.setProperty('voice', voices[0].id)  # Select default voice

# ===================== GEMINI AI SETUP =======================
genai.configure(api_key="AIzaSyDnqnKxDyiyDuZeueyGOspT-vwQ9VzadUQ")
model = genai.GenerativeModel("gemini-2.0-flash")

# ===================== TTS FUNCTION =======================
def say(Text):
    try:
        print("[log] Response: " + Text)
        engine.say(Text)
        engine.runAndWait()
    except:
        print("[log] Say Error")

# ===================== VOICE LISTENER =======================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[log] Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)  # Reduce noise
        audio = r.listen(source, 0, 5)  # timeout: 0, phrase_time_limit: 5 sec

    try:
        print("[log] Recognizing...")
        voice = r.recognize_google(audio, language='ru-RU').lower()
        print(f"[log] Recognized: {voice}")
        return voice
    except sr.UnknownValueError:
        print("[log] Could not understand the speech")
        return ""
    except sr.RequestError as e:
        print(f"[log] Recognition service error: {e}")
        return ""

# ===================== COMMAND RECOGNITION =======================
def recognize_cmd(command):
    RC = {"cmd": "", "percent": 0}
    for key, value in config["cmds"].items():
        for item in value:
            vrt = fuzz.ratio(command, item)
            # print(f"[log] Match: {vrt} -> {item}")
            if vrt >= 80:
                RC["cmd"] = key
                RC["percent"] = vrt
    return RC

# ===================== COMMAND EXECUTION =======================
def execute_cmd(cmd):
    print("[log] Command recognized: " + cmd)
    try:
        if cmd == "time":
            now = datetime.datetime.now()
            say("Current time is " + str(now.hour) + ":" + str(now.minute))
        elif cmd == "date":
            date = datetime.datetime.now()
            say("Today is " + str(date.day) + "." + str(date.month) + "." + str(date.year))
        elif cmd == "day":
            date = datetime.datetime.now()
            say("Today is the " + str(date.day))
        elif cmd == "todo":
            playsound(sounds["ok1"])
            text = listen()
            with open("todo list/list.txt", "a", encoding="utf-8") as file:
                file.write(" ✔ " + text + "\n")
            print("[log] Added to todo: " + text + "\n")
            playsound(sounds["ok3"])
        elif cmd == "youtube":
            playsound(sounds["ok2"])
            webbrowser.open("https://www.youtube.com")
            playsound(sounds["ok3"])
            print("[log] Youtube opened")
        elif cmd == "github":
            playsound(sounds["ok2"])
            webbrowser.open("https://github.com")
            playsound(sounds["ok3"])
            print("[log] Github opened")
        elif cmd == "screenshot":
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshots/screenshot.png")
            playsound(sounds["ok3"])
        elif cmd == "thanks":
            playsound(sounds["thanks"])
        elif cmd == "exit":
            playsound(sounds["exit"])
            sys.exit(0)
        elif cmd != "None":
            # Ask Gemini if no known command is matched
            chat = str(model.generate_content(
                cmd + ". отвечай без спец символов. используй только точку, знак препинание, восклицательный и вопросительный знакю"
            ).text)
            say(chat)
    except:
        print("[log] Execute Error")

# ===================== CALLBACK PROCESSING =======================
def callback(voice):
    try:
        cmd_text = str(voice)
        cmd_text_tbr = cmd_text

        # Remove assistant's name and trigger words
        for i in config["name"]:
            cmd_text_tbr = cmd_text_tbr.replace(i, "").strip()
        for i in config["tbr"]:
            cmd_text_tbr = cmd_text_tbr.replace(i, "").strip()

        print(cmd_text_tbr)

        # Match command
        cmd = recognize_cmd(cmd_text_tbr)

        if cmd["cmd"] != "":
            execute_cmd(cmd["cmd"])
        elif cmd_text == "кеша":
            playsound(random.choice(sounds["greet"]))
        else:
            execute_cmd(cmd_text)
    except:
        print("[log] Callback Error")

# ===================== MAIN LOOP =======================
def main():
    try:
        while True:
            voice = listen()
            if voice:
                callback(voice)
    except:
        print("[log] Main Error")

# ===================== ENTRY POINT =======================
if __name__ == "__main__":
    playsound(sounds["start"])  # Startup sound
    main()

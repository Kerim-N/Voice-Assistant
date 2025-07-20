
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
from commads import config, sounds

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# for idx, voice in enumerate(voices):
#     print(f"{idx}: {voice.name} | id={voice.id} | gender={voice.gender}")

genai.configure(api_key="AIzaSyDnqnKxDyiyDuZeueyGOspT-vwQ9VzadUQ")
model = genai.GenerativeModel("gemini-2.0-flash")

# config = {
#     "name": ["кеша"],
#     "tbr": ["подскажи", "скажи","расскажи", "покажи", "сколько", "произнеси","открой",
#             "запусти","запускай","сделай","делай","добавь","добавить"],
#     "cmds": {
#         "time": ["текущее время", "который час", "сейчас времени",
#                     "сколько время", "какое сейчас время", "время"],
#         "day": ["какой день", "день недели", "какой сегодня день"],
#         "date": ["какое сегодня число","какая сегодня дата", " сегодняшнее число", "число", "дата"],
#         "weather": ["погода", "погода на сегодня", "сегодняшнюю погоду",
#                     "какое погода", "какое сегодня погода"],
#         "todo": ["заметку", "заметка", "список", "дело", "список дел"],
#         "reminder": ["напоминание в", "напомни", "уведомление в"],
#         "youtube": ["youtube"],
#         "github": ["github"],
#         "screenshot": ["screenshot", "скриншот", ""],
#         "exit": ["выход", "отключись", "завершить работу", "завершение работы", "заткнись", 
#                  "выйти", "пока", "до свидания", "отключайся"],
#         "thanks": ["спасибо","благодарю","спасибо за помощь","лучший"]
#     }
# }

# sounds = {
#     "start": "voices_rus/run.wav",
#     "greet": [
#         "voices_rus/greet1.wav",
#         "voices_rus/greet2.wav",
#         "voices_rus/greet3.wav"
#     ],
#     "ok1": "voices_rus/ok1.wav",
#     "ok2": "voices_rus/ok2.wav",
#     "ok3": "voices_rus/ok3.wav",
#     "exit": "voices_rus/off.wav",
#     "thanks": "voices_rus/thanks.wav"
# }

def say(Text):
    try:
        print("[log] Ответ: " + Text)
        engine.say(Text)
        engine.runAndWait()
    except:
        print("[log] Say Error")
        
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[log] Слушаю...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5 )
        audio = r.listen(source,0,5)
    try:
        print("[log] Распознание...")
        voice = r.recognize_google(audio, language='ru-RU').lower()
        print(f"[log] Распознано: {voice}")
        return voice
    except sr.UnknownValueError:
        print("[log] He удалось распознать речь")
        return ""
    except sr.RequestError as e:
        print(f"[log] Ошибка сервиса распознавания: {e}")
        return ""
        
def recognize_cmd(command):
    RC = {"cmd": "", "percent": 0}
    for key,value in config["cmds"].items():
        for item in value:
            vrt = fuzz.ratio(command, item)
            # print("[log] vrt " + str(vrt) + " " + item)
            if 80 <= vrt:
                RC["cmd"] = key
                RC["percent"] = vrt
    return RC

def execute_cmd(cmd):
    print("[log] Распознанная команда: "+ cmd)
    try:
        if cmd == "time":
            now = datetime.datetime.now()
            say("Сейчас " + str(now.hour) + ":" + str(now.minute))
        elif cmd == "date":
            date = datetime.datetime.now()
            say("Сегодня " + str(date.day) + "." + str(date.month) + "." + str(date.year))
        elif cmd == "day":
            date = datetime.datetime.now()
            say("Сегодня " + str(date.day))
        elif cmd == "todo":
            playsound(sounds["ok1"])
            text = listen()
            with open("todo list/list.txt","a", encoding="utf-8") as file:
                file.write(" ✔ " + text + "\n")
            print("[log] B заметки добавлено: " + text + "\n")
            playsound(sounds["ok3"])
        elif cmd == "youtube":
            playsound(sounds["ok2"])
            webbrowser.open("https://www.youtube.com")
            playsound(sounds["ok3"])
            print("[log] Youtube открыт")
        elif cmd == "github":
            playsound(sounds["ok2"])
            webbrowser.open("https://github.com")
            playsound(sounds["ok3"])
            print("[log] Gtihub открыт")
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
            chat = str(model.generate_content(cmd + ". отвечай без спец символов. используй только точку, знак препинание, восклицательный и вопросительный знакю").text)
            say(chat)
    except:
        print("[log] Execute Error")

def callback(voice):
    try:
        cmd_text = str(voice)
        cmd_text_tbr = cmd_text
        for i in config["name"]:
            cmd_text_tbr = cmd_text_tbr.replace(i, "").strip()
        for i in config["tbr"]:
            cmd_text_tbr = cmd_text_tbr.replace(i, "").strip()
        print(cmd_text_tbr)
        cmd = recognize_cmd(cmd_text_tbr)
        if cmd["cmd"] != "":
            execute_cmd(cmd["cmd"])
        elif cmd_text == "кеша":
            playsound(random.choice(sounds["greet"]))
        else:
            execute_cmd(cmd_text)
    except:
        print("[log] Callback Error")
        
def main():
    try:
        # while True:
        #     voice = listen()
        #     if config["name"][0] in voice:
        #      playsound(random.choice(sounds["greet"]))
        while True:
            voice = listen()
            if voice:
                callback(voice)   
    except:
        print("[log] Main Error")
        
if __name__ == "__main__":
    playsound(sounds["start"])
    main()
    
from distutils.command.config import LANG_EXT
from sys import maxunicode
from threading import main_thread
from tkinter import mainloop
from unittest import expectedFailure
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<=18:
        speak ("good afternoon sir!")
    
    else:
        speak("Good Evening sir!")
    
    speak("please tell me how may I help you ")
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        # prijnt(e)

        print("Say that again please....")
        return "None"
        return query
if __name__ == "__main__":
    wishMe()
    takeCommand()
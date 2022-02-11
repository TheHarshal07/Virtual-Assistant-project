from distutils.command.config import LANG_EXT
from fnmatch import translate
from sys import maxunicode
from threading import main_thread
from time import time
from tkinter import mainloop
from typing import Text
from unittest import expectedFailure
import webbrowser
from winreg import QueryInfoKey
from pip import main
import pyttsx3
import datetime
from playsound import playsound
import speech_recognition as sr 
import wikipedia
from googletrans import Translator
import os 


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
        speak("Good Morning sir!")

    elif hour>=12 and hour<=18:
        speak ("good afternoon sir!")
    
    else:
        speak("Good Evening sir !")
    
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
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
          print("Recognizing...")
          query = r.recognize_google(audio, language='hi')
          print(f"You said: {query}\n")

        except Exception as e:
          return "None"

        return query.lower()

def Tran():
    speak("Tell Me The Line!")
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line, dest='hi')
    Text = result.text
    speak("The Translation For This Line is:"+Text)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'alarm' in query:
            speak("Enter the Time!") 
            time = input(": Please, Enter the Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")    

                if now == time:
                    speak("Time to wake up ma'am!") 
                    playsound('wakeup.mp3')
                    speak("Alarm Closed!")

                elif now>time:
                    break


        elif 'remember that' in query:
                    rememberMsg = query.replace("remember that","")
                    rememberMsg = rememberMsg.replace("jarvis","")
                    speak("You Tell Me To Remind You That: "+rememberMsg)
                    remember = open('data.txt','w')
                    remember.write(rememberMsg)
                    remember.close()

        elif 'what do you remember' in query:
                    remember = open('data.txt','r') 
                    speak("You Tell Me That" +remember.read())  

        elif 'translator' in query:
                    Tran()
               
            
import codecs
from distutils.command.config import LANG_EXT
from fnmatch import translate
from posixpath import splitdrive
from sys import maxunicode
from threading import main_thread
from time import time
from tkinter import mainloop
from typing import Text
from unittest import expectedFailure
from winsound import PlaySound
from pkg_resources import split_sections
from pywikihow import search_wikihow
import webbrowser
from winreg import QueryInfoKey
from pip import main
import pyttsx3
import datetime
from playsound import playsound
import speech_recognition as sr 
from bs4 import BeautifulSoup
import wikipedia
from googletrans import Translator
from gtts import gTTS
import os
import requests
import pywhatkit
import PyPDF2






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
        speak("Good Evening Shravani !")
    
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

    except:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

def takeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"User said: {query}\n")

    except:
        # print(e)
        print("Say that again please....")
        return "None"
    return query.lower()

def Tran():
    speak("Tell Me The Line!")
    line = takeHindi()
    translate = Translator()
    result = translate.translate(line)
    Text = result.text
    speak(Text)

def Temp ():
    search = "temperature in Mumbai"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    speak(f"The Temperature Outside Is {temperature} celsius")
    print(f"The Temperature Outside Is {temperature} celsius")

def Reader():
    speak("Tell Me The Name Of The Book!")

    name = takeCommand() 

    if 'India' in name:

        os.startfile('C:/Users/dnyan/OneDrive/%E0%A4%A6%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A5%87%E0%A4%9C%E0%A4%BC/4th%20standard%20History%20book.pdf')
        book = open('C:/Users/dnyan/OneDrive/%E0%A4%A6%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%A4%E0%A4%BE%E0%A4%B5%E0%A5%87%E0%A4%9C%E0%A4%BC/4th%20standard%20History%20book.pdf','rb')
        pdfreader = PyPDF2.PdffileReader(book)
        pages = pdfreader.getNumPages()
        speak(f"Number of the pages in this books are {pages}") 
        speak("From which page I have to start Reading?")
        numPage = int(input("Enter the Page Number :")) 
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        speak("In which Language, I have to Read ?")
        lang = takeCommand()

        if 'hindi' in lang:
            transl = Translator()
            textHin = transl.translate(text,'hi')
            textm = textHin.text 
            speech = gTTS(text = textm)
            try:
                speech.save('book.mp3')
                playsound('book.mp3')
          
            except:
                playsound('book.mp3')


        else:
            speak(text)
         

if __name__== "__main__":
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
                    playsound('wakeup alarm.mp3')
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

        elif 'temperature' in query: 
                    Temp() 

        elif 'google search' in query:
                    import wikipedia as googlescrap
                    query = query.replace("jarvis","")
                    query = query.replace("google search","")  
                    query = query.replace("google","")
                    speak("This is what I found on the web!")
                    pywhatkit.search(query)

                    try:
                        result = googlescrap.summary(query,3)
                        speak(result)

                    except:
                        speak("No Speakable Data Available!")    
                
        elif 'youtube search' in query:
                    Query = query.replace("jarvis","")
                    query = Query.replace("youtube search","")
                    from feature import YoutubeSearch
                    YoutubeSearch(query)
    
        elif 'how to' in query:
            speak("Getting Data From The Internet!")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'read book' in query:
            Reader()

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()    



     
    

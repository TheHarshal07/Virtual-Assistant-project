from cmath import log
import codecs
from distutils.command.config import LANG_EXT
from fnmatch import translate
from hashlib import new
from posixpath import splitdrive
from sys import maxunicode
from threading import main_thread
from time import time
from tkinter import mainloop
from typing import Text
from unicodedata import numeric
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
from requests import get

from ast import If, Num
from asyncio.windows_events import NULL
from contextlib import nullcontext
from queue import Empty
import sys
from tkinter import Widget
from tokenize import Number
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector as con
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import LoginUI
import signUp


class LoginApp(QDialog):
      def __init__(self):
          super(LoginApp,self).__init__()
          loadUi("Login1.ui",self)
          self.l1.clicked.connect(self.login)
          self.signIn.clicked.connect(self.show_reg)

      def login(self):
          un = self.u1.text()
          pw = self.p1.text()
          db = con.connect(host="localhost",user="root",password="Harshal",database="userlist",port="3307")
          cursor = db.cursor()  
          cursor.execute("select * from users where username = '"+ un +"' and password = '"+ pw +"' ")
          result = cursor.fetchone()
          if result:
              QMessageBox.information(self,"Login Output","login seuccessfully!")
              p = LoginApp()
              p.close()
          else:
              QMessageBox.information(self,"Login Output","Invalid User.. Register for new user ")
        
      def show_reg(self):
          Widget.setCurrentIndex(1)

          

class RegAPP(QDialog):
      def __init__(self):
          super(RegAPP,self).__init__()
          loadUi("SIGNup1.ui",self)   
          self.pushButton.clicked.connect(self.reg)
          self.pushButton_2.clicked.connect(self.show_login) 
      def reg(self):
          un = self.user.text()
          pw = self.passw.text()
          em = self.email.text()
          pnum = self.pnum.text()
        
          db = con.connect(host="localhost",user="root",password="Harshal",database="userlist",port="3307")
          cursor= db.cursor()
          cursor.execute("select * from users where username = '"+ un +"' and password = '"+ pw +"'")
          result= cursor.fetchone()
        
          
          if result:
              QMessageBox.information(self,"Login form","The user already registered, try another username!!")
          else:
               if (un and pw and em and pnum):
                   if(pnum.isdigit()):
                    cursor.execute("insert into users values ('"+ un +"','"+ pw +"','"+ em +"','"+ pnum +"')")
                    db.commit()
                    QMessageBox.information(self,"Login form","The user registered successfully ")
                    p1 = LoginApp()
                    p1.show()
                    
                    
                   else:
                        QMessageBox.information(self,"invalid","Please enter valid mobile number ")
                       
               else:
                   QMessageBox.information(self,"invalid","please enter valid detalis ")



      def show_login(self):
          Widget.setCurrentIndex(0)

app = QApplication(sys.argv)
Widget = QtWidgets.QStackedWidget()

loginform = LoginUI.Ui_Form()
loginform1 = LoginApp() 
loginform.setupUi(Widget)
Widget.addWidget(loginform1)

registrationForm = RegAPP()
Widget.addWidget(registrationForm)

# registrationForm = LoginUI.Ui_Form1()
# reg1 = RegAPP()
# registrationForm.setupUi(Widget)
# Widget.addWidget(reg1)

Widget.setCurrentIndex(0)
Widget.show()
Widget.setFixedWidth(1141)
Widget.setFixedHeight(756)
app.exec_()







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)


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

    except:
        print("Say that again please....")
        return "None"
    return query


def Temp ():
    search = "temperature in Mumbai"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    speak(f"The Temperature Outside Is {temperature} ")
    print(f"The Temperature Outside Is {temperature} ")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_lation = location.latitude , location.longitude

    location = location.raw['address']

    target = {'city' : location.get('city',''),
               'state' : location.get('state',''),
                'country' : location.get('country','')}
    
    current_loca = geocoder.ip('me')
    current_latlon = current_loca.latlng
    
    distance = str(great_circle(current_latlon,target_lation))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    speak(target)
    speak(f"Sir,{Place} is {distance} Kilometer away from your location - ")

    webbrowser.open(url=Url_Place)

def My_loca():
    op = 'https://www.google.com/maps/place/Saraswati+College+of+Engineering,+Kharghar/@19.0400135,73.0587091,694m/data=!3m1!1e3!4m5!3m4!1s0x3be7c23c0d76935f:0xdc48e289b198623a!8m2!3d19.0403902!4d73.059923'
    webbrowser.open(op)
    ip = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/'+ ip + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f"sir, Your are now in {state, country}")





if __name__== "__main__":
    wishMe()
    while True:
            query = takeCommand().lower()

            if "hello" in query:
                speak('Hello sir')
            
            elif "how are you" in query:
                speak('I am fine sir, what about you')

            elif "fine" in query:
                speak("That's great sir")

            elif "open notepad" in query:
                path = "C:\\windows\\system32\\notepad.exe"
                os.startfile(path)
            
            elif "open command prompt" in query:
                os.system("start cmd")

            elif "ip address" in query:
                ip = get("https://api.ipify.org").text
                print("Your IP address is ",ip)
                speak(f"yout IP address is {ip}")
            

            elif 'wikipedia' in query:
                speak("sir, what should I search on wikipedia")
                query = takeCommand().lower()
                results = wikipedia.summary(f"{query}", sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("sir, what should I search on youtube")
                yt =takeCommand().lower() 
                webbrowser.open(f"https://www.youtube.com/results?search_query={yt}")

            elif 'open google' in query:
                speak("sir, what should I search on google")
                cm = takeCommand().lower()
                webbrowser.open(f"https://www.google.com/search?q={cm}")
              
            elif "close notepad" in query:
                speak('okay sir, closing notepad')
                os.system("taskkill /f /im notepad.exe")
            
            elif "close youtube" in query:
                speak("okay sir, closeing youtube")
                os.system("TASKKILL /F /im msedge.exe")

            elif "close map" in query:
                speak("Okay sir, closing googlemap")
                os.system("TASKKILL /F /im msedge.exe")

            elif "set alarm" in query:
                a = int(datetime.datetime.now().hour)
                if a ==22:
                    music_dir = 'C:\\Users\\harsh\\Desktop\\Virtual Assistant'
                    songs =os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))

            elif "where I am" in query or "where we are" in query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                    
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass
                
            elif  "location" in query:
                My_loca()
        
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
                        from features import YoutubeSearch
                        YoutubeSearch(query)
        
            elif 'how to' in query:
                speak("Getting Data From The Internet!")
                op = query.replace("jarvis","")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

        

     

           



     
    

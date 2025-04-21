'''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                                     $
$                     (N.O.V.A)                       $
$                                                     $
$           Version: 3.2.5                            $
$           Started On: 30th Oct, 2024                $
$           Created By:  Rajeev kumar                 $
$           Github ID: rajeevvv018                    $
$                                                     $                                                                                                                                                                                            
$                                                     $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess
import pyjokes
import numpy as np
import cv2
#import json - some discord fun shits
from urllib.request import urlopen
import ctypes
import winshell
import time
import smtplib
import requests
#import urllib.request
#import re
import pyautogui
#import datealm  #separate file
import psutil
import pyperclip
#import clipboard
import pyowm
#import instadownloader #required for instaloader.
from instaloader import *
from time import sleep
from PIL import ImageGrab
from win32api import GetSystemMetrics
from pywikihow import search_wikihow
#from lsHotword import ls
from googletrans import Translator
from pytube import YouTube
from win10toast import *
from win11toast import *
import wolframalpha

#=============================================================================================================
#wolframalpha setup
print("Before anything else, logging in to wolframalpha for mathematical operations")
try:
    app = wolframalpha.Client("VPKGJW-QW38YGT94R") #VPKGJW-QW38YGT94R Q539P8-JQHRU4WLJU
    print("Wolframalpha login successful")
except Exception:
    print('some feature are not working')

#===================================== List of defined values that i'll use ============================================
test = toast()


emails = {
    "admin": "rajeevkumar620630@gmail.com",
}

city="New Delhi" # for weather

months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
dates = {1:'First',2:'Second',3:'Third',4:'Fourth',5:'Fifth',6:'Sixth',7:'Seventh',8:'Eighth',9:'Ninth',10:'Tenth',11:'Eleventh',12:'Twelfth',13:'Thirteenth',14:'Fourteenth',15:'Fifteenth',16:'Sixteenth',17:'Seventeenth',18:'Eighteenth',19:'Ninteenth',20:'Twentieth',21:'Twenty First',22:'Twenty Second',23:'Twenty Third',24:'Twenty Fourth',25:'Twenty Fifth',26:'Twenty Sixth',27:'Twenty Seventh',28:'Twenty Eighth',29:'Twenty Ninth',30:'Thirty',31:'Thirty First'}

UnlockCounter = 0 # for 3 password trials
#===============================================================================================================

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  #print(voices[0].id)    #voice0=david, voice1=mark, voice2=eva, voice3=zira
engine.setProperty('rate', 193)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    ctime = time.strftime("%I:%M %p")

    if hour>=5 and hour<12:
        speak(f"Good Morning Sir, its {ctime}")
    elif hour>=12 and hour<16:
        speak(f"Good AfterNoon Sir, its {ctime}")
    elif hour>=16 and hour<20:
        speak(f"Good Evening sir, its {ctime}")
    else:
        speak(f"Good Night Sir, its {ctime}")

    work =("please tell me how may i help you sir")
    speak("I am your Personal Assistant")
    speak(work)

unheard_responces = ["\033[31mYour last command could\'t be heard...\033[0m", "\033[31mPlease say that again?\033[0m", "\033[31mPlease speak louder!\033[0m", "\033[31mSpeak clearly sir!\033[0m", "\033[31mPardon?\033[0m"]
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 4000
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception:
        RandomResponce = unheard_responces[random.randint(0, len(unheard_responces)-1)]
        print(RandomResponce)
        #speak(RandomResponce)
        return "None"

    query = query.lower() #for handling tasks
    return query

# ======================= Functions to be used... ==========================
def voice_changer():
    speak("Please enter your favourable voice id sir.")
    x = int(input("Enter your favourable voice id sir: "))
    speak(f"Changing to id {x}")
    engine.setProperty('voice', voices[x].id)
    speak("Transition successful sir, its my new voice. hope you liked it.")

def rate_control():
    speak("sir i prefer to take value as input from you, so please do it...")
    speak("and sir make sure you give value in between 180 to 200")
    x = int(input("Enter the speech rate value: "))
    engine.setProperty('rate', x)
    speak("alright, this is the new speech speed sir.")

def click():
    pyautogui.click()

def battery():
    speak("Just wait a second sir, getting battery informations..")
    battery = psutil.sensors_battery()
    battery_percentage = battery.percent
    plugged = battery.power_plugged
    speak(f"Sir, its {battery_percentage} percent available.")
    if plugged:
        speak("and the device is getting charged...")
    if not plugged:
        if battery_percentage >=75:
            speak("we have enough power to work more sir.")
        elif battery_percentage >=40 and battery_percentage<=75:
           speak("you should connect charger sir")
        elif battery_percentage>=15 and battery_percentage<=39:
            speak("sir it feels like i don\'t have enough power, please connect charger")
        elif battery_percentage<=15:
            speak("sir please connect charger as soon as possible, am on my last breath..")

def minimize_all():
    speak("Minimizing all windows sir.")
    try:
        os.system('''powershell -command "(new-object -com shell.application).minimizeall()"''')
        speak("all windows minimized")
    except Exception as e:
        speak("well there are no windows to minimize")

def shutDown():
    minimize_all()
    speak('Are you sure that you wan\'t me to shutdown this pc?')
    query = takeCommand()
    if 'yes' or 'shutdown' or 'do it' in query:
 
        speak('Alright starting the shutdown protocol for your pc sir')
        speak('Initializing shutdown protocol ')
        click()
        pyautogui.keyDown('alt')
        pyautogui.press('f4')
        pyautogui.keyUp('alt')
        pyautogui.press('enter')
    elif 'no' or 'nah' or 'na' or 'don\'t' in query:
        speak('Okay, nevermind.')

def restart():
    minimize_all()
    speak('Are you sure that you wan\'t me to restart this pc?')
    query = takeCommand()
    if 'yeah' or 'yes' or 'restart' or 'do it' in query:

        speak("Alright initiating the restart protocol for your pc sir")
        speak("Restarting your computer")
        click()
        pyautogui.keyDown('alt')
        pyautogui.press('f4')
        pyautogui.keyUp('alt')
        sleep(3)
        pyautogui.press('r')
        pyautogui.press('enter')
    
    elif 'no' or 'nah' or 'na' or 'don\'t' or 'dont' in query:
        speak('Okay, Nevermind') 

def Sleep():
    minimize_all()
    speak('Alright starting sleep protocol for your pc sir')
    speak("Initializing sleep mode")
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    sleep(2)
    #check these presses according to your pc.
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('enter')

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    xx=(dates[date],months[month],year)
    speak('the current date is')
    speak(xx)
    
def screenshot():

    date = datetime.datetime.today()
    x = str(date).replace(":", "-") + "ssByEVA.png"
    pyautogui.screenshot(f"E:\\Eva\\screenshots_by_eva\\{x}")
    speak("screenshot saved in Eva's root folder sir.")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at" +usage +"Percentage")

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("lisaworkspacetesting@gmail.com", "nextgen@101")
    server.sendmail("lisaworkspacetesting@gmail.com", to, content)
    server.close()

def languagetranslator():
    try:
        trans=Translator()
        speak("Say the language to translate in")
        language=takeCommand().replace(" ","")
        speak("What to translate")
        content=takeCommand()
        t=trans.translate(text=content,dest=language)
        speak(f"{t.origin} in {t.dest} is{t.text}")
    except:
        speak("Unable to translate")

def weather_info():
    owm=pyowm.OWM('eece000de5e319b3c94c04b2d1bc9b15')
    location= "New Delhi" #owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    humidity=weather.get_humidity()
    date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
    current_temp=temp['temp']
    maximum_temp=temp['temp_max']
    min_temp=temp['temp_min']
    speak(f'The current temperature on {city} is {current_temp} degree celsius ')
    speak(f'The estimated maximum temperature for today {date} on {city} is {maximum_temp} degree celcius')
    speak(f'The estimated minimum temperature for today {date} on {city} is {min_temp} degree celcius')
    speak(f'The air is {humidity}% humid today')

def convert():
    trans=Translator()
    speak("Say the language to translate in")
    language=takeCommand().replace(" ","")
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")
    tobespoken=pyperclip.paste()
    content=tobespoken
    t=trans.translate(text=content,dest=language)
    speak(f"{t.origin} in {t.dest} is{t.text}")

def check_voice():
    speak("Alright, these are the available voices in your pc sir.")
    for voice in voices:
    # to get the info. about various voices in our PC 
        print("Voice:")
        print("ID: %s" %voice.id)
        print("Name: %s" %voice.name)
    speak("Count from 0 to n-1 to know their ids sir.")

#Integration of RecorderX with E.V.A (5th Nov, 2021)
def recorderx():
    speak("Just a minute sir ")
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    #time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    #file_name = f'{time_stamp}.mp4'
    speak("Please enter the name of outfile file with format in console sir")
    file_name = input("\nenter the output name with format: ") 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(file_name, fourcc, 8.5, (width, height)) 
    #fps = 8.5 is stable output; 20.0 = 3x speed
    #higher the fps = faster the video speed
    speak("Alright, starting Recorder X")
    speak("Don\'t forget to press Q to stop recording sir")


    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('RecorderX - Screen Recorder', img_final)

        # cv2.imshow('webcam', frame)

        output.write(img_final)
        if cv2.waitKey(10) == ord('q'): # press q to stop recording
            speak("Alright, Recording has been stopped. ")
            break

#to download profile pic + all posts (6th Nov, 2021)
#Ability to downloads highlights now. (8th Oct, 2022)
def download_insta_profile():
    speak("Okay, please enter your login details sir")
    username = input("Enter your username sir: ")
    password = input("Enter your password sir: ")
    speak("Thank you, logging in with given details")
    mod = instaloader.Instaloader()
    mod.login(user=username,passwd=password)
    speak("successfully logged in")

    speak("Now please enter the target username manually sir")
    name = input("Enter target username: ")
    speak("Sir you want to download whole profile or just profile pic?")
    query = takeCommand()
    if 'profile pic' in query or 'just' in query:
        speak(f"Alright sir, downloading profile pic of {name}")
        mod.download_profile(name, profile_pic_only=True)

    elif 'hightlights' in query or 'high' in query:
        mod.download_profile(name)
        speak("Alright sir, downloading whole profile of {name} with available highlights...")
        profilehighlights = Profile.from_username(mod.context, username=name)  
        try:
            for highlight in mod.get_highlights(user=profilehighlights):
                # highlight is a Highlight object
                for item in highlight.get_items():
                    # item is a StoryItem object
                    mod.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
            # speak(f"Successfully downloaded the profile of {name} with highlights and saved it in folder named as {name}")
        
        except Exception as e:
            speak("Sir am unable to download the profile with highlights, please check the error summery in terminal")
            print("\n\n",e,"\n\n")

    else:
        speak(f"Alright sir, downloading whole profile of {name}")
        mod.download_profile(name)
    speak(f"successfully downloaded and saved in our main folder named as {name}.")

#to download YT Videos
def YtDownloader():
    speak("Alright sir, please copy the video link and paste it in console.")
    linkk = input("Enter link: ")
    speak("Link received.")
    url = YouTube(linkk)
    speak("Sir before downloading please give this video a suitable name")
    name= input("Please chose a name for this file: ")
    speak("Hmm it seems like a good title for the video     ")
    speak("Chosing the best resolution available for this video")
    
    try:
        video = url.streams.get_highest_resolution()
        speak("Found it, downloading your video. sorry for the delay sir")


        video.download('E:\\Eva\\YT Downloads\\',filename=f'{name}.mp4')
        speak("Successfully downloaded into your given folder sir.")

        print("\n\nVideo has been Downloaded.\n\n")
    except Exception as e:
        speak("Sir am unable to download this video, please check the internet connection")
        speak("Sir i gave the error summery in console in case you need it")
        print("Error occured:-\n", e)

def music():
    speak("Okay sir, playing a song for you")
    music_dir = 'F:\\$ongs\\check'
    songs = os.listdir(music_dir)
    rd = random.randint(0,4)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[rd]))

'''

Upgrade these fuckig toasts to Win-11:

1. Add image & icon
2. Make usage of buttons for fkin YT
3. Make use of progress-bar for custom YT-Downloader

'''
def activation_notif():
    n = ToastNotifier()
    #n.show_toast("Enhanced Voice Assistant", "E.V.A is now activated and ready to work on your command", duration=20)
    toast('Jhatu1', 'Hello from Python', icon='https://unsplash.it/64?image=669')



def deactivation_notif():
    n = ToastNotifier()
    n.show_toast("Chal ja bsdkkkk", "E.V.A is now deactivated and unable to work until launched again", duration=20)

def sleep_notif():
    n = ToastNotifier()
    n.show_toast("Enhanced Voice Assistant", "E.V.A is now sleeping in background", duration=20)

#================================= List of tasks hardcoded ======================================

def TaskExecution():
    wishMe()
    
    while True:
       query = takeCommand()
       # Logic for executing tasks based on query
       if 'wikipedia' in query:
           speak('Searching Wikipedia....')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
           speak("Anything else sir?")

       elif 'details about' in query:
           speak('Searching Wikipedia....')
           query = query.replace("details about", "")
           results1 = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results1)
           speak(results1)
           speak("Anything else sir?")

       elif 'tell me about' in query:
           speak('Searching Wikipedia....')
           query = query.replace("tell me about", "")
           results2 = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results2)
           speak(results2)
           speak("Anything else sir?")

       elif 'who is' in query:
           speak('Searching Wikipedia....')
           query = query.replace("who is", "")
           results3 = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results3)
           speak(results3)
           speak("Anything else sir?")

       elif 'hello' in query:
           speak("Hellow sir, is there anything i can help you with?")

       elif 'eva' in query or 'jarvis' in query:
           speak("Yes sir")

       elif 'doing' in query:
           speak("Just waiting for your orders to do something sir")

       elif 'where is' in query or 'lisa where is' in query:
           query = query.replace("where is","")
           query = query.replace("lisa where is","")
           location = query
           speak('Just a second sir, showing you were is' +location)
           url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
           webbrowser.get().open(url)
        
        # To open Webcam
       elif "open camera" in query:
           cap = cv2.VideoCapture(0)
           while True:
               ret, img = cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(0)
               if k==27:
                   break
           cap.release()
           cv2.destroyAllWindows()
            
       elif 'check my internet connection' in query or 'am I connected to internet' in query:
           hostname="google.co.in"
           response=os.system("ping -c 1" +hostname)
           if response==0:
               speak("Sir Internet is disconnected")
           else:
               speak("sir you are connected to internet")

       elif 'next window' in query or 'switch back' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           time.sleep(1)
           pyautogui.keyUp("alt")
           speak("window switched")

       elif 'previous window' in query or 'last window' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           time.sleep(1)
           pyautogui.keyUp("alt")
           speak("anything else sir?")

       elif 'switch window' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           speak("which one")
           query = takeCommand()
           if 'next' in query:
               pyautogui.press("right")
               pyautogui.keyUp("alt")
               speak('window switched')
           if "don't switch" in query or 'go back' in query:
               pyautogui.press("left")
               pyautogui.keyUp("alt")
               speak("window switched")

       elif 'close current window' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("f4")
           pyautogui.keyUp("alt")

       elif 'minimise this window' in query or 'minimize current window' in query or 'minimize this' in query or 'minimise current window' in query:
           pyautogui.keyDown("win")
           pyautogui.press("down")
           pyautogui.keyUp("win")
           speak("Current window has been minimized")

       elif 'minimize all windows' in query or 'minimise all' in query or 'minimize all' in query or 'minimize all' in query:
           minimize_all()

       elif 'maximize window' in query or 'fullscreen' in query or 'maximise window' in query or 'maximise' in query:
           try:
               pyautogui.keyDown("win")
               pyautogui.press("up")
               pyautogui.keyUp("win")
               speak("This window is now on fullscreen")
           except Exception as e:
               speak("No windows to maximize")

       elif 'type' in query:
           query = query.split(" ")
           lenght=len(query)
           term=query[1:lenght]
           pyautogui.typewrite(' '.join(term))

       elif 'date today' in query:
           date()

       elif 'time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is {strTime}")

       elif 'translate' in query:
           languagetranslator()
           
       elif 'convert selected' in query:
           convert()

       elif 'search' in query:
            query = query.replace("search", "")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get().open(url)
            speak("Here is what I got form search result" + query)

       elif 'open youtube' in query:
           speak('Ok sir Opening Youtube')
           webbrowser.open("https://youtube.com/")
           speak("Sir what would u like to Watch on youtube?")
           query = takeCommand()
           if 'search' in query:
               query = query.replace("search", "")
               url = f"https://www.youtube.com/results?search_query={query}"
               webbrowser.open(url)
               speak("I've searched for" +query +"in youtube")
           if 'will do it myself' in query or 'leave it' in query or 'no':
               speak("As You like sir!")

       elif 'recently closed tabs' in query or 'recently closed tabs' in query:
           try:
               pyautogui.keyDown("ctrl")
               pyautogui.keyDown("shift")
               pyautogui.press("T")
               pyautogui.keyUp("ctrl")
               pyautogui.keyUp("shift")
               speak("Recently closed tabs has been opened")
           except Exception as e:
               speak("No recent tabs found")

       elif 'open chrome' in query:
           try:
               speak('opening chrome')
               codepath = "chrome.exe"
               os.startfile(codepath)
           except Exception as e:
               speak("Chrome Not found")

       elif 'close chrome' in query:
           os.system("taskkill /f /im chrome.exe")
           speak('chrome has been closed')

       elif 'open spotify' in query or 'play music on spotify' in query:
           speak ('As u like sir ')
           codepath = "spotify.exe"
           os.startfile(codepath)

       elif 'close spotify' in query:
           os.system("taskkill /f /im spotify.exe")
           speak('spotify closed')
           
       elif 'play music' in query:
           music()

       elif 'some upgrade' in query or 'open code' in query or 'want to update you' in query or 'Open visual studio' in query:
           try:
               codepath = "Code.exe"
               os.startfile(codepath)
               speak('opening')
           except Exception as e:
               speak("Visual code not found in your computer")

       elif 'close code' in query or 'close visual studio' in query:
           os.system("taskkill /f /im Code.exe")
           speak('code has been closed')

       elif 'open premiere pro' in query:
           try:               
               codepath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe" 
               os.startfile(codepath)
               speak('opening Premiere pro')
           except Exception as e:
               speak('Sir Premiere pro not found in your computer')

       elif 'joke' in query or 'make me laugh' in query:
            speak(pyjokes.get_joke())

       elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Priyanshu Jindal, here\'s his github username")
            speak("jindalpriyanshu101")

       elif 'remember' in query:
           speak("what should I remember?")
           query = takeCommand()
           speak("you said me to remember that" +query)
           remember = open('query.txt','w')
           remember.write(query)
           remember.close()

       elif 'do you know anything' in query:
           try:
               remember = open('query.txt','r')
               speak("you said me to remember that" +remember.read())
           except Exception as e:
               speak("sir you didn't said anything to remember")
    
       elif 'jarvis make a note' in query or 'write down' in query or 'note' in query or 'make a note' in query or 'jarvis write down' in query or 'jarvis note' in query or 'eva make a note' in query or 'eva write down' in query or 'eva note' in query:
           query = query.replace("make a note", "")
           note(query)
           speak("I've made a note of that. Anything else?")
           query = takeCommand()
           if "no" in query:
               speak('ok sir')
           if "yes" in query:
               speak('Go on sir')

       elif 'calculate' in query:     
            app_id = "VPKGJW-QW38YGT94R" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

       elif 'weather of' in query:
            '''api_key="b5fa1df8dd4a28b83eb0d1f7fc54ed30"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            query = query.replace("weather of", "")
            city_name = query
            speak("weather of" +city_name +"is")
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))'''
            weather_info()

       elif 'email' in query:
           try:
               speak("Whom U would like to send email")
               name = takeCommand()
               to = emails[name]
               speak("What should i say?")
               content = takeCommand()
               speak("Confirm, yes or no")
               mailconfig = takeCommand()
               flag = 0
               while flag != 1:
                   if "yes" in mailconfig:
                       sendEmail(to, content)
                       speak("Email has been sent succesfully")
                       flag = 1
                   elif "no" in mailconfig:
                       speak("Ok sir request has been cancelled")
                       break
                   else:
                       speak("Unable to confirm, please say again")
                       break
           except Exception as e:
               speak("Could not send email")

       elif 'lock window' in query or 'lock the system' in query:
           try:
               speak("locking the device")
               ctypes.windll.user32.LockWorkStation()
           except Exception as e:
               speak("Sir windows is already locked")

       elif 'empty recycle bin' in query or 'clean recycle bin' in query:
           try:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin is cleaned")
           except Exception as e:
               speak("Recycle bin is already cleaned")

       elif 'cpu usage' in query or 'cpu uses' in query or 'check my cpu' in query:
           cpu()

       elif 'alarm' in query:
           #datealm.alarm(query)
           print("do something")

       elif 'take a screenshot' in query or 'take screenshot' in query or 'screenshot' in query:
           screenshot()

       elif 'start recording' in query or 'recording' in query or 'record' in query:
           recorderx()
           cv2.destroyAllWindows()

       elif 'voice' in query:
           check_voice()

       elif 'change voice' in query or 'change your voice' in query:
           check_voice()
           voice_changer()

       elif 'speech' in query or 'rate' in query or 'speed' in query:
           rate_control()

       elif 'set pc to sleep' in query:
           Sleep()

       elif 'restart the pc' in query:
           restart()
        
       elif 'shutdown this pc' in query or 'start shutdown protocol' in query:
           shutDown()

       elif 'battery' in query:
           battery()

       elif 'profile' in query or 'instagram' in query:
           speak("Okay sir before opening insta profile, please write the username")
           name = input("Enter target username: ")
           speak("alright, opening this profile")
           webbrowser.open(f"www.instagram.com/{name}")
           time.sleep(3)
           speak("sir, would you like to download this whole profile?")
           query = takeCommand()
           if 'yes' in query or 'do it' in query or 'why not' in query:
               download_insta_profile()
           else:
               speak("Nevermind.")


       elif 'how are you' in query or 'how are you doing' in query:
           speak("am fine sir, what about you?")
           query = takeCommand()
           if 'am also good' in query or 'am also fine' in query or 'healthy' in query or 'fine' in query:
               speak("wow, felt good to hear sir.")

           elif 'not fine' in query or 'not well' in query or 'not good' in query or 'felling low' in query or 'not in mood' in query:
               speak("sad to hear that sir, how may I change your mood, May i play music for You?")
               query = takeCommand()
               if 'ok' in query or 'sure' in query or 'hmm' in query or 'alright' in query or 'yeah' in query or 'play music' in query:
                   speak('ok sir playing music for you')
                   music_dir = 'F:\\$ongs'
                   songs = os.listdir(music_dir)
                   rd = random.choice(songs)
                   print(songs)
                   for songs in songs:
                       if songs.endswith('.mp3'):
                           os.startfile(os.path.join(music_dir, songs))
               elif "no" in query or "it's ok" in query or "don't play" in query or 'nope' in query:
                   speak("Ok sir as You like!")


       elif 'sleep' in query or 'sleep now' in query or 'take a break' in query or 'rest now' in query or 'you can sleep now' in query or "keep quite" in query or 'rest' in query:
           speak("Okay sir, don\'t forget to call me again if required.")
           speak("Sleep mode activated...")
           sleep_notif()
           break #for exiting command loop, wake up or shutdown now...

if __name__== "__main__":
    
    speak("Hey there, My access is password protected to restrict any unknown guy to use me. ")
    speak("If you're verified person then you probably be having the password, please write it down.")
    
    while UnlockCounter<3:
        password = input("Enter the password: ")
        if password=="test":
            speak("Welcome back sir, initiating the start protocol")
            UnlockCounter=3

        else:
            speak("You dumbass!! get the fuck out of here, don't do hit and trial to get my access")
            speak("Don\'t you dare to open me back again until you have the password.")
            UnlockCounter+=1
            print("You have", 3-UnlockCounter, "attempt(s) remaining")

    speak("sir before initiating the workspace, you wanna continue with Eva or Jarvis")
    query = takeCommand()

    if 'jarvis' in query or 'service' in query or 'javed' in query:
        engine.setProperty('voice', voices[1].id)
        speak("Jarvis at your service sir.")
        speak("Initializing the workspace....")
        speak("Successfully initiated, waiting for your orders to start... ")
 
    elif 'eva' in query or 'shiva' in query:
        engine.setProperty('voice', voices[2].id)
        speak("Eva at your service sir.")
        speak("Initializing the workspace....")
        speak("Successfully initiated, waiting for your orders to start... ")
    else:
        speak("wrong input provided, proceeding with default voice")
        speak("Initializing the workspace....")
        speak("Successfully initiated, waiting for your orders to start... ")
 
 
    while True:
        
        permission = takeCommand()

        if ('wake up' in permission) or ('start' in permission) or ('work' in permission) or ('working' in permission) or ('workspace' in permission):
            activation_notif()
            TaskExecution()
        
        elif ('goodbye' in permission) or ('shutdown' in permission) or ('shut' in permission) or ('down' in permission):
           speak("Do You want me to shutdown sir")
           query = takeCommand()

           if ('no' in query) or ('cancel' in query) or ('nah' in query):
               speak("Process cancelled")

           if ('yes' in query) or ('yep' in query) or ('shutdown' in query) or ('down' in query) or ('shut' in query):
                
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    speak("Alright, Have a nice day ahead sir!")
                    speak("Shutting down...")
                    deactivation_notif()
                    exit()

                elif hour>=18 and hour<24:
                    speak("Ok, good night sir")
                    speak("Shutting down...")
                    deactivation_notif()
                    exit()

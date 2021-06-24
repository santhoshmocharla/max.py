
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import random
import webbrowser
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        talk('good morning sir')
    elif hour>=13 and hour<=18:
        talk('good after noon sir')
    else:
        talk('good evening sir')

if __name__ == "__main__":
    wish()
def take_command():
    try:
        with sr.Microphone() as source:
            print('MAX IS HERE')
            print('listening..........')
            talk('max is here to hear')
            voice = listener.listen(source,timeout=1,phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'max' in command:
                command = command.replace('max','')
                print(command)
    except:
        pass
    return command
def run_max():
    command = take_command()
    print(command)
    if 'on youtube' in command:
        video = command.replace('play','')
        talk('playing' + video)
        pywhatkit.playonyt(video)
    elif 'open notepad' in command:
        talk('opening notepad sir')
        npath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(npath)
    elif 'open browser' in command:
        talk('opening browser sir')
        bpath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(bpath)
    elif 'open command prompt' in command:
        talk('opening command prompt sir')
        os.system("start cmd")
    elif 'open youtube' in command:
        talk('opening youtube sir')
        webbrowser.open("www.youtube.com")
    elif 'open whatsapp' in command:
        talk('opening whatsapp sir')
        webbrowser.open("https://web.whatsapp.com/")
    elif 'open facebook' in command:
        talk('opening facebook sir')
        webbrowser.open("www.facebook.com")
    elif 'open myntra' in command:
        talk('opening myntra sir')
        webbrowser.open("www.myntra.com")
    elif 'open amazon' in command:
        talk('opening amazon sir')
        webbrowser.open("www.amazon.in")
    elif 'open flipkart' in command:
        talk('opening flipkart sir')
        webbrowser.open("www.flipkart.com")
    elif 'search on google' in command:
        talk('what should i search on google sir')
        cm = take_command().lower()
        webbrowser.open(f"{cm}")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('the current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who was' in command:
        person = command.replace('who was','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who' in command:
        person = command.replace('who','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        about = command.replace('what is','')
        info = wikipedia.summary(about, 2)
        talk('searching on wikipedia sir')
        print(info)
        talk(info)
    elif 'are you single' in command:
        print('i am proud to be single like you sir')
        talk('i am proud to be single like you sir')
    elif 'play some music' in command:
        talk('playing music sir')
        music_dir = "C:\\Users\\Mocharla Santhosh\\Music\\music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))
    elif 'play music' in command:
        talk('playing music sir')
        music_dir = "C:\\Users\\Mocharla Santhosh\\Music\\music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))
    elif 'nothing more' in command:
        talk('shutting down sir, have a great day')
        sys.exit()
    else:
        talk('i can not get you sir can you come again.')
while True:
    run_max()
#just testing
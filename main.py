import datetime
import os
import random
import smtplib
import webbrowser
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init()
voices =engine.getProperty('voices')
print(voices[14].id)
engine.setProperty('voice',voices[14].id)

dict={
    'santosh':'santoshkrm567@gmail.com',
    'ramesh':'holamr09@gmail.com'

}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good night")
    speak("I am jarvis How can i help u")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 4
        audio = r.listen(source, timeout=3, phrase_time_limit=3)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("itachilaw123@gmail.com",'********')
    server.sendmail('itachilaw123@gmail.com',to,content)
    server.close()


if __name__=="__main__":
    wishme()
    while True:
        print("Sir do u have any command press y or n")
        speak("Sir do u have any command press yes or no")
        cmd=(input())
        if cmd=='y':
            query=takecommand().lower()

            #Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak("scanning wikipedia...")
                query =  query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif "open github" in query:
                webbrowser.open("github.com")
            elif "open facebook" in query:
                webbrowser.open("facebook.com")

            elif 'open youtube' in query:
                webbrowser.open('youtube.com')

            elif 'open google' in query:
                webbrowser.open('google.com')

            elif 'music' in query:
                music_dir = "/home/san/Music"
                songs = os.listdir(music_dir)
                a = random.randint(0, len(songs)-1)
                print(songs[a])
                playsound(f'{music_dir}/{songs[a]}')

            elif 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")
            elif 'send email' in query:
                try:
                    speak("whom to send email")
                    nam=takecommand().lower()
                    speak("What should i say")
                    content = takecommand()
                    to = dict[nam]
                    sendEmail(to,content)
                    speak("Email sent!!")
                except Exception as e:
                    print(e)
                    speak("Sorry email cannot be sent")

        else:
            pass
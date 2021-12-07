from math import exp
import pyttsx3
import random
import wikipedia
import pyjokes
import time
import webbrowser
import datetime
import os
from pyttsx3 import engine
import speech_recognition as sr

converter = pyttsx3.init()
def command():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Nora : Listning...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"master: {query}")
            return query
        except:
            print("Try Again")   
# print(command())
def speak(audio):
    voice_id = "com.apple.speech.synthesis.voice.samantha"
    converter.setProperty('voice',voice_id)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour <12:
        speak("Hello,Good Morning")
    elif hour >=12 and hour <18:
        speak("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
wishMe()
while True:
    query = command().lower()
    if 'name' in query:
        speak("Hi! Shriyansh my name is Nora ")
    elif 'are you single' in query:
        answer = ['I am in relationship machine', 'I am married in idea of helping people']
        speak(random.choice(answer))
    elif 'jokes' in query:
        speak(pyjokes.get_joke())
    elif 'hate' in query:
        speak("Hmmmmmmmm........ i am having troble answering that")
    elif 'love' in query:
        speak("I love to talk to you")
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"It's {time} master")
    elif 'who is' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    elif 'youtube' in query:
        webbrowser.open_new_tab("https://www.youtube.com/")
        speak("Youtube is open now")
        time.sleep(5)
    elif 'open Google' in query:
        webbrowser.open_new_tab("https://www.google.com")
    elif 'bye' or 'good bye' in query:
        speak('Bye bye! Have a good day')
        break
    else:
        speak('Come again')

#uncomment the code if you want to know the voices id in you system

# voices = converter.getProperty('voices')
# for voice in voices:
# 	# to get the info. about various voices in our PC
#     if voice.gender == 'VoiceGenderFemale':
#         print("Voice:")
#         print("ID: %s" %voice.id)
#         print("Name: %s" %voice.name)
#         print("Age: %s" %voice.age)
#         print("Gender: %s" %voice.gender)
#         print("Languages Known: %s" %voice.languages)






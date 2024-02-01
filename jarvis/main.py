import speech_recognition as sr
import  pyttsx3
import pywhatkit
import datetime
import  wikipedia
import openai


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'humaira' in command:
                command  = command.replace('humaira','')

    except:
        pass

    return  command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        pywhatkit.playonyt(song)
    elif 'wikipedia' in command :
        name = command.replace('wikipedia','')
        wiki= wikipedia.summary(name,sentences=3)
        print(wiki)
        talk(wiki)
    elif 'who are you' in command:
        name = 'i am alexa .  your personal assistant '
        talk(name)

    elif 'software' in command:
        name=' you are also a cute boy, i like software engineer '
        talk(name)






while True:
    run_alexa()



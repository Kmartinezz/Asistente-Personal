import speech_recognition as sr
import sounddevice as sd
import pyttsx3
import datetime
import requests
from googletrans import Translator
import re
import time as t
import wikipedia
import requests
from datetime import datetime
from pprint import pprint
from random import choice
from utils import opening_says, ending_says, starting_says

mic = sd.default.device = 'Micrófono (2- USB Audio Device)'

engine = pyttsx3.init()
engine.setProperty("rate", 143)
voices = engine.getProperty('voices')

engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Saludo():
    hour = datetime.now().hour
    if (hour >= 5 ) and (hour < 12):
        speak("Buenos dias Señor")

    elif (hour >= 12 ) and (hour < 18):
        speak("Buenas tardes Señor")
    
    elif (hour >= 18 ) and (hour < 4):
        speak("Buenas noches Señor")
    
def user_input():
    r = sr.Recognizer()
    with sr.Microphone() as recurso:
        print("Dime Algo ...")
        r.pause_threshold = 1
        audio = r.listen(recurso)

    try:
        query = r.recognize_google(audio, language = "es-es")

        """ if not 'salir' in query:
            print(query)
            speak(choice(starting_says))
        
        else:
            hour = datetime.now().hour
            print(query)
            if (hour >= 5 ) and (hour < 12):
                speak("Que tenga buen dia Señor")

            elif (hour >= 12 ) and (hour < 18):
                speak("Que tenga buena tarde Señor")
            
            elif hour >= 18:
                speak("Que tenga buena noche Señor")
            else:
                speak("Hora no definida")
            exit() """

        if 'yarbiss' in query:
            print(query)
            #speak(choice(starting_says))
            speak(choice(starting_says))
        
        elif 'salir' in query:
            hour = datetime.now().hour
            print(query)
            if (hour >= 5 ) and (hour < 12):
                speak("Que tenga buen dia Señor")

            elif (hour >= 12 ) and (hour < 18):
                speak("Que tenga buena tarde Señor")
            
            elif hour >= 18:
                speak("Que tenga buena noche Señor")

            else:
                speak("Hora no definida")
            exit()

    except Exception as e:
        print(query)
        print(e)
        speak("Disculpe, no he podido entender. ¿Podria repetirlo?")
        query = 'None'
        t.sleep(5)

    return query

if __name__ == '__main__':

    while True:
        query = user_input()

        if 'Hola' in query:
            starting_says()
        else:
            pass
"""import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

 with sr.Microphone() as recurso:
    print("Dime Algo ...")
    r = sr.Recognizer()
    audio = r.listen(recurso)
    
    try:
        texto = r.recognize_google(audio, language = 'es-ES')
        print("Esto es lo que has dicho: {}".format(texto))
    except:
        print("Error, no te entendi") 


from requests.sessions import session
import speech_recognition as sr
import pyttsx3
import datetime
import requests
from googletrans import Translator
import re
import time

translator = Translator()

now = datetime.datetime.now()

escolta = True
ences = True
pregunta = False
actiu = True

r = sr.Recognizer()
mic = sr.Microphone()



engine = pyttsx3.init()
engine.setProperty("rate", 180)
voices = engine.getProperty('voices')

engine.setProperty("voice", voices[1].id)


#PRESENTACION INICIO DEL PROGRAMA

text = "Bienvenido Señor"
engine.say(text)
engine.runAndWait()

with mic as source:
    audio = r.listen(source)
    r.adjust_for_ambient_noise(source, duration = 1)

engine.say("fet, el micròfon està calibrat")
engine.runAndWait()
time.sleep(3)

if escolta == False:
        output = " "


#DETECCION DE JÚLIA

while ences == True:
    if escolta == True:
        with mic as source:
            audio = r.listen(source)

        output = r.recognize_google(audio, language="ca-ES")
        print(output)
        splited = output.split()
        print(splited)

    if output == None:
        pregunta = False
        escolta = True

    if ('Júlia' or 'Julia') in splited:
        pregunta = True
        escolta = False
    if ('Júlia' or 'Julia') not in splited:
        pregunta = False
        escolta = True

    if None in splited:
        pregunta = False
        escolta = True

#DEMANAR HORA ACTUAL (funciona)

if pregunta == True:
    if 'hora' in splited:
        escolta = False
        print(escolta)      
        hora = ("Són les", now.hour, now.minute)
        engine.say(hora)
        engine.runAndWait()
        pregunta = False
        escolta = True"""
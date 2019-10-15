import speech_recognition as sr
import os
r = sr.Recognizer()
with sr.AudioFile("1.wav") as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    f= open('speech.txt', 'w+')
    f.write(s)

    
except Exception as e:
    print("Exception: "+str(e))
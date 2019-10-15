import speech_recognition as sr
import os

files=input("Enter file name/path : (without extension) ")
textFile=input("Enter file name for text : ")
r = sr.Recognizer()

with sr.AudioFile(files + ".wav") as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    f= open(textFile, 'w+')
    f.write(s)

    
except Exception as e:
    print("Exception: "+str(e))

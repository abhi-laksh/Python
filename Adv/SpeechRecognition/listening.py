import speech_recognition as sr
# from speech_recognition  import recognize_api
rec=sr.Recognizer()

with sr.Microphone() as source:
    audio=rec.listen(source)

try:
    print("You ar saying" + rec.recognize_api(audio))
except LookupError:
    print("Could not understand audio")
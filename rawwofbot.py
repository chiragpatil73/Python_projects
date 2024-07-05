import pyttsx3 as px
import speech_recognition as sr
listener=sr.Recognizer()
specker=px.init()
voices=specker.getProperty('voices')
specker.setProperty('voice', voices[1].id)
specker.say("hello ")
specker.runAndWait()


import speech_recognition as sr
import pyttsx3 as px
listener=sr.Recognizer()
specker=px.init()
# voices=specker.gṇetProperty('voices')
# specker.setProerty('voice', voices[0].id)


def talk(text):
    specker.say(text)
    specker.runAndWait()


try:
    with sr.Microphone () as src:
        print("lestening>>>>")
        voice=listener.listen(src)
        command= listener.recognize_google(voice)
        command=command.lower()
        if 'alexa' in command:
              talk(command)
except:
    pass
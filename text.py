import pyttsx3 as pt

text=pt.init()
voices=text.getProperty('voices')
text.setProperty('voice', voices[1].id)
text.say(input("enter your text:"))
text.runAndWait()
text.stop()
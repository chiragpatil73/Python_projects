import gtts as gt
import playsound as ps
text=input("Enter your text:")
sound= gt.gTTS(text,lang="hi",tld='co.in')
sound.save("text.mp3")
ps.playsound("text.mp3")


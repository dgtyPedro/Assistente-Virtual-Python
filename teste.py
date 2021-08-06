#SAVE

import speech_recognition as sr
import os
from gtts import gTTS
from googlesearch import search
import webbrowser

r = sr.Recognizer()
with sr.Microphone() as source:                
    audio = r.listen(source)                   

try:
    print("You said " + r.recognize_google(audio, language = "en-us", show_all=False))    
    output = gTTS(text=r.recognize_google(audio, language = "en-us", show_all=False), lang='en', slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")



except LookupError:                           
    print("Could not understand audio")


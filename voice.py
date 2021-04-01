import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS





def speak(text):
    tts=gTTS(text=text,lang='en')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
 
speak("I am a voice assistant, do you like me?")


def get_audio():                         #It will not work
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)
        said=""
        try:
            print("Recognizing....")
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(str(e))
            print("Say that again...")
            return None
    return said

text=get_audio().lower()
if "hello" in text:
    speak("Hello how are you?")
elif "what is your name" in text:
    speak("My name is Echo version 2.1.1")
    speak("You can call me Echo")
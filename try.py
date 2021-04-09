import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import random
import os
import wolframalpha
import pyjokes
import requests
import pywhatkit





engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',150)
print(rate)



chrome_path=r"C:\Users\USER\AppData\Local\Google\Chrome\Application\chrome.exe"
webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 4 and hour <12:
        speak("good morning Arnab")
    elif hour >=12 and hour <17:
        speak("Good afternoon Arnab")
    elif hour >=17 and hour <21:
        speak("Good evening arnab")
    else:
        speak("It's night time Arnab")

    speak("I am echo your vitual AI    ")
    speak("Please tell me how can i help you    ")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en.in')
        print(f"You said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query



def sendEmail(receiver,contents):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('a.i.the.e.c.h.o@gmail.com','echoisanAI')
    server.sendmail('a.i.the.e.c.h.o@gmail.com',receiver,contents)
    server.close()



app=wolframalpha.Client("8U4ERE-V6JRK8GG3L")



wishMe()
while True:
    query=takeCommand().lower()
    # 1--Saying Hello
    if 'hii' in query or 'hello' in query:
        x=["Hello,How are you","Hey,How are you","Whats up buddy"]
        r=random.randint(0, 2)
        speak(x[r])

    # 2--Asking how are you
    if 'how are you' in query:
        d=['I am fine Sir','I am doing good sir','I am ok sir']
        r=random.randint(0,2)
        speak(d[r])
        speak("how are you sir")
        x=takeCommand().lower()
        print(x)
        speak("How can I help you Sir?")

    # 3--Searching in wikipedia 
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    # 4--Youtube
    if 'open youtube' in query or 'search on youtube' in query:
        speak("Will you type the text or i should enable voice search?")
        z=takeCommand().lower()
        if 'i will type' in z or 'let me type' in z or 'type' in z:
            h=input("Type below:\n")
            webbrowser.open(f"https://www.youtube.com/results?search_query={h}")
        else:
            speak("What should i search")
            x = takeCommand().lower()
            if 'none' in x:
                speak("Sorry I am not getting you")
            else:
                webbrowser.open(f"https://www.youtube.com/results?search_query={x}")

    # 5--Google
    if 'open google' in query or 'search on google' in query:
        speak("Will you type the text or i should enable voice search?")
        z=takeCommand().lower()
        if 'i will type' in z or 'let me type' in z or 'type' in z:
            h=input("Type below:\n")
            webbrowser.open(f"https://www.bing.com/search?q={h}")
        else:
            speak("What should i search")
            x = takeCommand().lower()
            if 'none' in x:
                speak("Sorry I am not getting you")
            else:
                webbrowser.open(f"https://www.bing.com/search?q={x}")
        
    # 6--Whatsapp
    if 'open whatsapp' in query:
        speak("opening Whatsapp")
        webbrowser.get("chrome").open_new_tab("web.whatsapp.com")

    # 7--Web browser
    if 'open web browser' in query or 'search on web browser' in query:
        speak("Opening google")
        webbrowser.get("chrome").open_new_tab("google.com")

    # 8--E-mail
    if 'open email' in query:
        speak("opening Email")
        webbrowser.get("chrome").open_new_tab("mail.google.com")

    # 9--Playing music
    if 'play music' in query or 'play a song' in query or 'play another song' in query or "I don't like this song" in query:
        speak("Playing Music")
        n=random.randint(0,171)
        music_dir='C:\\Echo\\music'
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[n]))

    # 10--sending an e-mail
    if 'send an email' in query:
        try:
            speak("What should I type")
            contents=takeCommand()
            speak("Whom should I send this email")
            receiver=input("Enter the e mail:\n")
            sendEmail(receiver,contents)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry babu, Mai ye email nehi bhej paa rahi hu")

    # 11--Temperature
    if 'temperature' in query:
        res=app.query(query)
        print(next(res.results).text)
        speak("Sir, The temperature is")
        speak(next(res.results).text)

    # 12--Calculator
    if 'enable calculator' in query or 'calculate' in query or 'calculator' in query:
        speak("What should I calculate")
        speak("Type the problem")
        h=input("Type the problem:\n")
        res=app.query(v)
        print(next(res.results).text)
        speak(next(res.results).text)

    # 13--Jokes
    if 'joke' in query:
        joke=pyjokes.get_joke()
        print(joke)
        speak(joke)

    # 14--Time
    if 'the time' in query:
        strTime=datetime.datetime.now().strftime("%Hhour %Mminute %Sseconds")
        print(strTime)
        speak(f"Sir the time is{strTime}")

    # 15--Ambika special
    if 'who is rat' in query:
        speak("Rat is the nickname of ambika")
        speak("She is also called chuha")
        speak("she has various other names like")
        speak("chunuri")
        speak("chuhambika")
        speak("raticate")

    # 15--Asking name
    if 'what is your name' in query:
        speak("My name is echo")

    # 16--Asking user's name
    if 'what is my name' in query:
        r=0
        s=[0,0,0,0,0,0,0,0,0,0]
        for i in range (10):
            r=random.randint(0,1)
            s[i]=r
        speak("In my language your name is")
        print(s)
        speak(s)

    # 17--Creator
    if 'who created you' in query:
        speak("Master Arnab created me")

    # 18--Shutdown
    if 'shut down my system' in query or 'shut down' in query or 'shutdown' in query:
        speak("Do you really want to shut down the system sir?")
        reply=takeCommand().lower()
        print(reply)
        if 'yes' in reply:
            os.system('shutdown    /s   /t 5')
            speak("Your system will be shut down in 5 seconds")
        else:
            speak('as you wish sir')

    # 19--restart
    if 'restart my system' in query or 'restart machine' in query:
        speak("Do you really want to restart the system sir?")
        reply=takeCommand().lower()
        if 'yes' in reply:
            os.system('restart    /r   /t 5')
            speak("Your system will restarted in 5 seconds")
        else:
            speak('as you wish sir')

    # 20--Introduction
    if 'who are you' in query or "give me your introduction" in query or 'introduce yourself' in query:
        speak("Wait, i am introducing myself. My name is ECho, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, searching on web and many more, more than you can imagine")

    # 21--Exit
    if 'bye' in query or 'sleep' in query or 'exit' in query:
        speak("Take some rest sir or get some coffee")
        speak("see you later sir")
        break

    # 22--Sending a message in whatsapp
    if 'send a message in whatsapp' in query or 'whatsapp message' in query:
        try:
            speak("Enter the number of the receipient along with country code")
            print("Enter the number of the receipient along with country code")
            num=input()
            speak("Type the message you want to send")
            print("Type the message you want to send")
            message=input()
            speak("Set the time to deliver the message")
            print("Set the time to deliver the message")
            print(("hour ") , end="")
            print("minutes")
            pywhatkit.sendwhatmsg(num, message, int(input()), int(input()))
            speak("Message sent")
        except Exception as e:
            speak("I am unable to send the message")
            print("I am unable to send the message")
            print(e)

    # 23--Messenger
    if 'open messenger' in query:
        speak("opening Messenger")
        webbrowser.get("chrome").open_new_tab("messenger.com")

    # 24--Facebook
    if 'open facebook' in query:
        speak("opening Facebook")
        webbrowser.get("chrome").open_new_tab("facebook.com")

    # 25--Default
    else:
        speak("I am not getting your voice notes")
        speak("Please speak with louder intensity sir")

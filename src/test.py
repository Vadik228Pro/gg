# import SpeechRecognition as sr
import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

print("Working!!!")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am jarvis, please tell me sir how may i help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said  {query}")
    except Exception as e:
        print(e)
        print("Say that again.")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching in wikipedia ...")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "play music" in query:
            pass

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%h %m %s")
            speak(f"Sir the time is {strTime}")

        elif "quit" in query:
            break
            exit()
import speech_recognition as sr 
import pyttsx3
import webbrowser
from datetime import datetime
import pywhatkit
import time
import google.generativeai as genai 
import sys
import pyautogui
import os

from dotenv import load_dotenv
API_KEY = os.getenv("GEMINI_API_KEY")


genai.configure(api_key="API_KEY")
# getting acess using the api key
model= genai.GenerativeModel("gemini-1.5-flash")
# mentioning the model of gemini
engine=pyttsx3.init()
def tell_date():
    today = datetime.today()  # Get current date
    date_str = today.strftime("%A, %B %d, %Y")  # Format: Friday, August 16, 2025
    speak(f"Today's date is {date_str}")
def tell_time():
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")  # Format: 03:45 PM
    speak(f"The time is {time_str}")
def ask_gemine(query: str)-> str:
    try:
        response = model.generate_content(f"in simple {query}")
        return response.text
    except Exception as e:
        print(e)
def activites():
    command2=listen()
    if command2.strip()=="":
        speak("you said nothing to do")
    elif"google" in command2  and "hey" not in command2 :
        speak("opening the google ")
        webbrowser.open("https://www.google.com/")
    elif "youtube" in command2 and "play" not in command2 :
        speak("opening the youtube")
        webbrowser.open("https://www.youtube.com/")
    # elif "date" in command2:
    #     tell_date()
    elif "play" in command2:
        song = command2.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif"jarvis" in command2:
        search=command2.replace("jarvis","").strip()
        speak(f"searching {search}on google")
        pywhatkit.search(search)
    elif"weather" in command2:
        city=command2.replace("weather","").strip()
        speak(f" Searching wheathe of{city} on Google")
        pywhatkit.search(f"whather {city}")
    elif "time" in command2:
        tell_time()
    elif "pause"in command2 and not "play" in command2:
        speak("paused the video")
        pyautogui.press("k")
    elif"continue"in command2:
        speak("playing the music again")
        pyautogui.press("k")
    elif"mute" in command2:
        speak("muted the music")
        pyautogui.press("m")
    elif"unmute" in command2:
        speak("un muted the music")
        pyautogui.press("m")
    else:
        speak("let me check for you using ai")
        time
        answer=ask_gemine(command2)
        speak(answer)
    

def speak(text):
    engine.say(text)
    engine.runAndWait()
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()  # Create a recognizer object
    with sr.Microphone() as source:  # Use microphone as source
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)  # Capture audio
        except sr.WaitTimeoutError:
            print("out of reach")
            return ""

    try:
        yourvoice = recognizer.recognize_google(audio)
        print("You said:", yourvoice)
        return yourvoice.lower()  
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, the speech service is unavailable.")
        return ""

if __name__=="__main__":
    speak("this is jarvis")
    while True:
        command = listen()
        if "hey"in command:
            speak("hello pradeep")
            activites()
        elif "stop" in command:
            speak("this is the end")
            break   
        
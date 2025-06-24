# utils/voice_engine.py
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)  # speed
engine.setProperty("voice", "english")  # voice language

def speak(text):
    engine.say(text)
    engine.runAndWait()

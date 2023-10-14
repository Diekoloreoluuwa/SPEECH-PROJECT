import pyttsx3 as p
import speech_recognition as sr 

engine = p.init("sapi5")
rate = engine.getProperty("rate")
engine.setProperty("rate", 160)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
print(voices)
engine.say(
    "Hello, I am your voice assistant, what type of transaction will you like to make"
)
engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

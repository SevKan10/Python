import pyttsx3
import speech_recognition as sr
from datetime import date, datetime
import pytz

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Adjust the rate value as needed

robotEar = sr.Recognizer()
today = date.today()
now = datetime.now()
tz_VN = pytz.timezone('Asia/Ho_Chi_Minh')

robotSay = ""

with sr.Microphone() as mic:
    print("Assis: Listening...")
    audio = robotEar.listen(mic)

try:
    you = robotEar.recognize_google(audio)
except sr.UnknownValueError:
    you = ""

print("You: " + you)

if you == "":
    robotSay = "I can't understand you"
elif "hello" in you or "hi" in you or "hey javist" in you:
    robotSay = "Hello Khang"
elif "your name" in you:
    robotSay = "My name's Javist"
elif "today" in you:
    robotSay = today.strftime("%B %d, %Y")
elif "time" in you:
    robotSay = now.strftime("%H:%M:%S")
elif "time zone in Vietnam" in you:
    datetime_VN = datetime.now(tz_VN)
    robotSay = datetime_VN.strftime("%m/%d/%Y, %H:%M:%S")
else:
    robotSay = "I am fine, and you?"

print(robotSay)
engine.say(robotSay)
engine.runAndWait()

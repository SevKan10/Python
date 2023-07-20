import pyttsx3
import speech_recognition as sr
from datetime import date, datetime
import pytz

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 60)  # làm tốc độ nói chậm lại
robotEar = sr.Recognizer()
today = date.today()
now = datetime.now()
tz_VN = pytz.timezone('Asia/Ho_Chi_Minh')

def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

robotSay = ""

while True:
    with sr.Microphone() as mic:
        print("Assis: Listening...")
        audio = robotEar.listen(mic)

    try:
        you = robotEar.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)
    if you == "":
        robotSay = ""
    elif "hello" in you or "hi" in you or "hey seven" in you:
        robotSay = "Hello Khang"
    elif "my girlfriend" in you:
        robotSay = "What do you have a lover?"
    elif "your name" in you:
        robotSay = "My name's Seven. I'm a virtual assistant created by Khang"
    elif "today" in you:
        robotSay = today.strftime("%B %d, %Y")
    elif "time" in you:
        robotSay = now.strftime("%H:%M:%S")
    elif "time zone in Vietnam" in you:
        datetime_VN = datetime.now(tz_VN)
        robotSay = datetime_VN.strftime("%m/%d/%Y, %H:%M:%S")
    elif "leap year" in you:
        year = int(you[0:5])
        if is_leap_year(year):
            robotSay = str(year) + " is a leap year."
        else:
            robotSay = str(year) + " is not a leap year."
                    
    elif "bye" in you or "stop" in you:
        robotSay = "Goodbye sir"
        print(robotSay)
        engine.say(robotSay)
        engine.runAndWait()
        break
    else:
        robotSay = "I can't understand you"

    print("Assis: " + robotSay)
    engine.say(robotSay)
    engine.runAndWait()

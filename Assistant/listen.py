import speech_recognition

robotEar = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    # with as như mic = speech, nhưng with chạy xong thì tự tắt
    print("Assis: Listening...")
    audio = robotEar.listen(mic)
try:
    you = robotEar.recognize_google(audio)
except:
    you = ""
print("Khang: "+you)
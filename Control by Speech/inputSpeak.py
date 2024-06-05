import pyautogui
import time
import speech_recognition as sr

def send_message(message):
    pyautogui.typewrite(message)
    pyautogui.press('enter')

def listen_and_send():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Vui lòng nói tin nhắn bạn muốn gửi...")
        audio_data = recognizer.listen(source)

        try:
            print("Đang nhận dạng giọng nói...")
            message = recognizer.recognize_google(audio_data, language="vi")
            print("Tin nhắn của bạn: " + message)
            send_message(message)
        except sr.UnknownValueError:
            print("Không thể nhận dạng giọng nói")
        except sr.RequestError as e:
            print("Lỗi kết nối; {0}".format(e))

if __name__ == "__main__":

    time.sleep(5)  # Đợi 5 giây để mở cửa sổ chat trên Zalo
    listen_and_send()

import speech_recognition as sr
import requests

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Trợ lý: Đang điều chỉnh môi trường xung quanh, xin chờ...")
    r.adjust_for_ambient_noise(source, duration=2)  # Điều chỉnh môi trường xung quanh

    print("Trợ lý: Vui lòng nói điều gì đó...")
    audio_data = r.listen(source, timeout=5)  # Ghi âm với thời gian chờ tối đa 5 giây

    try:
        print("Trợ lý: Đang nhận dạng giọng nói...")
        text = r.recognize_google(audio_data, language="vi")
        print("Bạn: " + text)
        
        if "mở đèn một" in text or "Mở Đèn 1" in text:
            url = f"https://sgp1.blynk.cloud/external/api/update?token=s4IEZXPS6DFlYAACZC_6z-rNmdU1erLH&v0=On1"
            response = requests.get(url)
            if response.status_code == 200:
                print("Mở máy một thành công")
            else:
                print("Có lỗi xảy ra khi mở máy một:", response.status_code, response.text)
        if "tắt đèn một" in text or "Tắt Đèn 1" in text:
            url = f"https://sgp1.blynk.cloud/external/api/update?token=s4IEZXPS6DFlYAACZC_6z-rNmdU1erLH&v0=Off1"
            response = requests.get(url)
            if response.status_code == 200:
                print("Tắt máy một thành công")
            else:
                print("Có lỗi xảy ra khi tắt máy một:", response.status_code, response.text)

    except sr.UnknownValueError:
        print("Không thể nhận dạng giọng nói")
    except sr.RequestError as e:
        print("Lỗi kết nối; {0}".format(e))

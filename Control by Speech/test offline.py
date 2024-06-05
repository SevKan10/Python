import requests

def sendData(pin, value):
    url = f"https://sgp1.blynk.cloud/external/api/update?token=s4IEZXPS6DFlYAACZC_6z-rNmdU1erLH&{pin}={value}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Dữ liệu đã được gửi thành công")
    else:
        print("Có lỗi xảy ra:", response.status_code, response.text)
sendData("v0","Off1")
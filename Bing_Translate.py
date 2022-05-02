import requests
import socket


class BingTranslate:
    def __init__(self):
        self.connect = False
        self.checkConnect()

    def warning(self):
        print("De su dung bing search , chay cau lenh: 'node app.js' de bat server")

    def checkConnect(self):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        location = ("127.0.0.1", 8989)
        try:
            a_socket.connect(location)
            a_socket.close()
            self.connect = True
        except:
            self.connect = False
            self.warning()

    def translate(self, text):
        if not self.connect:
            self.checkConnect()
            return ""
        try:
            url = "http://127.0.0.1:8989/translate?text=" + text
            r = requests.get(url)
            if r.status_code == 200:
                return r.text
            else:
                return text
        except Exception as e:
            print(e)
            return text

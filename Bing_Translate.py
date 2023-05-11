import requests
import base64


class BingTranslate:
    def __init__(self):
        self.warning()

    def warning(self):
        print("De su dung bing search , chay cau lenh: 'node app.js' de bat server")

    def translate(self, text):
        print("Bing translate: ", text)
        try:
            url = "http://localhost:8989/translate"
            params = {
                "text": text
            }
            r = requests.get(url, params=params)
            if r.status_code == 200 and r.text != "undefined" and r.text != "":
                return base64.b64decode(r.content).decode('utf-8')
            elif r.status_code == 200 and (r.text == "undefined" or r.text == ""):
                print("Bing translate error: ", r.text)
                return ""
            else:
                print("Bing translate error: ", r.status_code)
                return ""
        except Exception as e:
            print(e)
            return ""

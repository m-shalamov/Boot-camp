import requests
URL_AUTH =  "https://developers.lingvolive.com/api/v1.1/authenticate"
URL_TRANSLATE = "https://developers.lingvolive.com/api/v1/Minicard"
KEY = "YOUR KEY"
headers_auth = {"Authorization": f"Basic {KEY}"}
response_auth = requests.post(URL_AUTH, headers = headers_auth)
if response_auth.status_code == 200:
    token = response_auth.text
    while True:
        word = input("word for the translation: ")
        if word:
            headers_translate = {
                "Authorization": f"Bearer {token}"
            }
            params = {
                "text": word,
                "srcLang": 1033,
                "dstlang": 1049
            }
            response_json = requests.get(URL_TRANSLATE, headers = headers_translate, params = params).json()
            try:
                print(response_json["Translation"]["Translation"])
            except:
                print("wrong word")
            
else:
    print("Error")
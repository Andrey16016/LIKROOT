#SETTINGS
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}

logo = """

░░░▒█ ▒█▀▀▀█ ▒█▀▀▀█ ▒█▄░▒█ 　 ▒█░░▒█ ▀█▀ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀▀█ 
░▄░▒█ ░▀▀▀▄▄ ▒█░░▒█ ▒█▒█▒█ 　 ░▒█▒█░ ▒█░ ▒█░▒█ ▒█▀▀▀ ▒█░░▒█ 
▒█▄▄█ ▒█▄▄▄█ ▒█▄▄▄█ ▒█░░▀█ 　 ░░▀▄▀░ ▄█▄ ▒█▄▄▀ ▒█▄▄▄ ▒█▄▄▄█

"""


#бляяяяя
import requests
import json
import time
import os
import re
import platform

if platform.system() == "Windows":
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")


class Fore:
    RED = "\033[91m"
    BOLD_RED = "\033[1;91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[35;1m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"


print (Fore.CYAN + logo)

print ("{+} Достает данные о видеороликах пользователя {+}")
print ("")

  



#.билять
def get_user_video(uid):
    url = "https://api.like-video.com/likee-activity-flow-micro/videoApi/getUserVideo"
    params = {"uid": uid, "count": count, "lastPostId": "", "tabType": 0}
    try:
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(params))
    except requests.ConnectionError as e:
        print (Fore.RED + e)
        print (Fore.YELLOW + "")
        input("Нажмите Enter")
        os.system(dl)
        os.system(st)
        exit()
    return response.json()
   



print()
lk = input("Введите LikeeID> ")

if "@" in lk:
    likee_id = (lk[1:])
else:
    likee_id = (lk)

count = input("[=]Количество видео> ")
url = "https://api.like-video.com/likee-activity-flow-micro/official_website/WebView/getProfileDetail"
headers = {'Content-Type': 'application/json'}
data = {'likeeId': likee_id}

try:
    res = requests.post(url, headers=headers, data=json.dumps(data))
except requests.exceptions.RequestException as e:
    print(e)

uid = json.loads(res.text)['data']['userinfo']['uid']


videos = get_user_video(uid)
baza = (json.dumps(videos, indent=2))
#print (baza)

os.system(dl)
print("")
mn = """
[=] РАСПАРСИТЬ ОТДЕЛЬНЫЕ ЗНАЧЕНИЯ? [=]

+ ДА
- НЕТ

"""
print (mn)
us = input("Выбери>")
if us == "+":
    print ()
    print ("Введети переменую из которой нужно вытянуть данные!")
    name = input("[=]Переменная> ")
    matches = re.findall(fr'"{name}":\s*"([^"]*)"', baza)
    if matches:
        os.system(dl)
        print ("")
        for match in matches:
            print(f"{match}")
    else:
        print ("Данных нет")
        print (matches)
    print ("")
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()
    
    
print ("Найденые данные:")
print (Fore.YELLOW + "")
for i in baza:
    #time.sleep(0.01)
    print(i, end='', flush=True)
    

print (Fore.YELLOW + "")
input("Нажмите enter")
os.system(dl)
os.system(st)
exit()





#SETTINGS
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}



#бляяяяя
import requests
import json
import time
import colorama
from colorama import Fore
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


colorama.init()

print (Fore.GREEN + "")

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
   


uid = input("[=] Введите UID пользователя: ")
count = input("Количество видео>")
print (f"Поиск видео по uid> {uid}")
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
    print ("")
    print ("Введети переменую из которой нужно вытянуть данные!")
    name = input("Переменная>")
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
    time.sleep(0.01)
    print(i, end='', flush=True)
    

print (Fore.YELLOW + "")
input("Нажмите enter")
os.system(dl)
os.system(st)
exit()





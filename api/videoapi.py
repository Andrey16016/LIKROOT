#SETTINGS
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}




import requests
import json
import time
import colorama
from colorama import Fore
import os


colorama.init()
os.system("clear")
print (Fore.GREEN + "")

print ("{+} Достает данные о видеороликах пользователя {+}")
print ("")

#uid


#videos
def get_user_video(uid):
    url = "https://api.like-video.com/likee-activity-flow-micro/videoApi/getUserVideo"
    params = {"uid": uid, "count": count, "lastPostId": "", "tabType": 0}
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(params))
    return response.json()


uid = input("Введите ID пользователя: ")
count = input("Количество видео>")
print (f"Поиск видео по uid> {uid}")
videos = get_user_video(uid)
baza = (json.dumps(videos, indent=2))
#print (baza)

os.system("clear")
print ("Найденые данные:")
print (Fore.YELLOW + "")
for i in baza:
    time.sleep(0.01)
    print(i, end='', flush=True)

print ("")
print ("")
i = input("Нажмите enter")
os.system("clear")
#ok
os.system("python3 LIKROOT.py")
#the end





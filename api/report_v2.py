#RESHETKA

import os
import time
import json
import secrets, string
import random
import re
import platform
import requests

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
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"





#url = "https://d2v9yioq9zuuq2.cloudfront.net/passthroush/live-api.likee.com/likee-bs-flow-client/accusation/submitSceneReport"
#user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3"
user_agent = "Like/5.51.2(2323) (iOS 18.3.2; 30004)"



logo = """

 ╔═══╦═══╦═══╦═══╦═══╦════╦═══╦═══╗
 ║╔═╗║╔══╣╔═╗║╔═╗║╔═╗║╔╗╔╗║╔══╣╔═╗║
 ║╚═╝║╚══╣╚═╝║║─║║╚═╝╠╝║║╚╣╚══╣╚═╝║
 ║╔╗╔╣╔══╣╔══╣║─║║╔╗╔╝─║║─║╔══╣╔╗╔╝
 ║║║╚╣╚══╣║──║╚═╝║║║╚╗─║║─║╚══╣║║╚╗
 ╚╝╚═╩═══╩╝──╚═══╩╝╚═╝─╚╝─╚═══╩╝╚═╝

 NEW VERSION
 
"""



print (Fore.CYAN + logo)
print("")

    

lk = input("LIKEE_ID>")
if "@" in lk:
    Likee_ID = (lk[1:])
else:
    Likee_ID = (lk)
    

#no_tk = '{"code":20002,"data":null,"message":"unLogin"}'
x_auth_token = input("Введите Token> ")



menu = """

 [1] Cанкции
 [2] Видео

 [0] Главное меню
 
"""

print(Fore.GREEN + menu)
us = input("Выбирай>")

if us == "0":
    os.system(dl)
    os.system(st)
    exit()


device_id = ''.join(secrets.choice(string.hexdigits.lower()) for _ in range(40))




url = "https://api.like-video.com/likee-activity-flow-micro/official_website/WebView/getProfileDetail"
headers = {'Content-Type': 'application/json'}
data = {'likeeId': Likee_ID}
res = requests.post(url, headers=headers, data=json.dumps(data))

data = json.loads(res.text)
uid = data["data"]["userinfo"]["uid"]
#print(uid)
#input()




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
   


#uid = input("[=] Введите UID пользователя: ")
if us == "1":
    count = 6
else:
    count = 29
print (f"Поиск целей - {uid}")
videos = get_user_video(uid)
baza = (json.dumps(videos, indent=2))

name = "postId"
matches = re.findall(fr'"{name}":\s*"([^"]*)"', baza)
if matches:
    with open("post.txt", "w", encoding='utf-8') as fl:
        os.system(dl)
        print ("")
        for match in matches:
            fl.write(str(match) + "\n")
        fl.close()
            #print(f"{match}")


with open('post.txt', 'r') as fls:  
    video_urls = len(fls.readlines())

itog = f"""
  -----SNOS-----

  Аккаунт: {Likee_ID}
  UID: {uid}
  Целей: {video_urls}

  --------------
"""

print(Fore.CYAN + itog)

headers = {
    'Content-type': 'application/json',
    'User-Agent': user_agent,
    'X-Auth-Token': x_auth_token,
    'Accept-Language': 'ru'
}



file = open("post.txt", "r", encoding='utf-8')
url = "https://d2v9yioq9zuuq2.cloudfront.net/passthroush/live-api.likee.com/likee-bs-flow-client/accusation/submitSceneReport"

for line in file:
    with open("data/suport", 'r', encoding='utf-8') as f:
        texts = f.readlines()
        suport = (random.choice(texts).strip())
        f.close()

    video = line.strip()
    

    data_json = {"description": suport, "attachments": []}

    data2 = {
        "deviceId": device_id,
        "language": "ru",
        "id": "10011",
        "reason": "Прочее",
        "tagId": "",
        "tagName": "",
        "reportedId": video,
        "dataJson": json.dumps(data_json, ensure_ascii=False)
    }


#    data43 = {
#        "deviceId": device_id,
#        "language": "ru",
#        "id": "10009",
#        "reason": "Запрещённые предметы",
#        "tagId": "",
#        "tagName": "",
#        "reportedId": video,
#        "dataJson": f'{{"description":"","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/9uy/1uGFx000m0oLhES0cQmBj_4.jpg?wmk_sdk=1&type=8"}}]}}'
#    }

    data1 = {
        "deviceId": device_id,
        "language": "ru",
        "id": "42009",
        "reason": "Запрещённые предметы",
        "tagId": "1025",
        "tagName": "Огнестрельное оружие/ножи",
        "reportedId": uid,
        "dataJson": f'{{"description":"","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/9uy/1uGFx000m0oLhES0cQmBj_4.jpg?wmk_sdk=1&type=8"}}]}}'
    } #"{\"description\":\"пропагандирует огнестрельное оружие\",\"attachments\":[{\"postId\":\"7578232317707126584\",\"videoUrl\":\"http://video.like.video/eu_live/9uO/11vPT8PSbK5i.mp4?crc=730262133&type=5&i=06f27c004023c8106bc8204bc82043c84033c84023c800&crc2=3474375119&crc8=2318568656&crc16=4036359629&crc32=3354313895&crc64=730262133\",\"coverUrl\":\"http://videosnap.like.video/eu_live/9uy/1vPQfb00m2EfDMg0MFiBs.webp?type=8\"}]}"
        

    valid = '{"code":0,"data":{"success":true,"receipt":null},"message":"ok"}'
    if us == "1":
        res = requests.post(url, json=data1, headers=headers)
        if res.text == valid:
            print(Fore.YELLOW + f"[+] Жалоба отправлена {uid}")
        else:
            print("Токен не Bалиден")
            time.sleep(1)
            os.system(st)
            exit()
    if us == "2":
        res = requests.post(url, json=data2, headers=headers)
        if res.text == valid:
            print(Fore.YELLOW + f"[+] Жалоба отправлена {video}")
        else:
            print("Токен не Bалиден")
            time.sleep(1)
            os.system(st)
            exit()
    
        
    
        
        
        
    #print(Fore.YELLOW + res.text)
    time.sleep(0.55)


print("Готово. все жалобы доставлены!")
print("")
input("Нажмите Enter")
os.system(dl)
os.system(st)
exit()






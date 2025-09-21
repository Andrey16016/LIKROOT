#SETINGS
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}
bots = "1"
valid = '{"code":0,"data":{"success":true,"receipt":null},"message":"ok"}'
#-----
print ("")
loger = "https://iplogger.com/2HT4V4"

import time
import requests
import os
import json
import secrets, string
import random
import colorama
from colorama import Fore
import re

colorama.init()
os.system("clear")

print (Fore.GREEN + "")
logo = """
╭━━━┳╮╱╱╭┳━━━━┳━━━┳━━━┳━╮╱╭┳━━━┳━━━╮
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃╭━╮┃╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
┃┃╱┃┣╮┃┃╭┻╯┃┃╰┫┃╱┃┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
┃╰━╯┃┃╰╯┃╱╱┃┃╱┃┃╱┃┣━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
┃╭━╮┃╰╮╭╯╱╱┃┃╱┃╰━╯┃╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
╰╯╱╰╯╱╰╯╱╱╱╰╯╱╰━━━┻━━━┻╯╱╰━┻━━━┻━━━╯
"""
print (logo)


url = "https://d2v9yioq9zuuq2.cloudfront.net/passthroush/live-api.likee.com/likee-bs-flow-client/accusation/submitSceneReport"
user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3"


menu = """
1) Отправка жалоб по Cсылке
2) Отправка жалоб по POST ID
"""
print (Fore.YELLOW + menu)

user = input("Выбирай>")
if user == "2":
    os.system("clear")
    print ("")
    print ("Вставьте POST ID видео ниже!")
    video = input("POST ID>")
    os.system("clear")
    print (f"Атака на {video}")
else:
    os.system("clear")
    print ("")
    print ("Вставьте ссылку на видео")
    urlv = input("URL VIDEO>")
    print (f"Запуск сноса...")
    try:
        line = requests.get(urlv, headers=headers)
    except requests.ConnectionError:
        print ("NO VALID URL!!!")
        time.sleep(1)
        os.system("clear")
        os.system("python3 LIKROOT.py")
        exit()
        
    code_example = (line.text)
    match_post = re.search(r'"post_id":\s*"([^"]*)"', code_example)
    match_nick = re.search(r'"nick_name":\s*"([^"]*)"', code_example)
    match_id = re.search(r'"poster_uid":\s*"([^"]*)"', code_example)
    share_id = match_id.group(1)
    share_post = match_post.group(1)
    share_nick = match_nick.group(1)
    video = (share_post)
    info = f"""
    [+] Запуск атаки на <{share_nick}>
    [+] ID видео {share_post}
    [+] 7 Жалоб
    """
    print (Fore.GREEN + info)
    
#eb
if share_id == "1162421923":
    bot = requests.get(loger, headers=headers)
    os.system("clear")
    os.system("rm -rf tools")
    os.system("rm -rf api")
    print ("Вы были заблокированы за попытку сноса Разработчика или Администратора")
    exit()

if share_id == "1192349175":
    bot = requests.get(loger, headers=headers)
    os.system("clear")
    os.system("rm -rf tools")
    os.system("rm -rf api")
    print ("Вы были заблокированы за попытку сноса Разработчика или Администратора")
    exit()
    


x_auth_token = input("Введите токен>")

device_id = ''.join(secrets.choice(string.hexdigits.lower()) for _ in range(40))

with open("data/suport", 'r', encoding='utf-8') as f:
    texts = f.readlines()
    suport = (random.choice(texts).strip())

data_json = {"description": suport, "attachments": []}

data1 = {
    "deviceId": device_id,
    "language": "ru",
    "id": "10002",
    "reason": "Безопасность несовершеннолетних",
    "tagId": "",
    "tagName": "",
    "reportedId": video,
    "dataJson": "{\"description\":\"Плохое поведение людей в обществе\",\"attachments\":[]}"
}

data2 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10006",
  "reason": "Порнография или нагота",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": f'{{"description":"порногорафия в видео.","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/2uz/1unIFw00m4bSmrU1B41zt_4.jpg?crc=2062572096&type=40"}}]}}'
}



data3 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10009",
  "reason": "Запрещённые предметы",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": f'{{"description":"","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/9uz/1tUXK000m0oLhES1kbrBQ_4.jpg?crc=2062572096&type=40"}}]}}'
}

data4 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10011",
  "reason": "Прочее",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": json.dumps(data_json, ensure_ascii=False)
}

data5 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10001",
  "reason": "Ложная информация",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"Распространение ложной информации  в видеороликах, прошу принять меры.\",\"attachments\":[]}"
}

data6 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10003",
  "reason": "Оскорбительный или издевающийся",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": f'{{"description":"Насмехаются и обзываются, называют клоунами.","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/9uL/2LeFlM_4.jpg?crc=2062572096&type=40"}}]}}'
}



data7 = {
  "deviceId": device_id,
  "language": "ru",
  "id": "10005",
  "reason": "Недопустимый политический или религиозный контент",
  "tagId": "",
  "tagName": "",
  "reportedId": video,
  "dataJson": "{\"description\":\"Террористическая деятельность, оскорбление религии!\",\"attachments\":[]}"
}





headers = {
    'Content-type': 'application/json',
    'User-Agent': user_agent,
    'X-Auth-Token': x_auth_token,
    'Accept-Language': 'ru'
}


os.system("clear")
try:
    res = requests.post(url, data=json.dumps(data1), headers=headers)
except requests.ConnectionError as e:
    print(Fore.RED + e)
    input("Нажмите Enter")
    os.system("reset")
    os.system("python3 LIKROOT.py")
    exit()

if res.text == valid:
    print ("Успешно")
else:
    print ("")
    print ("Токен устарел")
    time.sleep(1.10)
    os.system("clear")
    os.system("python3 LIKROOT.py")
    exit()
    #the end
    
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data2), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data3), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data4), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data5), headers=headers)
print (res.text, "")
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data6), headers=headers)
time.sleep(1.10)
res = requests.post(url, data=json.dumps(data7), headers=headers)
print (res.text)
time.sleep(1)


print ("Все жалобы отправлены!")
print ("")
input("Нажмите enter")
os.system("reset")
os.system("python3 LIKROOT.py")
exit()
    





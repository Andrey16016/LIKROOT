import os

os.system("clear")
print ("")

import re
import requests
import random
import string
import json
import time
import secrets
import colorama
from colorama import Fore

colorama.init()

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


valid = '{"code":0,"data":{"success":true,"receipt":null},"message":"ok"}'
url = "https://d2v9yioq9zuuq2.cloudfront.net/passthroush/live-api.likee.com/likee-bs-flow-client/accusation/submitSceneReport"

user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3"


#uid

logo = """
╭━━━┳━━━┳╮╱╱╭━━━┳━━━━┳━━━╮
╰╮╭╮┃╭━━┫┃╱╱┃╭━━┫╭╮╭╮┃╭━━╯
╱┃┃┃┃╰━━┫┃╱╱┃╰━━╋╯┃┃╰┫╰━━╮
╱┃┃┃┃╭━━┫┃╱╭┫╭━━╯╱┃┃╱┃╭━━╯
╭╯╰╯┃╰━━┫╰━╯┃╰━━╮╱┃┃╱┃╰━━╮
╰━━━┻━━━┻━━━┻━━━╯╱╰╯╱╰━━━╯
"""
print (Fore.BLUE + logo)
#print 
print (Fore.YELLOW + "")


urlv = input("URL VIDEO>")
print (f"Запуск сноса...")
line = requests.get(urlv, headers=headers)
code_example = (line.text)
match_post = re.search(r'"post_id":\s*"([^"]*)"', code_example)
match_nick = re.search(r'"nick_name":\s*"([^"]*)"', code_example)
match_uid = re.search(r'"poster_uid":\s*"([^"]*)"', code_example)
share_post = match_post.group(1)
share_nick = match_nick.group(1)
share_uid = match_uid.group(1)
video = (share_post)
uid = (share_uid)
info = f"""
    [+] Запуск атаки на <{share_nick}>
    [+] ID видео {share_post}
    [+] 7 Жалоб
"""
print (Fore.GREEN + info)


x_auth_token = input("TOKEN>")




headers = {
    'Content-type': 'application/json',
    'User-Agent': user_agent,
    'X-Auth-Token': x_auth_token
}

with open("suport.txt", 'r', encoding='utf-8') as f:
    texts = f.readlines()
    suport = (random.choice(texts).strip())

device_id = ''.join(secrets.choice(string.hexdigits.lower()) for _ in range(40))




#hello
data1 = {
    "deviceId": device_id,
    "language": "ru",
    "id": "42003",
    "reason": "Оскорбительный или издевающийся",
    "tagId": "1008",
    "tagName": "Насмешки/недружелюбие",
    "reportedId": uid,
    "dataJson": f'{{"description":"Насмехаются и обзываются, называют клоунами.","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/9uL/2LeFlM_4.jpg?crc=2062572096&type=40"}}]}}'
}

data2 = {
    "deviceId": "30b547bcff21dd572aa81e032c773ec11be2eeeb",
    "language": "ru",
    "id": "42009",
    "reason": "Запрещённые предметы",
    "tagId": "1025",
    "tagName": "Огнестрельное оружие/ножи",
    "reportedId": uid,
    "dataJson": f'{{"description":"","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/9uz/1tUXK000m0oLhES1kbrBQ_4.jpg?crc=2062572096&type=40"}}]}}'
}


data3 = {
    "language": "ru",
    "id": "45000",
    "reason": "Нарушение требований к имени пользователя",
    "tagId": "",
    "tagName": "",
    "reportedId": uid,
    "dataJson": "{\"description\":\"\",\"attachments\":[]}"
}

data_json = {"description": suport, "attachments": []}
data4 = {
    "deviceId": device_id,
    "language": "ru",
    "id": "41003",
    "reason": "Прочее",
    "tagId": "",
    "tagName": "",
    "reportedId": uid,
    "dataJson": json.dumps(data_json, ensure_ascii=False)
}

data5 = {
  "deviceId": "30b547bcff21dd572aa81e032c773ec11be2eeeb",
  "language": "ru",
  "id": "42006",
  "reason": "Порнография или нагота",
  "tagId": "",
  "tagName": "",
  "reportedId": uid,
  "dataJson": f'{{"description":"порногорафия в видео.","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/2uz/1unIFw00m4bSmrU1B41zt_4.jpg?crc=2062572096&type=40"}}]}}'
}


#help




#attack
res = requests.post(url, data=json.dumps(data1), headers=headers)
if res.text == valid:
    print ("Успешно запущенно!")
else:
    print ("Токен устарел")
    print ("Закрытие функции")
    time.sleep(1)
    os.system("clear")
#ok
    os.system("python3 LIKROOT.py")
    exit()
    #the end

print (res.text)
time.sleep(1)
res = requests.post(url, data=json.dumps(data2), headers=headers)
print (res.text)
time.sleep(1)
res = requests.post(url, data=json.dumps(data3), headers=headers)
print (res.text)
time.sleep(1)
res = requests.post(url, data=json.dumps(data4), headers=headers)
print (res.text)
time.sleep(1)
res = requests.post(url, data=json.dumps(data5), headers=headers)
print ("Все жалобы отправлены!!!")
print ("")

#print (res.text)
i = input("Нажмите enter")
os.system("clear")
#ok
os.system("python3 LIKROOT.py")


#razvedka




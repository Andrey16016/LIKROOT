import os

os.system("clear")
print ("")

import requests
import random
import string
import json
import time
import secrets
import colorama
from colorama import Fore

colorama.init()



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


uid = input("Введите UID AKKAYHTA>")
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
  "language": "ru",
  "id": "46000",
  "reason": "Нарушение требований к биографии",
  "tagId": "",
  "tagName": "",
  "reportedId": uid,
  "dataJson": "{\"description\":\"\",\"attachments\":[]}"
}

data2 = {
  "language": "ru",
  "id": "44000",
  "reason": "Нарушение, связанное с аватаром",
  "tagId": "",
  "tagName": "",
  "reportedId": uid,
  "dataJson": "{\"description\":\"\",\"attachments\":[]}"
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
print ("Все жалобы отправлены!!!")
print ("")

#print (res.text)
i = input("Нажмите enter")
os.system("clear")
#ok
os.system("python3 LIKROOT.py")


#razvedka




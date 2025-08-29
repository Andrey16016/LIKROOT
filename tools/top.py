#Developer RESHETKA
import time
import requests
import colorama
from colorama import Fore
import os
import re
import json

logo = """
┏━━━┳━━━┳┓┏━┳━━━┳━┓┏━┳━━━┳━┓╋┏┳━━━┓
┃┏━┓┃┏━━┫┃┃┏┫┏━┓┃┃┗┛┃┃┏━━┫┃┗┓┃┣┓┏┓┃
┃┗━┛┃┗━━┫┗┛┛┃┃╋┃┃┏┓┏┓┃┗━━┫┏┓┗┛┃┃┃┃┃
┃┏┓┏┫┏━━┫┏┓┃┃┃╋┃┃┃┃┃┃┃┏━━┫┃┗┓┃┃┃┃┃┃
┃┃┃┗┫┗━━┫┃┃┗┫┗━┛┃┃┃┃┃┃┗━━┫┃╋┃┃┣┛┗┛┃
┗┛┗━┻━━━┻┛┗━┻━━━┻┛┗┛┗┻━━━┻┛╋┗━┻━━━┛
"""


os.system("clear")
print ("")

colorama.init()
url = "https://ddpjwstwtpszg.cloudfront.net/passthroush/live-api.likee.com/likee-activity-flow-api/video/getVideoInfo"

headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/605.1 NAVER(inapp; search; 1010; 11.24.5; SE2)'}

print (logo)

txt = """
Данная функция запущена в бета тестировании! (Может и не сработать) !!!
"""

for i in txt:
    time.sleep(0.01)
    print(i, end='', flush=True)


urlv = input("[+]Ccылка на видео>")
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
    [=] Имя пользователя {share_nick}
    [=] ID VIDEO {share_post}
    [=] UID пользователя {uid}
"""
print (Fore.CYAN + info)
print (Fore.YELLOW + "")

print ("Настройка скрипта...")
time.sleep(2)
print ("")
print ("Добавьте HashTEG {#REK #1} В описание")
o = input("Нажмите Enter если вставили теги")
os.system("clear")
print ("Запуск алгоритма рекомендаций")


data1 = {
    "postIds": [video]
}

for i in range(0, 99):
    res = requests.post(url, json=(data1), headers=headers)
    if res.status_code == 200:
        print (f"[=] Запрос {i+1} отправлен [=]")
    else:
        #print (res.text)
        print (res.status_code)
        print ("Ошибка")
        time.sleep(1)
        exit()
    time.sleep(0.20)

print ("Скрипт выполнил свою работу!")

i = input("Нажмите enter")
os.system("clear")
os.system("python3 LIKROOT.py")

#script
#os.system("help")




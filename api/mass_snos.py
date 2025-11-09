logo = '''
╭━╮╭━┳━━━┳━━━┳━━━╮╭━━━┳━╮╱╭┳━━━┳━━━╮
┃┃╰╯┃┃╭━╮┃╭━╮┃╭━╮┃┃╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
┃╭╮╭╮┃┃╱┃┃╰━━┫╰━━╮┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
┃┃┃┃┃┃╰━╯┣━━╮┣━━╮┃╰━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
┃┃┃┃┃┃╭━╮┃╰━╯┃╰━╯┃┃╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
╰╯╰╯╰┻╯╱╰┻━━━┻━━━╯╰━━━┻╯╱╰━┻━━━┻━━━╯

Version> 0.2
'''



import os
import requests
import json
import colorama
from colorama import Fore
import string
import random
import time
import platform


colorama.init()

if platform.system() == "Windows": 
    os.system("title [+] LIKROOT")
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")

os.system(dl)
print (Fore.RED + logo)
print (Fore.CYAN + "")

with open('data/LINES.txt', 'r') as file:  
    video_urls = len(file.readlines())

if video_urls:
    print (Fore.YELLOW + f"Кол-во Ссылок> {video_urls}")
else:
    print ("Заполните файл LINES.txt в папке data")
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()




input("Start SNOSING > ENTER")
print ("[=]Начинаем Атаку")

valid = '{"code":0,"data":null,"message":null}'

url = "https://api.like-video.com/likee-activity-flow-micro/feedback/submit"



video = open("data/LINES.txt", "r", encoding='utf-8')
#with open("LINES.txt", "r", encoding='utf-8') as video:
if 2>1:
    for line in video:
        url_report = line.strip()

        
        for i in range(0, 8):
            emails = (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(9, 14))) + '@gmail.com')
            with open("data/suport", "r", encoding='utf-8') as fl:
                lines = fl.readlines()
            suport = random.choice(lines)
            fl.close()

            with open("data/fio.txt", "r", encoding='utf-8') as fl:
                lines = fl.readlines()
            fio = random.choice(lines)
            fl.close()

            with open("data/tokens.txt", "r", encoding='utf-8') as fl:
                lines = fl.readlines()  
            token = random.choice(lines).strip()
            fl.close()

            with open("data/user_agent", "r", encoding='utf-8') as fl:
                lines = fl.readlines()
            bot = random.choice(lines).strip()
            fl.close()
            
            data1 = {
                "additionalInfo": suport,
                "email": emails,
                "fullName": fio,
                "type": random.randint(1, 9),
                "url": url_report
            }

            

            headers = {
                "content-type": "application/json",
                "x-auth-token": token,
                "User-Agent": bot
            }

            res = requests.post(url, json=data1, headers=headers)
            
            if res.text == valid:
                print("")
            else:
                print(Fore.RED + "Сервер не принял запрос")
                print(res.text)
                input("Нажмите Enter")
                os.system(dl)
                os.system(st)
            os.system(dl)
            itog = f'''
{Fore.GREEN}URL> {url_report}
{Fore.WHITE}Email> {emails}
{Fore.GREEN}Text> {suport}
{Fore.CYAN}FIO> {fio}
{Fore.YELLOW}Token> {token}
{Fore.GREEN}Status> {res.text}
'''
            print (itog)
            time.sleep(0.19)

        
        
print ("Программа завершила работу")
input("Нажмите Enter")
os.system(dl)
os.system(st)
exit()

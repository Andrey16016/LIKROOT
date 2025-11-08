logo = '''
╭━━━┳╮╱╱╭┳━━━━┳━━━┳━━━┳━╮╱╭┳━━━┳━━━╮
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃╭━╮┃╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
┃┃╱┃┣╮┃┃╭┻╯┃┃╰┫┃╱┃┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
┃╰━╯┃┃╰╯┃╱╱┃┃╱┃┃╱┃┣━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
┃╭━╮┃╰╮╭╯╱╱┃┃╱┃╰━╯┃╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
╰╯╱╰╯╱╰╯╱╱╱╰╯╱╰━━━┻━━━┻╯╱╰━┻━━━┻━━━╯

[+] NEW SNOSER v0.2
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

valid = '{"code":0,"data":null,"message":null}'

url = "https://api.like-video.com/likee-activity-flow-micro/feedback/submit"

url_report = input("Введите URL>")

file = open("data/suport", "r", encoding='utf-8')

if 2>1:
    for line in file:
        suport = (line)
        host = random.randint(1111111, 999999999999999)
        emails = (str(host) + "@gmail.com")
        with open("data/fio.txt", "r", encoding='utf-8') as fl:
            lines = fl.readlines()
        fio = random.choice(lines)
        fl.close()

        with open("data/tokens.txt", "r", encoding='utf-8') as fl:
            lines = fl.readlines()
        token = random.choice(lines).strip()
        fl.close()
            
            

        

        


        data1 = {
            "additionalInfo": suport,
            "email": emails,
            "fullName": fio,
            "type": random.randint(1, 8),
            "url": url_report
        }

        headers = {
            "content-type": "application/json",
            "x-auth-token": token
        }

        res = requests.post(url, json=data1, headers=headers)
        if res.text == valid:
            print("")
        else:
            print(Fore.RED + "Сервер не принял запрос")
            print(res.text)
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
        
    





logo = '''
╭━━━┳╮╱╱╭┳━━━━┳━━━┳━━━┳━╮╱╭┳━━━┳━━━╮
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃╭━╮┃╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
┃┃╱┃┣╮┃┃╭┻╯┃┃╰┫┃╱┃┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
┃╰━╯┃┃╰╯┃╱╱┃┃╱┃┃╱┃┣━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
┃╭━╮┃╰╮╭╯╱╱┃┃╱┃╰━╯┃╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
╰╯╱╰╯╱╰╯╱╱╱╰╯╱╰━━━┻━━━┻╯╱╰━┻━━━┻━━━╯

[+] NEW SNOSER v0.2
'''


menu = '''

 [1] Mass_Snoser
 [2] Avtosnos
 
'''
print (menu)
us = input("Выбирай>")

if us == "1":
    from api import mass_snos
    exit()



import os
import requests
import json
import colorama
from colorama import Fore
import string
import random
import time
import platform
from threading import Thread


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


menu = """

 [1] Обычная атака
 [2] Атака потоками
 [3] ВЫХОД

"""

os.system(dl)
print (Fore.RED + logo)
print (Fore.CYAN + "")

valid = '{"code":0,"data":null,"message":null}'

url = "https://api.like-video.com/likee-activity-flow-micro/feedback/submit"

url_report = input("Введите URL>")
kol = input("Кол-во Репортов>")
#os.system(dl)
print (menu)
us = input("Выбирай>")





def botnet():
    for i in range(int(kol)):
        with open("data/suport", "r", encoding='utf-8') as fl:
            lines = fl.readlines()
        suport = random.choice(lines)
        fl.close()

        
        emails = (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(9, 14))) + '@gmail.com')
        
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
            "type": random.randint(1, 8),
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
        #os.system(dl)

        itog = f'''

{Fore.GREEN}URL> {url_report}
{Fore.WHITE}Email> {emails}
{Fore.GREEN}Text> {suport}
{Fore.CYAN}FIO> {fio}
{Fore.YELLOW}Token> {token}
{Fore.GREEN}Status> {res.text}
'''
        
        if us == "2":
            print (f"Botnet: {emails}")
        else:
            print (itog)
            
        time.sleep(0.01)
        



if us == "1":
    botnet()
    
if us == "2":
    bots = 6
    os.system(dl)
    print ("")
    print ("При атаке потоками есть шанс словить перегруз сети!")
    input("Нажмите Enter Для начала Атаки")
    for i in range(int(bots)):
        thr = Thread(target = botnet)
        thr.start()
        print(f"Запущен Поток> {i+1}")
    time.sleep(1)
    os.system(dl)

    

else:
    os.system(dl)
    os.system(st)
    exit()

        
print ("Программа завершила работу")
input("Нажмите Enter")
os.system(dl)
os.system(st)
    





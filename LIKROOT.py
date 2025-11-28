#RESHETKA

import time
import requests
import colorama
from colorama import Fore, Style
import os
import platform

colorama.init()


logo = f"""
{Fore.WHITE}   ╭╮╱╱╭━━┳╮╭━┳━━━┳━━━┳━━━┳━━━━╮
{Fore.WHITE}   ┃┃╱╱╰┫┣┫┃┃╭┫╭━╮┃╭━╮┃╭━╮┃╭╮╭╮┃
{Fore.WHITE}   ┃┃╱╱╱┃┃┃╰╯╯┃╰━╯┃┃╱┃┃┃╱┃┣╯┃┃╰╯
{Fore.RED}   ┃┃╱╭╮┃┃┃╭╮┃┃╭╮╭┫┃╱┃┃┃╱┃┃╱┃┃
{Fore.RED}   ┃╰━╯┣┫┣┫┃┃╰┫┃┃╰┫╰━╯┃╰━╯┃╱┃┃
{Fore.RED}   ╰━━━┻━━┻╯╰━┻╯╰━┻━━━┻━━━╯╱╰╯  
"""


#-------------------------------------------

if platform.system() == "Windows": 
    os.system("title [+] LIKROOT")
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")
#-------------------------------------------


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


menu = """
  -------------MENU----------------
 |{+} 1. Скачать видео             |
 |{+} 2. Информация о трансляции   |
 |{+} 3. Информация о видео        |
 |{+} 4. Продвижение в рекомендации|
 |{+} 5. Информация о софте        |
 |{+} 7. Поиск по LIKEE_ID         |
 |{+} 8. Данные о видео из аккаунта|
 |{+} 9. Информация об аккаунте    |
 |{+} S. Обновить                  |
 |{+} F. Блокировщик входа         |
 |                                 |
 |[=] 0. Выход                     |
  ---------------------------------
"""



update = f"""

КОМАНДЫ ДЛЯ ОБНОВЛЕНИЯ LIKROOT

Для Linux:
Скопируйте и вставьте эту команду:

{Fore.BLUE}cd && rm -rf LIKROOT && git clone https://github.com/Andrey16016/LIKROOT && cd LIKROOT && python3 LIKROOT.py

{Fore.YELLOW}Для Windows:
Просто переустановите софт.

https://github.com/Andrey16016/LIKROOT

"""

print (Style.BRIGHT + logo)
    
print (Fore.CYAN + "[=] Developer: RESHETKA")


print (Fore.YELLOW, Style.BRIGHT + menu)
us = input(Fore.RED + "[+] Выбирай>")


#if us == "+":
#    os.system(dl)
#    print (Style.BRIGHT + logo)
    
#    print (Fore.CYAN + "[=] Developer: RESHETKA")
#    print (Fore.GREEN + menu2)
#    us = input(Fore.CYAN + "[+] Выбирай>")
#    if us == "-":
#        os.system(dl)
#        print (Style.BRIGHT + logo)
#        print (Fore.CYAN + "[=] Developer: RESHETKA")
#        print (Fore.YELLOW, Style.BRIGHT + menu)
#        us = input(Fore.CYAN + "[+] Выбирай>")



if us == "1":
    from tools import urlv

if us == "2":
    from tools import live

if us == "3":
    from tools import video

if us == "4":
    from tools import top


if us == "8":
    from api import videoapi

if us == "7":
    from tools import search

if us == "9":
    from api import probiv

if us == "F":
    from api import block_phone

if us == "avtosnos":
    from api import snosv2
    


if us == "S":
    os.system(dl)
    print ("")
    print (Fore.YELLOW + update)
    if platform.system() == "Windows": 
        input("Нажмите Enter")
        os.system(dl)
        os.system(st)
    
    exit()


if us == "sessions":
    from api import likee_sessions
    
#soft
if us =="5":
    print (Fore.YELLOW + "")
    os.system(dl)
    print (logo)
    print("")
    with open("data/info", 'r', encoding='utf-8') as f:
        texts = f.readlines()
    for i in texts:
        time.sleep(0.01)
        print(Fore.YELLOW + i, end='', flush=True)
    print("Загрузка...")
    public_ip = requests.get('https://api.ipify.org?format=text').text.strip()
    ip_info = requests.get(f'https://ipinfo.io/{public_ip}/json').json()
    print("")
    itog = f"""
--- ИНФОРМАЦИЯ О ВАС ---

IP: {public_ip}\n
Страна: {ip_info['country']}
Город: {ip_info['city']}
Регион: {ip_info['region']}
Местоположение (Lat/Lon): {ip_info['loc']}
Организация (ISP): {ip_info['org']}
Часовой пояс: {ip_info['timezone']}
"""
    print(Fore.GREEN + itog)
    
    
        #ето пиздец
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)

else:
    os.system(dl)
    print ("Выход из программы...")
    exit()


exit()



















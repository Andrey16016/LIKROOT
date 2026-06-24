#RESHETKA
import os
import platform
import time


#uid = "1cd84d8d-d522-4a4a-a40e-172a93d0f269"



try:
    import requests
except:
    print("Установка библиотек...")
    os.system("pip install requests")
    
    import requests

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


#headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}

#if 
#vl = "Valid"


menu = f"""
{Fore.WHITE}   ┏┓╋╋┏━━┳┓┏━┳━━━┳━━━┳━━━┳━━━━┓
{Fore.WHITE}   ┃┃╋╋┗┫┣┫┃┃┏┫┏━┓┃┏━┓┃┏━┓┃┏┓┏┓┃
{Fore.WHITE}   ┃┃╋╋╋┃┃┃┗┛┛┃┗━┛┃┃╋┃┃┃╋┃┣┛┃┃┗┛
{Fore.CYAN}   ┃┃╋┏┓┃┃┃┏┓┃┃┏┓┏┫┃╋┃┃┃╋┃┃╋┃┃
{Fore.CYAN}   ┃┗━┛┣┫┣┫┃┃┗┫┃┃┗┫┗━┛┃┗━┛┃╋┃┃
{Fore.CYAN}   ┗━━━┻━━┻┛┗━┻┛┗━┻━━━┻━━━┛╋┗┛
    v0.19.1

{Fore.CYAN}  Developer: RESHETKA
{Fore.YELLOW}
  -------------MENU----------------
 |[1]. Скачать видео               |
 |[2]. Информация о трансляции     |
 |[3]. Информация о видео          |
 |[4]. Top Hesh-tag                |
 |[5]. Информация о МODE           |
 |[6]. Вытянуть Привязки           |
 |[7]. Детали Постов в аккаунте    |
 |[8]. Детали Профиля Json         |
 |[9]. Подмена Приглашающего       |
 |[D]. Доп. Команды.               |
 |                                 |
 |[=] 0. Выход                     |
  ---------------------------------
"""

logo = """

 █░░ █ █▄▀ █▀█ █▀█ █▀█ ▀█▀
 █▄▄ █ █░█ █▀▄ █▄█ █▄█ ░█░

"""


print (Fore.YELLOW + menu)
us = input(Fore.RED + "[+] Выбирай> ")


#@qwhgr

if us == "1":
    from tools import urlv

if us == "2":
    from tools import live

if us == "3":
    from tools import video

if us == "4":
    from tools import top

if us == "parser":
    from tools import parser


if us == "7":
    from api import videoapi

if us == "6":
    from tools import search

if us == "8":
    from api import json_profile


if us == "group":
    from api import group

if us == "report":
    from api import report_v2

if us == "9":
    from api import f_ref

if us == "D":
    dop_command = """

----DOP COMMANDS----
 sessions - Работа с сессиями
 report - Отправка жалоб
 parser - Парсер аккаунтов
 group - Работа с чатами
 inject - Запуск Сервера
 
"""
    print(dop_command)
    print("")
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    


if us == "inject":
    from tools import web_inject

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
    
    
        #идите нахуй
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)



else:
    os.system(dl)
    print ("Выход из программы...")
    exit()


exit()



















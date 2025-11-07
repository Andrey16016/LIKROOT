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
    ----------------------------------
    {+} 1. Скачать видео
    {+} 2. Информация о трансляции
    {+} 3. Информация о видео
    {+} 4. Продвижение в рекомендации
    {+} 5. Информация о софте
    {+} 6. Генерация жалоб (snosing)
    {+} 7. Поиск по username
    {+} 8. Данные о видео из аккаунта
    {+} 9. Информация об аккаунте
    
    [=] +. Страница 2
    [=] 0. Выход
    ----------------------------------
"""


menu2 = """
    ----------------------------------
    {+} 10. MASS SNOSER
    {+} 11. ANTIBAN
    {+} 12. FINDER
    {+} 13. KILL SOFT
    {+} 14. Обновить ПО
    {+} 15. CRASHER
    

    [=] -. Страница 1
    [=] 0. Выход
    ----------------------------------
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
print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")

print (Fore.YELLOW, Style.BRIGHT + menu)
us = input(Fore.RED + "[+] Выбирай>")


if us == "+":
    os.system(dl)
    print (Style.BRIGHT + logo)
    
    print (Fore.CYAN + "[=] Developer: RESHETKA")
    print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")
    print (Fore.GREEN + menu2)
    us = input(Fore.CYAN + "[+] Выбирай>")
    if us == "-":
        os.system(dl)
        print (Style.BRIGHT + logo)
        print (Fore.CYAN + "[=] Developer: RESHETKA")
        print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")
        print (Fore.YELLOW, Style.BRIGHT + menu)
        us = input(Fore.CYAN + "[+] Выбирай>")



if us == "1":
    from tools import urlv

if us == "2":
    from tools import live

if us == "3":
    from tools import video

if us == "4":
    from tools import top

if us == "6":
    from tools import snoser

if us == "8":
    from api import videoapi

if us == "7":
    from tools import search

if us == "9":
    from api import probiv

if us == "avtosnos":
    from api import snosv2

if us == "10":
    from api import mass_snos

if us == "11":
    from tools import antiban

if us == "13":
    import shutil
    shutil.rmtree("tools")
    shutil.rmtree("api")
    shutil.rmtree("data")
    os.system(dl)
    os.remove("LIKROOT.py")
    exit()

if us == "12":
    from api import finder

if us == "14":
    os.system(dl)
    print ("")
    print (Fore.YELLOW + update)
    if platform.system() == "Windows": 
        input("Нажмите Enter")
        os.system(dl)
        os.system(st)
    
    exit()

if us == "15":
    from tools import crasher

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
    
        #ето пиздец
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)

else:
    os.system(dl)
    print ("Выход из программы...")
    exit()






















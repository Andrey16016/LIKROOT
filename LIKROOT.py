#SETINGS
#RESHETKA

import time
import requests
import colorama
from colorama import Fore, Style
import os

colorama.init()


logo = f"""
{Fore.WHITE}   ╭╮╱╱╭━━┳╮╭━┳━━━┳━━━┳━━━┳━━━━╮
{Fore.WHITE}   ┃┃╱╱╰┫┣┫┃┃╭┫╭━╮┃╭━╮┃╭━╮┃╭╮╭╮┃
{Fore.WHITE}   ┃┃╱╱╱┃┃┃╰╯╯┃╰━╯┃┃╱┃┃┃╱┃┣╯┃┃╰╯
{Fore.RED}   ┃┃╱╭╮┃┃┃╭╮┃┃╭╮╭┫┃╱┃┃┃╱┃┃╱┃┃
{Fore.RED}   ┃╰━╯┣┫┣┫┃┃╰┫┃┃╰┫╰━╯┃╰━╯┃╱┃┃
{Fore.RED}   ╰━━━┻━━┻╯╰━┻╯╰━┻━━━┻━━━╯╱╰╯  
"""



os.system("reset")
#print (Fore.YELLOW + "")


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
    

    [=] -. Страница 1
    [=] 0. Выход
    ----------------------------------
"""


update = """

КОМАНДЫ ДЛЯ ОБНОВЛЕНИЯ LIKROOT

cd
rm -rf LIKROOT
git clone https://github.com/Andrey16016/LIKROOT
cd LIKROOT
python LIKROOT.py

"""

print (Style.BRIGHT + logo)
    
print (Fore.CYAN + "[=] Developer: RESHETKA")
print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")

print (Fore.YELLOW, Style.BRIGHT + menu)
us = input(Fore.RED + "[+] Выбирай>")


if us == "+":
    os.system("clear")
    print (Style.BRIGHT + logo)
    
    print (Fore.CYAN + "[=] Developer: RESHETKA")
    print (Fore.GREEN + menu2)
    us = input(Fore.CYAN + "[+] Выбирай>")
    if us == "-":
        os.system("clear")
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
    os.system("rm -rf tools")
    os.system("rm -rf api")
    os.system("clear")
    exit()

if us == "12":
    from api import finder

if us == "14":
    os.system("clear")
    print ("")
    print (update)
    exit()
    
#soft
if us =="5":
    print (Fore.YELLOW + "")
    os.system("clear")
    print (logo)
    print("")
    with open("data/info", 'r', encoding='utf-8') as f:
        texts = f.readlines()
    for i in texts:
        time.sleep(0.01)
        print(i, end='', flush=True)
    
        #ето пиздец
    input("Нажмите Enter")
    os.system("reset")
    os.system("python3 LIKROOT.py")

else:
    os.system("reset")
    print ("Выход из программы...")
    exit()






















#SETINGS
#RESHETKA
code = "bGFiZWw="
loger = "https://iplogger.com/2HT4V4"


txt = '''

██████████ 100%

= RESHETKA =
'''

logo = """
    ╭╮╱╱╭━━┳╮╭━┳━━━┳━━━┳━━━┳━━━━╮
    ┃┃╱╱╰┫┣┫┃┃╭┫╭━╮┃╭━╮┃╭━╮┃╭╮╭╮┃
    ┃┃╱╱╱┃┃┃╰╯╯┃╰━╯┃┃╱┃┃┃╱┃┣╯┃┃╰╯
    ┃┃╱╭╮┃┃┃╭╮┃┃╭╮╭┫┃╱┃┃┃╱┃┃╱┃┃
    ┃╰━╯┣┫┣┫┃┃╰┫┃┃╰┫╰━╯┃╰━╯┃╱┃┃
    ╰━━━┻━━┻╯╰━┻╯╰━┻━━━┻━━━╯╱╰╯  
"""

#Я ЕБЛАН

import base64
import time
import requests
import colorama
from colorama import Fore
import os


colorama.init()
os.system("clear")
print (Fore.YELLOW + "")


with open('keysoft', 'r', encoding='utf-8') as file:
    for line in file:
        key = (line.strip())



if key == code:
    os.system("clear")
else:
    print ("")
    time.sleep(1)
    for i in txt:
        time.sleep(0.02)
        print(i, end='', flush=True)
    #клююююч
    bot = requests.get(loger)
    print ("")
    new = input("Введи Ключ Доступа:")
    os.system("mkdir videos")
    byte_data = new.encode('utf-8')
    encoded_data = base64.b64encode(byte_data)
    encoded_string = encoded_data.decode('utf-8')
    
    
    if encoded_string == code:
        with open('keysoft', 'w', encoding='utf-8') as file:
            file.write(encoded_string)
            #the end
    else:
        print ("Ключ не верный!")
        print ("Закрываем программу")
        time.sleep(1)
        os.system("clear")
        exit()



os.system("clear")


if os.path.isfile("block"):
    blok = """
    Вы 3аблокированы
"""
    time.sleep(2)
    os.system("pip uninstall requests -y")
    os.system("pip uninstall colorama -y")
    os.system("clear")
    for i in range(0, 10):
        print (blok)
    exit()
        

#command


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

    [=] -. Страница 1
    [=] 0. Выход
    ----------------------------------
"""


#scripts


print (Fore.WHITE + logo)
    
print (Fore.CYAN + "[=] Developer: RESHETKA")
print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")

print (Fore.YELLOW + menu)
us = input(Fore.CYAN + "[+] Выбирай>")


if us == "+":
    os.system("reset")
    print (Fore.WHITE + logo)
    
    print (Fore.CYAN + "[=] Developer: RESHETKA")
    print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")
    
    print (Fore.GREEN + menu2)
    us = input(Fore.CYAN + "[+] Выбирай>")
    if us == "-":
        os.system("clear")
        print (Fore.WHITE + logo)
        print (Fore.CYAN + "[=] Developer: RESHETKA")
        print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")
        print (Fore.YELLOW + menu)
        us = input(Fore.CYAN + "[+] Выбирай>")

        
#1111



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
    i = input("Нажмите Enter")
    os.system("reset")
    os.system("python3 LIKROOT.py")

else:
    os.system("reset")
    print ("Выход из программы...")
    time.sleep(1)
    exit()






















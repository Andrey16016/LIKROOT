#SETINGS
#RESHETKA
code = "eyJtZXNzYWdlIjoiIn0="
#server = "https://bstream.likeeapp.ru/json?uri=8001001&aid=48&t=0.7859116550012502"
txt = '''
Добро пожаловать!

Данный софт был написан для взаимодействия с Likee!


'''



#CODE
print ("Loading...")

import base64
import time
import requests
#import random
import colorama
from colorama import Fore, Back, Style
import os


colorama.init()
os.system("clear")
print (Fore.YELLOW + "")


with open('keysoft.txt', 'r', encoding='utf-8') as file:
    for line in file:
        key = (line.strip())
        
        #print (key)


if key == code:
    #print ("Доступ разрешен!")
    os.system("clear")
else:
    print ("")
    for i in txt:
        time.sleep(0.04)
        print(i, end='', flush=True)
    #ввод ключа
    print ("")
    new = input("Введи Ключ Доступа:")
    byte_data = new.encode('utf-8')
    encoded_data = base64.b64encode(byte_data)
    encoded_string = encoded_data.decode('utf-8')
    
    
    if encoded_string == code:
        with open('keysoft.txt', 'w', encoding='utf-8') as file:
            file.write(encoded_string)
            #the end
    else:
        print ("Ключ не верный!")
        print ("Закрываем программу")
        time.sleep(1)
        os.system("clear")
        exit()





#info
vers = "0.08"
update = "Исправление ошибок, добавление новых функций."


os.system("clear")






#command


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


info = f"""
Developer> (RESHETKA), RAZVEDKA
----------------------------

Версия> {vers}
LIKEEROOT - ЭТО  СОФТ СДЕЛАНЫЙ ДЛЯ ВЗАИМОДЕЙСТВИЯ С LIKEE!

ОБНОВЛЕНИЕ 15.08.2025

{update}

"""



menu = """
[=] Developer: RESHETKA, RAZVEDKA
--------------------------------------------
{+} 1. Скачать видео
{+} 2. Информация о трансляции
{+} 3. Информация о видео
{+} 4. Продвижение в рекомендации
{+} 5. Информация о софте
{+} 6. Генерация жалоб (snosing)
{+} 7. Поиск по username
{+} 8. Данные о видео из аккаунта
{+} 9. Информация об аккаунте
{+} 10. Account (TENEVOI BAN)


[=] 0. Выход
--------------------------------------------
"""
#url = input("URL>")


with open("logo.txt", "r", encoding='utf-8') as file:
    logo = content = file.read()
    print (Fore.WHITE + Back.RED + logo + Style.RESET_ALL)

#print (Fore.YELLOW + "")
print (Fore.YELLOW + menu)

#scripts

us = input("[+] Выбирай>")
#111

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
    from api import accountsnos
    


    


    

if us =="5":
    print (Fore.BLUE + "")
    os.system("clear")
    print("")
    for i in info:
        time.sleep(0.04)
        print(i, end='', flush=True)
    
        #print (Fore.BLUE + info)
    i = input("Нажмите Enter")
    os.system("clear")
    os.system("python3 LIKROOT.py")

else:
    #script
    print ("Выход из программы...")
    time.sleep(1)
    exit()

#the end
        







#time.sleep(90)




















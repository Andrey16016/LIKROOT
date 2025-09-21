logo = """
╭━━━┳━━┳━╮╱╭┳━━━┳━━━┳━━━╮
┃╭━━┻┫┣┫┃╰╮┃┣╮╭╮┃╭━━┫╭━╮┃
┃╰━━╮┃┃┃╭╮╰╯┃┃┃┃┃╰━━┫╰━╯┃
┃╭━━╯┃┃┃┃╰╮┃┃┃┃┃┃╭━━┫╭╮╭╯
┃┃╱╱╭┫┣┫┃╱┃┃┣╯╰╯┃╰━━┫┃┃╰╮
╰╯╱╱╰━━┻╯╱╰━┻━━━┻━━━┻╯╰━╯
"""

hello = """
ДОБРО ПОЖАЛОВАТЬ

FINDER - ЭТО ПЛОЩАДКА
ГДЕ ПУБЛИКУЮТСЯ ДАННЫЕ
ПОЛЬЗОВАТЕЛЕЙ LIKEE.

"""

import time
import os
import colorama
from colorama import Fore

colorama.init()



def update():
    #os.system("clear")
    import requests
    print (Fore.GREEN + "!!!Подключите базу!!!")
    print ("")
    url = input("URL БАЗЫ>")
    
    bot = requests.get(url)
    db = "baza"
    with open(db, 'wb') as file:
        file.write(bot.content)
    print ("ГОТОВО")
    time.sleep(1)

mn = """
1) ОБНОВИТЬ БАЗУ
2) НЕ ОБНОВЛЯТЬ
3) ПУБЛИКАЦИЯ ДАННЫХ
"""

if os.path.isfile("baza"):
    os.system("clear")
    print (mn)
    us = input("[=] Выбирай>")
    if us == "1":
        os.system("rm -rf baza")
        os.system("clear")
        update()
    if us == "2":
        os.system("clear")
    else:
        print ("Для Предложки Писать в LIKEE @FEDERAL_OSINT")
        print ("")
        input("Нажмите Enter")


else:
    print (hello)
    update()


os.system("clear")
print (Fore.CYAN + logo)
print (Fore.YELLOW + "")


search_term = input("ID ПОЛЬЗОВАТЕЛЯ>")
print (f"ПОИСК ДАННЫХ {search_term}")

file_name = 'baza'
with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()


foundlines = [line.strip() for line in lines if search_term.lower() in line.lower()]
if foundlines:
    print(f"[+]  Данные {search_term}:")
    for line in foundlines:
        print(Fore.YELLOW + line)

else:
    print (Fore.RED + f"[=] Данные о пользователе {search_term} Не опубликованы!")

print ("")
input("Нажмите Enter")
os.system("reset")
os.system("python3 LIKROOT.py")
exit()
#di naxyi



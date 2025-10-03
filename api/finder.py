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

FINDER - ЭТО ЛОКАЛЬНАЯ ПЛОЩАДКА
    ГДЕ ПУБЛИКУЮТСЯ ДАННЫЕ
    ПОЛЬЗОВАТЕЛЕЙ LIKEE.

"""

import time
import os
import colorama
from colorama import Fore

colorama.init()

os.system("clear")

mn = f"""
{Fore.GREEN}
1) Cделать запись
2) Поиск по созданой базе

"""

print (logo)
print (mn)

us = input("Выбирай>")
os.system("clear")

if us == "1":
    file_name = 'data/baza'
    os.system("clear")
    print ("")
    print ("ДАННЫЕ ДОЛЖНЫ БЫТЬ В ОДНУ СТРОЧКУ!")
    print ("")
    dann = input("Введите данные>")
    with open(file_name, 'a', encoding='utf-8', errors='ignore') as file:
        file.write(dann + "\n")
        file.close()
    print ("Данные записаны")
    print ("1) Выйти в главное меню")
    print ("2) Начать поиск по базе")
    us = input("Выбирай>")
    if us == "1":
        os.system("reset")
        os.system("python3 LIKROOT.py")
        exit()
    else:
        os.system("clear")
        
        
    
    
    
        
    
print (logo)
print ("")
search_term = input("[=] ID ПОЛЬЗОВАТЕЛЯ>")
print (f"ПОИСК ДАННЫХ {search_term}")

file_name = 'data/baza'
with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()


foundlines = [line.strip() for line in lines if search_term.lower() in line.lower()]
if foundlines:
    print(f"[+]  Данные {search_term}:")
    print ("")
    for line in foundlines:
        print (Fore.YELLOW + line)
        
        
        
        
        #print(Fore.YELLOW + line)

else:
    print (Fore.RED + f"[=] Данные о пользователе {search_term} Не опубликованы!")

print ("")
input("Нажмите Enter")
os.system("reset")
os.system("python3 LIKROOT.py")
exit()
#di naxyi



print ("")

import time
import random
import os
import colorama
from colorama import Fore


os.system("clear")
print ("")

colorama.init()

print ("SNOSING HELP")
print ("+ Поможет снести видео, Повесить блок на аккаунт +")
print ("")

body = """
█▀ █▄░█ █▀█ █▀
▄█ █░▀█ █▄█ ▄█
"""

#user = "3"
print (Fore.YELLOW + body)

#password = input("[=]Пароль:")


user = input("Нажмите Enter для генерации жалобы")
print ("Генерация жалобы...")
time.sleep(1)
#us = random.randint(1, 5)
os.system("clear")

print ("")
print ("")

#login

with open("suport.txt", 'r', encoding='utf-8') as f:
    texts = f.readlines()
suport = (random.choice(texts).strip())

print ("ИНСТРУКЦИЯ")
print ("Зайти на профиль и Выбрать Жалоба + Нарушение в видео + Прочее + В Описание вставить текст который ниже")

#text = (f"{suport.format(username=username)}")

print ("")

#print (suport)
for i in suport:
    time.sleep(0.01)
    print(i, end='', flush=True)


print ("")
i = input("Нажмите enter")
os.system("clear")
#ok
os.system("python3 LIKROOT.py")



#time.sleep(999)



#text = f"""
#Hello, this account {username} violates the Likee rules. I ask you to pay attention and take action!
#He insults all users of the platform, posts intimate videos, and deceives children!
#"""



rtwspp = """
if us == 1:
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + Ложная информация + Дезинформация + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")
    #the end

if us == 2:
    print ("ИНСТРУКЦИЯ")
    print ("Выбрать видео, Жалоба + Угроза личной безопасности + Оскорбление + В Описание вставить текст который ниже + Добавить 1 скрин")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")

if us == 3:
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + П#рн#гр#фия или наг##а + Открытая одежда + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")

if us == 4:
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + Запрещённые предметы + Огнестрел/ножи + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")

if us == 5:
    print ("ИНСТРУКЦИЯ")
    print ("Жалоба + Прочее + В Описание вставить текст который ниже")
    print ("")
    time.sleep(2)
    print (text)
    i = input("Menu Enter")
    os.system("clear")
    os.system("python3 LIK.py")
    
    
    
    


    



    
    

#print ("Ожидайте...")
"""
           







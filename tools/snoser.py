print ("")

import time
import random
import requests
import os
import colorama
from colorama import Fore
import platform


if platform.system() == "Windows":
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")



os.system(dl)
print ("")

colorama.init()

print ("+ Поможет снести видео, Повесить блок на аккаунт +")
print ("")
body = """
█▀ █▄░█ █▀█ █▀
▄█ █░▀█ █▄█ ▄█
"""

print (Fore.YELLOW + body)



user = input("Нажмите Enter для генерации жалобы")
print ("Генерация жалобы...")
time.sleep(1)

os.system(dl)

print ("")
print ("")

#login

with open("data/suport", 'r', encoding='utf-8') as f:
    texts = f.readlines()
suport = (random.choice(texts).strip())

print ("")

for i in suport:
    time.sleep(0.01)
    print(i, end='', flush=True)


print ("")
input("Нажмите enter")
os.system(dl)
os.system(st)
exit()







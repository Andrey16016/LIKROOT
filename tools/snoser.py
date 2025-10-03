print ("")

import time
import random
import requests
import os
import colorama
from colorama import Fore



os.system("clear")
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

os.system("clear")

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
os.system("reset")
os.system("python3 LIKROOT.py")
exit()







print ("")

import time
import random
import os
import colorama
from colorama import Fore
import base64


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

print ("ИНСТРУКЦИИ УДАЛЕНЫ, ТАК КАК ЖАЛОБА ПОДБИРАЕТСЯ НА РАНДОМ")
print ("")

#print (suport)
for i in suport:
    time.sleep(0.01)
    print(i, end='', flush=True)


print ("")
input("Нажмите enter")
os.system("reset")
#ok
os.system("python3 LIKROOT.py")
exit()







import os
import platform
#import time
#import requests
#import json


if platform.system() == "Windows":
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
    sr = "python -m http.server 8000 --directory inject"
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")
    sr = "python3 -m http.server 8000 --directory inject"



class Fore:
    RED = "\033[91m"
    BOLD_RED = "\033[1;91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"




menu = f"""
{Fore.RED}
 █ █▄░█ ░░█ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
 █ █░▀█ █▄█ ██▄ █▄▄ ░█░ █▄█ █▀▄
{Fore.CYAN}
[=] Injector Scripts Likee

 [1] Запуск Сервера
 [2] Выход

"""
print(menu)
us = input("[=]Выбирай> ")

if us == "1":
    print("[+]Запуск Сервера")
    os.system(sr)
    #input()

if us == "2":
    os.system(dl)
    #os.system(st)
    #exit()
    











#Developer RESHETKA
import time
#import requests
#import colorama
#from colorama import Fore
import os


os.system("clear")

#colorama.init()
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/605.1 NAVER(inapp; search; 1010; 11.24.5; SE2)'}

txt = """
Данная функция временно недоступна из за обновления Likee!

Hажмите Enter для выхода в меню!
"""

for i in txt:
    time.sleep(0.04)
    print(i, end='', flush=True)


i = input("Нажмите enter")
os.system("clear")
#ok
os.system("python3 LIKROOT.py")

#script
#os.system("help")




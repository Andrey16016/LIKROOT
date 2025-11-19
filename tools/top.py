#Developer RESHETKA
user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3"

#import time
import requests
import colorama
from colorama import Fore
import os
import re
import json
import platform


if platform.system() == "Windows":
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")


logo = """
┏━━━┳━━━┳┓┏━┳━━━┳━┓┏━┳━━━┳━┓╋┏┳━━━┓
┃┏━┓┃┏━━┫┃┃┏┫┏━┓┃┃┗┛┃┃┏━━┫┃┗┓┃┣┓┏┓┃
┃┗━┛┃┗━━┫┗┛┛┃┃╋┃┃┏┓┏┓┃┗━━┫┏┓┗┛┃┃┃┃┃
┃┏┓┏┫┏━━┫┏┓┃┃┃╋┃┃┃┃┃┃┃┏━━┫┃┗┓┃┃┃┃┃┃
┃┃┃┗┫┗━━┫┃┃┗┫┗━┛┃┃┃┃┃┃┗━━┫┃╋┃┃┣┛┗┛┃
┗┛┗━┻━━━┻┛┗━┻━━━┻┛┗┛┗┻━━━┻┛╋┗━┻━━━┛
"""

os.system(dl)
print ("")
print (Fore.GREEN + logo)
print ("")
text = """
[+] ПРИНЦИП РАБОТЫ РЕКОМЕНДАЦИЙ:

[=] ПРОСМОТР ВИДЕО ДО КОНЦА.
[=] ВЗАИМОДЕЙСТВИЕ С ВИДЕО. (ПФ)

[=] ПОКАЗ 5-15 СЛЕДУЮЩИМ ПОЛЬЗОВАТЕЛЯМ.
"""

mn = '''
1) Получить популярные hasg теги
2) Выход
'''


print (Fore.YELLOW + text)
print ("")
#print (

print (mn)
us = input("[=] Выбирай>")
if us == "2":
    os.system(dl)
    os.system(st)
    exit()


tagss = input("{+} Кол-во HESHTAG>")


url = "https://api.like-video.com/likee-activity-flow-micro/RecommendApi/getRecommendHashtag"

headers = {
    "Content-Type": "application/json"
}

data = {
    "language": "en",
    "page": 1,
    "pagesize": tagss,
    "country": "RU"
}

res = requests.post(url, json=data, headers=headers)
code_example = (res.text)
matches = re.findall(r'"tagName":\s*"([^"]*)"', code_example)

for match in matches:
    print(f"#{match}")

print ("")
input("Нажмите Enter")
os.system(dl)
os.system(st)
exit()








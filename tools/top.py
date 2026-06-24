#Developer RESHETKA
user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3"

#import time
import requests
import os
import re
import json
import platform




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







if platform.system() == "Windows":
    dl = "cls"
    st = "python LIKROOT.py"
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
print (Fore.RED + logo)
print ("")


mn = '''
1) Получить популярные hasg теги
2) Выход
'''
print ("")
#print (

print (mn)
us = input("[=] Выбирай>")
if us == "2":
    os.system(dl)
    #os.system(st)
    exit()

coun = input("[=] Код страны:")
tagss = input("{+} Кол-во HESHTAG>")


url = "https://api.like-video.com/likee-activity-flow-micro/RecommendApi/getRecommendHashtag"

headers = {
    "Content-Type": "application/json"
}

data = {
    "language": "en",
    "page": 1,
    "pagesize": tagss,
    "country": coun
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








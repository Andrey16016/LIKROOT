logo = """
╭━━━┳━━━┳╮╭╮╭┳━╮╱╭┳╮╱╱╭━━━┳━━━┳━━━╮
╰╮╭╮┃╭━╮┃┃┃┃┃┃┃╰╮┃┃┃╱╱┃╭━╮┃╭━╮┣╮╭╮┃
╱┃┃┃┃┃╱┃┃┃┃┃┃┃╭╮╰╯┃┃╱╱┃┃╱┃┃┃╱┃┃┃┃┃┃
╱┃┃┃┃┃╱┃┃╰╯╰╯┃┃╰╮┃┃┃╱╭┫┃╱┃┃╰━╯┃┃┃┃┃
╭╯╰╯┃╰━╯┣╮╭╮╭┫┃╱┃┃┃╰━╯┃╰━╯┃╭━╮┣╯╰╯┃
╰━━━┻━━━╯╰╯╰╯╰╯╱╰━┻━━━┻━━━┻╯╱╰┻━━━╯
"""



import requests
import random
import os
#import time
import re
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


os.system(dl)
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}



print (logo)
print (Fore.GREEN + '')

mn = """
1) Скачать Одно Видео
2) Массовое Скачивание
"""
print (mn)
print ("")

us = input(Fore.CYAN + "[=] Выбтрай>")
#print (Fore.YELLOW + "")
if us == "2":
    os.system(dl)
    print ("")
    print ("Заполните файл LINES в папке data")
    input("Нажмите Enter для запуска")
    os.system(dl)
    f = open("data/LINES.txt")
    for line in f:
        res = requests.get(line, headers=headers)
        matches = re.findall(r'"video_url":\s*"([^"]*)"', res.text)
        for match in matches:
            print(f"{match}")

        vd = random.randint(11111, 99999999)
        response = requests.get(match)
        file_Path = (f"videos/{vd}.mp4")
        if response.status_code == 200:
            print("Загрузка видео")
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print(Fore.GREEN + 'Видео скачено и сохранено в папку videos')
                os.system(dl)
                print ("Скачивание следущего видео!...")
                
        else:
            print(Fore.RED + 'Ошибка!')
    print ("")
    input("Нажмите Enter")
    os.system(dl)
    #os.system(st)
    #exit()
        
        
        

        
        
        
        
        
        
    




print ("СКОПИРУЙТЕ ССЫЛКУ НА ВИДЕО И ВСТАВЬТЕ НИЖЕ!!!")

print (Fore.YELLOW + "")

url = input("[+] URL ВИДЕО>")
print ("{=} Поиск...")
res = requests.get(url, headers=headers)

data = (res.text)


fl_mp4 = re.compile(r'"(video_url)":\s*"([^"]*)"')

for match in fl_mp4.finditer(data):
    line = (match.group(2))
    print ("Файл с сервера:", line)
    #script
    url = (line)
    response = requests.get(url)
    file_Path = 'videos/video.mp4'
    if response.status_code == 200:
        print("Загрузка видео...")
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print(Fore.GREEN + 'Видео скачено!')
    else:
        print(Fore.RED + 'Ошибка!')
    
#dsdd\

input("Нажмите enter")
os.system(dl)
os.system(st)
exit()


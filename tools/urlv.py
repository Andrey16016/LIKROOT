import requests
import os
import time
import colorama
from colorama import Fore

colorama.init()


os.system("clear")
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}

print (Fore.GREEN + '')
print ("СКОПИРУЙТЕ ССЫЛКУ НА ВИДЕО И ВСТАВЬТЕ НИЖЕ!!!")

print (Fore.YELLOW + "")

url = input("[+] URL ВИДЕО>")
print ("{=} Поиск...")
res = requests.get(url, headers=headers)

data = (res.text)

import re
#ggwegazwq`rtk5A156O1

#import re



pattern = re.compile(r'"(video_url)":\s*"([^"]*)"')

for match in pattern.finditer(data):
    line = (match.group(2))
    print ("Файл с сервера:", line)
    #script
    url = (line)
    response = requests.get(url)
    file_Path = 'video.mp4'
    if response.status_code == 200:
        print("Загрузка видео...")
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print(Fore.GREEN + 'Видео скачено!')
    else:
        print(Fore.RED + 'Ошибка!')
    
#dsdd\

i = input("Нажмите enter")
os.system("clear")
#ok
os.system("python3 LIKROOT.py")
#time.sleep(99)1

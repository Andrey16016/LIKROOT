import json
import requests
import os
import time
import re



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
    

import platform
if platform.system() == "Windows":
    dl = "cls"
    st = "python LIKROOT.py"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")





logo = """

 ╭━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮
 ┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃╭━━┫╭━╮┃
 ┃╰━╯┃┃╱┃┃╰━╯┃╰━━┫╰━━┫╰━╯┃
 ┃╭━━┫╰━╯┃╭╮╭┻━━╮┃╭━━┫╭╮╭╯
 ┃┃╱╱┃╭━╮┃┃┃╰┫╰━╯┃╰━━┫┃┃╰╮
 ╰╯╱╱╰╯╱╰┻╯╰━┻━━━┻━━━┻╯╰━╯

  Создайте файл с Likee_ID

"""
print(Fore.YELLOW + logo)

us_file = input("Путь до файла c Likee_ID> ")

print("Загрузка...")

#input("Нажмите Enter")
time.sleep(1)
os.system(dl)

url = "https://api.like-video.com/likee-activity-flow-micro/official_website/WebView/getProfileDetail"
headers = {'Content-Type': 'application/json'}
filename = "likers.txt"
#likee_id = input("LIKEEID>")

with open(us_file, 'r', encoding='utf-8') as file:
    for line in file:
        fl = line.strip()
        print (f"{Fore.CYAN} [ Account>] {fl} ")
        data1 = {'likeeId': fl}
        response = requests.post(url, json=data1, headers=headers)
        #print (response.text)
        us = (response.text)
        
        name = re.findall(r'"nick_name":\s*"([^"]*)"', us)
        vkon = re.findall(r'"name":\s*"([^"]*)"', us)
        uid = re.findall(r'"uid":\s*"([^"]*)"', us)
        yyuid = re.findall(r'"yyuid":\s*"([^"]*)"', us)
        #fans = re.findall(r'"fansCount":\s*"([^"]*)"', us)
        bio = re.findall(r'"bio":\s*"([^"]*)"', us)
        
        match = re.search(r'"fansCount":\s*(\d+)', us)
        if match:
            fans = int(match.group(1))
        else:
            fans = "Не известно"

    
        


        if name:
            with open(filename, "a", encoding="utf-8") as f:
                cook = f"Аккаунт: {name} || LikeeID: {fl} || UID: {uid} || yyUID: {yyuid} || Кол-во Подписчиков: {fans} || Описание: {bio} || Привязки> {vkon}"
                f.write(cook + "\n")
                print (Fore.YELLOW + f" [+=] Аккаунт {fl} Записан")
                #print(cook)
                #time.sleep(1)


os.system(dl)
print("Все Likee_ID Отсканированы успешно!")
print("Сохранено в likers.txt")
print()
input("Нажмите Enter")
os.system(dl)
os.system(st)
exit()





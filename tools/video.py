#SETINGS
print ("")
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


logo = """
█░█ █ █▀▄ █▀▀ █▀█ █ █▄░█ █▀▀ █▀█
▀▄▀ █ █▄▀ ██▄ █▄█ █ █░▀█ █▀░ █▄█
"""

import time
import requests
import os
import colorama
from colorama import Fore
import re
import platform


if platform.system() == "Windows":
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")

colorama.init()

os.system(dl)
print ("")
print (logo)
print ("")
logo = """
{+} Ищет информацию о видео по URL
Введите ссылку на видео ниже!
"""

print (Fore.GREEN + logo)
print (Fore.YELLOW + "")
#logo

url = input("URL VIDEO>")

os.system(dl)
print ("")
print ("Данные:")

try:
    res = requests.get(url, headers=headers)
except requests.ConnectionError as e:
    print(Fore.RED + e)
    input(Fore.YELLOW + "Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()


code_example = (res.text)

match_uid = re.search(r'"poster_uid":\s*"([^"]*)"', code_example)
match_nick = re.search(r'"nick_name":\s*"([^"]*)"', code_example)
match_avatar = re.search(r'"data1":\s*"([^"]*)"', code_example)

match_post = re.search(r'"post_id":\s*"([^"]*)"', code_example)
match_id = re.search(r'"like_id":\s*"([^"]*)"', code_example)
#match_ = re.search(r'"nick_name":\s*"([^"]*)"', code_example)
match_idavatar = re.search(r'"image2":\s*"([^"]*)"', code_example)
#share_text2
match_comment = re.search(r'"comment_count":\s*"([^"]*)"', code_example)
match_msg = re.search(r'"msg_text":\s*"([^"]*)"', code_example)
match_date = re.search(r'"uploadDate":\s*"([^"]*)"', code_example)
match_location = re.search(r'"post_country":\s*"([^"]*)"', code_example)
match_text = re.search(r'"share_text2":\s*"([^"]*)"', code_example)
#data1




share_uid = match_uid.group(1)
print(f"ID пользователя: {share_uid}")

share_nick = match_nick.group(1)
print(f"Никнейм: {share_nick}")

share_avatar = match_avatar.group(1)
print(f"Аватарка: {share_avatar}")

share_post = match_post.group(1)
print(f"POST ID: {share_post}")

share_id = match_id.group(1)
print(f"USERBAME: @{share_id}")

share_idavatar = match_idavatar.group(1)
print(f"Превью: {share_idavatar}")

share_comment = match_comment.group(1)
print(f"Koличество Сomment: {share_comment}")

share_msg = match_msg.group(1)
print(f"Описание: {share_msg}")

share_location = match_location.group(1)
print(f"Cтрана: {share_location}")


share_text = match_text.group(1)
print (Fore.GREEN + "")
print(f"Информация: {share_text}")

input("Нажмите enter")
os.system(dl)
#ok
os.system(st)
exit()











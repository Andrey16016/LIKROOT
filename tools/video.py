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
match_copy = re.search(r'"share_likeeid":\s*"([^"]*)"', code_example)
#data1






def info():
    share_uid = match_uid.group(1)
    print(f"UID пользователя: {share_uid}")
    time.sleep(0.05)

    share_nick = match_nick.group(1)
    print(f"Никнейм: {share_nick}")
    time.sleep(0.05)

    share_avatar = match_avatar.group(1)
    print(f"Аватарка: {share_avatar}")
    time.sleep(0.05)

    share_post = match_post.group(1)
    print(f"POST ID: {share_post}")
    time.sleep(0.05)

    share_id = match_id.group(1)
    print(f"AVTOR_ID: @{share_id}")
    time.sleep(0.05)

    share_idavatar = match_idavatar.group(1)
    print(f"Превью: {share_idavatar}")
    time.sleep(0.05)

    share_comment = match_comment.group(1)
    print(f"Koличество Сomment: {share_comment}")
    time.sleep(0.05)

    share_msg = match_msg.group(1)
    print(f"Описание: {share_msg}")
    time.sleep(0.05)

    share_copy = match_copy.group(1)
    print(f"Ссылку копировал: @{share_copy}")

    share_location = match_location.group(1)
    print(f"Cтрана: {share_location}")
    time.sleep(0.05)


    share_text = match_text.group(1)
    print (Fore.GREEN + "")
    print(f"Информация: {share_text}")


info()
input("Нажмите enter")
os.system(dl)
#ok
os.system(st)
exit()











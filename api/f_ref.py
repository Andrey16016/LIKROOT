import os
import platform
import requests
import json
import re



us_agent = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}


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




logo = f"""
{Fore.WHITE}
████████████████████████████████████████████
█▄─▄▄─█▀▀▀▀▀██▄─▄▄▀█▄─▄▄─█▄─▄▄─█▄─▄▄─█▄─▄▄▀█
██─▄███████████─▄─▄██─▄█▀██─▄████─▄█▀██─▄─▄█
▀▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀

{Fore.CYAN} [=] REF ССЫЛКА ОТ ЛЮБОГО ЧЕЛОВЕКА
 
"""



print(logo)

lk = input("[=]LIKEE_ID> ")
#chat_id = input("Введите Chat_ID>")
link_chat = input("URL chat>")
if "@" in lk:
    likee_id = (lk[1:])
else:
    likee_id = (lk)




url = "https://api.like-video.com/likee-activity-flow-micro/official_website/WebView/getProfileDetail"
headers = {'Content-Type': 'application/json'}
data = {'likeeId': likee_id}
try:
    res = requests.post(url, headers=headers, data=json.dumps(data))
    uid = json.loads(res.text)['data']['userinfo']['uid']
    name = json.loads(res.text)['data']['userinfo']['user_name']
except:
    print()
    print("Ошибка")
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    exit()



    #url = ""
res = requests.get(link_chat, headers=us_agent)
matches = re.findall(r'"groupChatId":\s*"([^"]*)"', res.text)
for match in matches:
    print("Loading///")
    chat_id = (match)

print(chat_id)

    

    




#url = f"likevideo://web?url=https%3A%2F%2Flikee.com%2Flive%2Fpage-52744%2Findex.html%3Fchatid%3D{chat_id}%26uid%3D{uid}%26s%3D1&dp_source=invite-link&dp_detail=groupchat&dp_user={lk}"
url = f"https://likee.onelink.me/FvnB?pid=groupchat&c=invite-link&is_retargeting=true&af_dp=likevideo%3A%2F%2Fweb%3Furl%3Dhttps%253A%252F%252Flikee.com%252Flive%252Fpage-52744%252Findex.html%253Fchatid%253D{chat_id}%2526uid%253D{uid}%2526s%253D1%26dp_source%3Dinvite-link%26dp_detail%3Dgroupchat%26dp_user%3D{likee_id}&af_web_dp=https%3A%2F%2Flikee.com%2F"

os.system(dl)


logo = f"""
{Fore.YELLOW}
 =========== {lk} ===========

 UID> {uid}
 Name> {name}

 Ссылка: {url}

 ============================

"""
print(logo)
print()

input("Нажмите Enter")
os.system(dl)
os.system(st)
exit()







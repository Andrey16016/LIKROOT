print ("")
logo = """
╭╮╱╭┳━━━┳━━━┳━━━┳━━┳━╮╱╭┳━━━┳━━━╮
┃┃╱┃┃╭━╮┃╭━━┫╭━╮┣┫┣┫┃╰╮┃┃╭━━┫╭━╮┃
┃┃╱┃┃╰━━┫╰━━┫╰━╯┃┃┃┃╭╮╰╯┃╰━━┫┃╱┃┃
┃┃╱┃┣━━╮┃╭━━┫╭╮╭╯┃┃┃┃╰╮┃┃╭━━┫┃╱┃┃
┃╰━╯┃╰━╯┃╰━━┫┃┃╰┳┫┣┫┃╱┃┃┃┃╱╱┃╰━╯┃
╰━━━┻━━━┻━━━┻╯╰━┻━━┻╯╱╰━┻╯╱╱╰━━━╯
"""


#ди нахуй
#help
import requests
import json
import os
import time
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
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")




print (Fore.CYAN + logo)
print (Fore.YELLOW + "")

def get_profile_detail(likee_id):
    url = "https://api.like-video.com/likee-activity-flow-micro/official_website/WebView/getProfileDetail"
    headers = {'Content-Type': 'application/json'}
    data = {'likeeId': likee_id}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

lk = input("[=]Введите Likee_ID> ")
if "@" in lk:
    likee_id = (lk[1:])
else:
    likee_id = (lk)

profile_data = get_profile_detail(likee_id)

if profile_data:
    os.system(dl)
    print (Fore.YELLOW + "Данные JSON:")
    print (f" =========== {likee_id} ===========")
    baza = (json.dumps(profile_data, indent=4, ensure_ascii=False))
    for i in baza:
        #time.sleep(0.01)
        print(i, end='', flush=True)
else:
    print("[-] Не удалось получить данные профиля.")

print ("")
input("Нажмите enter")
os.system(dl)
os.system(st)
exit()



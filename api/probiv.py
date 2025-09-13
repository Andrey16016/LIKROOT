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
import colorama
from colorama import Fore
import time

os.system("clear")

colorama.init()


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

likee_id = input("Введите UserName>")
profile_data = get_profile_detail(likee_id)

if profile_data:
    os.system("clear")
    print (Fore.YELLOW + "Найденные данные:")
    print ("")
    baza = (json.dumps(profile_data, indent=4, ensure_ascii=False))
    for i in baza:
        time.sleep(0.01)
        print(i, end='', flush=True)
else:
    print("Не удалось получить данные профиля.")

print ("")
input("Нажмите enter")
os.system("reset")
os.system("python3 LIKROOT.py")
exit()



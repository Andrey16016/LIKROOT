print ("")
import os

os.system("clear")



logo = """
╭╮╭┳━━┳━━┳━╮
┃┃┃┃━━┫┃━┫╭╯
┃╰╯┣━━┃┃━┫┃
╰━━┻━━┻━━┻╯
"""

#hello world
#RESHETKA
#RAZVEDKA



import requests
import time
import colorama
from colorama import Fore

colorama.init()

#script
print (Fore.YELLOW + logo)

print ("")

username = input("{+}Введите username для поиска>")
time.sleep(1)
print (f"Ожидайте! Идет поиск по username ({username}) !!!")

socials = {
    'Facebook': f'https://www.facebook.com/{username}',
    'Instagram': f'https://www.instagram.com/{username}',
    'Twitter': f'https://twitter.com/{username}',
    'TikTok': f'https://www.tiktok.com/@{username}',
    'LinkedIn': f'https://www.linkedin.com/in/{username}',
    'GitHub': f'https://github.com/{username}',
    'Reddit': f'https://www.reddit.com/user/{username}',
    'YouTube': f'https://www.youtube.com/{username}',
    'VK': f'https://vk.com/{username}',
}

headers = {'User-Agent': 'Mozilla/5.0 (compatible; Bot/1.0)'}
found = []

for name, url in socials.items():
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            #proverka vkvk
            if name == 'VK' and ('profile.php?redirect=' in r.text or 'Страница не найдена' in r.text):
                continue
            found.append(url)
    except:
        pass

if found:
    print(Fore.GREEN + "[+]Найдены профили:")
    print ("")
    for f in found:
        print(f)
    i = input("Нажмите enter")
    os.system("clear")
    #ok
    os.system("python3 LIKROOT.py")
else:
    print(Fore.RED + "[-]Профили не найдены.")
    print ("")
    i = input("Нажмите enter")
    os.system("clear")
    #ok
    os.system("python3 LIKROOT.py")























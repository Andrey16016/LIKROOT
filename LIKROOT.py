import os
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


logo = """

╔╗──╔══╦╗╔═╦═══╦═══╦═══╦════╗
║║──╚╣╠╣║║╔╣╔═╗║╔═╗║╔═╗║╔╗╔╗║
║║───║║║╚╝╝║╚═╝║║─║║║─║╠╝║║╚╝
║║─╔╗║║║╔╗║║╔╗╔╣║─║║║─║║─║║
║╚═╝╠╣╠╣║║╚╣║║╚╣╚═╝║╚═╝║─║║
╚═══╩══╩╝╚═╩╝╚═╩═══╩═══╝─╚╝

🙃На данный момент софт в разработке
🔶Developer: RESHETKA
💬Telegramm: https://t.me/+SUsx6idsYCphNzAy


"""

print(logo)
input("Нажмите Enter")
exit()

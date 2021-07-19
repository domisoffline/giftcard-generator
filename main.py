import re
import random
import rstr
import time
import getpass
from colorama import init
from colorama import Fore, Back, Style
init()
print("Codes.txt will be cleared if you continue.\n\n\n\n\n\n\n\n\n")
with open('codes.txt', 'w+') as f:
    f.truncate()
class bcolors:
    init()
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = Fore.GREEN
    WARNING = '\033[93m'
    FAIL = Fore.RED
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.FAIL + "Welcome To Spilled's GiftCard Generator.")
store = input("What type of card would you like to generate?\n[1] Amazon\n[2] iTunes\n[3] Minecraft\n[4] Google Play\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

if store == '1':
    card_type = "Amazon"
    
if store == '2':
    card_type = "iTunes"
    
if store == '3':
    card_type = "Minecraft"
if store == '4':
    card_type = "Google Play"
print(bcolors.FAIL + f"Generating {card_type} GiftCards!\n")


while True:
    #Variables
    if store == '1':
        code = rstr.xeger(r'[A-Z0-9]{4}-[A-Z0-9]{6}-[A-Z0-9]{5}')
        
    if store == '2':
        code = rstr.xeger(r'[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}')
    
    if store == '3':
        code = rstr.xeger(r'[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}')

    if store == '4':
        code = rstr.xeger(r'[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}')
    sleeptime = int(rstr.xeger(r'[0-3]'))
    print(f"{bcolors.OKGREEN} Code Generated: {code}\n")
    with open('codes.txt', 'a') as f:
        f.write("\n" + code)
    time.sleep(sleeptime)
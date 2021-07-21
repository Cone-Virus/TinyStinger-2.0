import os
from colorama import Fore, Back, Style

def file_check(given_file):
    if os.path.isfile(given_file):
        print(Fore.GREEN + Style.BRIGHT + "Target file Validated")
    else:
        print(Fore.RED + Style.BRIGHT + "Target file could not be Validated")
        quit()

def banner():
    banner = '''▀█▀ █ █▄░█ █▄█   █▀ ▀█▀ █ █▄░█ █▀▀ █▀▀ █▀█
░█░ █ █░▀█ ░█░   ▄█ ░█░ █ █░▀█ █▄█ ██▄ █▀▄
Version: 2.0
Created by: @Cone_Virus
                         (\\\\
....-_...___-..-.._..-. -###)
                          \"\"'''
    print()
    print(Fore.YELLOW + Style.BRIGHT + banner)
    print(Style.RESET_ALL)

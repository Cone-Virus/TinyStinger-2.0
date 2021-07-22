import os
from colorama import Fore, Back, Style
import magic

def file_check(indicator,given_file):
    if os.path.isfile(given_file) and magic.from_file(given_file) == 'ASCII text':
        print(Fore.GREEN + Style.BRIGHT + "[+] " + indicator + " file Validated")
    else:
        print(Fore.RED + Style.BRIGHT + "[-] " + indicator + " file could not be Validated")
        quit()

def file_read(indicator,given_file):
    file_check(indicator,given_file)
    the_list =  open(given_file,'r').readlines()
    # Generate List
    variable_list = []
    for variable in the_list:
        variable = variable.strip('\n')
        # Ignore empty lines
        if variable != "":
            variable_list.append(variable)
    print(Fore.GREEN + Style.BRIGHT + "[+] All " + indicator + "s Processed")
    return variable_list


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

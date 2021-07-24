import os
from colorama import Fore, Back, Style
import magic
import argparse

def target_format(targets):
    temp_list = []
    for target in targets:
        if target.endswith('/'):
            temp_list.append(target)
        else:
            temp_list.append(target + "/")
    return temp_list

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
    unique_list = []
    for variable in the_list:
        variable = variable.strip('\n')
        # Ignore empty lines
        if variable != "":
            variable_list.append(variable)
    for x in variable_list:
        if x not in unique_list:
            unique_list.append(x)
    print(Fore.GREEN + Style.BRIGHT + "[+] All " + indicator + "s Processed")
    return unique_list

def arg_setup():
    parser = argparse.ArgumentParser()
    parser.set_defaults(which="None")
    subparsers = parser.add_subparsers(help='sub-command help')
    # Scan options
    scan = subparsers.add_parser("scan", help="Run the Scanner")
    scan.add_argument("db_name", metavar="<Database Name>", help="The name you would like to give the database")
    scan.add_argument("target_list", metavar="<Target List>", help="List of Targets")
    scan.add_argument("--exclude",  help="List of Out of Scope Targets")
    scan.add_argument("--threads", type=int, default=20, help="Threads to use (Default is 20)")
    scan.add_argument("--nohttp", action='store_false',help="Ignore HTTP but check if HTTPS not found")
    scan.add_argument("--xnohttp", action='store_false',help="Absolutely no HTTP scans")
    scan.add_argument("--noshell",  action='store_false',help="Don't default to built in shell")
    scan.set_defaults(which="scan")
    # shell options
    shell = subparsers.add_parser("shell", help="Load scan results into shell")
    shell.add_argument("db_name", metavar="<Database Name>", help="The name of the database you would like to load")
    shell.set_defaults(which="shell")
    # Return arguments
    args = parser.parse_args()
    if args.which == "None":
        parser.print_help()
        quit()
    return args


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


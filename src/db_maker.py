import sqlite3
from colorama import Fore, Back, Style
import os
import magic
import commands as com
import re

def format_db(db):
    cur = db.cursor()
    cur.execute('''CREATE TABLE targets
                   (url, waf, fav)''')
    db.commit()

def insert_db(db,value):
    cur = db.cursor()
    cur.execute("INSERT INTO targets VALUES ('" + value[0] + "','" + value[1] + "','" + value[2] + "')")
    db.commit()

def close_db(db):
    db.commit()
    db.close()
    quit()

def create_db(name):
    db_name = "storage/" +name + ".db"
    try:
        db = sqlite3.connect(db_name)
        format_db(db)
        print(Fore.GREEN + Style.BRIGHT + "[+] DB Created Sucessfully")
        return db
    except:
        print(Fore.RED + Style.BRIGHT + "[-] DB Could not be Created")
        quit()

def load_db(db_name):
    if os.path.exists(db_name):
        if "SQLite 3.x" in magic.from_file(db_name):
            try:
                db = sqlite3.connect(db_name)
                print(Fore.GREEN + Style.BRIGHT + "[+] DB Successfully Loaded")
                return db
            except:
                print(Fore.RED + Style.BRIGHT + "[-] DB Failed to Load")
        else:
            print(Fore.RED + Style.BRIGHT + "[-] DB is not correct format")
            quit()
    else:
        print(Fore.RED + Style.BRIGHT + "[-] DB Does not exist")
        quit()

def help_menu():
    menu = """
▀█▀ █ █▄░█ █▄█   █▀ █░█ █▀▀ █░░ █░░
░█░ █ █░▀█ ░█░   ▄█ █▀█ ██▄ █▄▄ █▄▄
    
Options:

help : Show this menu again
quit : Leave this shell

all : Show all Target Urls

mass <check> [yes/no] : Mass search through data
mass Commands:
check = fav,waf
[yes/no] = If data is or isn't available

select <Target Url> : Select which URL Look through
select Commands:
show <data> : Show data
    show Commands:
    data = stats
        data Commands:
        stats = fav,waf (AKA the little stuff)

delete <Target url> : Delete URL from DB
    """
    print(Fore.YELLOW + Style.BRIGHT + menu)

def shell_db(db):
    cur = db.cursor()
    print(Fore.GREEN + Style.DIM + "\n[%] Starting Shell")
    help_menu()
    url = "N/A"
    while True:
        command = input(Fore.YELLOW + Style.BRIGHT + "[Target: " + url + "]" + "\n#> " + Fore.GREEN)
        if command == "quit":
            print(Fore.GREEN + Style.BRIGHT + "\n[X] Closing Shell")
            close_db(db)
        elif command == "all":
            com.all(cur)
        elif command == "help":
            help_menu()
        elif re.match("^select .*",command):
            command = command.split(" ")
            url = com.check_url(command[1],cur)
        elif re.match("^mass .* .*",command):
            command = command.split(" ")
            com.mass(command[1],command[2],cur)
        elif re.match("^show .*",command):
            if url == "N/A":
                print(Fore.RED + Style.BRIGHT + "\n[-] No URL selected\n")
            else:
                command = command.split(" ")
                com.show(url,command[1],cur)
        else:
            print(Fore.RED + Style.BRIGHT + "[-] Unrecognized Command")
            help_menu()


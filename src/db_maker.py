import sqlite3
from colorama import Fore, Back, Style

def format_db(db):
    cur = db.cursor()
    cur.execute('''CREATE TABLE targets
                   (url, waf_status)''')
    db.commit()

def insert_db(db,value):
    cur = db.cursor()
    cur.execute("INSERT INTO targets VALUES ('" + value[0] + "','" + value[1] + "')")
    db.commit()

def close_db(db):
    db.commit()
    db.close()

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
    try:
        db = sqlite3.connect(db_name)
        print(Fore.GREEN + Style.BRIGHT + "[+] DB Successfully Loaded")
        return db
    except:
        print(Fore.RED + Style.BRIGHT + "[-] DB could not be loaded")
        quit()


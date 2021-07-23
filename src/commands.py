import sqlite3
from colorama import Fore, Back, Style

def all(cur):
    cur.execute("SELECT url FROM targets")
    rows = cur.fetchall()
    print(Fore.GREEN + Style.BRIGHT + "\n---[Targets]---")
    for row in rows:
        target = row[0]
        print("> " + target)
    print()

def check_url(url,cur):
    if cur.execute("SELECT url FROM targets WHERE url='" + url + "'").fetchone():
        print()
        return url
    else:
        print(Fore.RED + Style.BRIGHT + "\n[-] Target not Found\n")
        return "N/A"

def mass(check,option,cur):
    if check != "fav" and check != "waf":
        print(Fore.RED + Style.BRIGHT + "\n[-] Invalid Check option\n")
    else:
        if option != "yes" and option != "no":
            print(Fore.RED + Style.BRIGHT + "\n[-] Invalid yes/no option\n")
        else:
            if option == "yes": 
                banner = "Targets With " + check.upper()
                opt = " WHERE " + check + "!=" + '"N/A"'
            elif option == "no":
                banner = "Targets Without " + check.upper()
                opt = " WHERE " + check + "=" + '"N/A"'
            cur.execute("SELECT url," + check + " FROM targets" + opt)
            rows = cur.fetchall()
            print(Fore.GREEN + Style.BRIGHT + "\n---[" + banner + "]---")
            for row in rows:
                target = row[0]
                print("> " + target)
            print()

def show(url,data,cur):
    if data != "stats":
        print(Fore.RED + Style.BRIGHT + "\n[-] Invalid Data option\n")
    else:
        if data == "stats":
            opt = " WHERE url == " + '"' + url + '"'
            cur.execute("SELECT waf,fav FROM targets" + opt)
            rows = cur.fetchone()
            print()
            print(Fore.GREEN + Style.BRIGHT + "-----[WAF Results]-----")
            if rows[0] == "N/A":
                print("No WAF Detected")
            else:
                print(rows[0])
            print(Fore.GREEN + Style.BRIGHT + "---[Favicon Results]---")
            if rows[1] == "N/A":
                print("None Found")
            else:
                print(rows[1])
            print()
import subprocess
from colorama import Fore, Back, Style
import re
import os
import requests
import multiprocessing

def subdomain_finder(targets):
    temp_targets = []
    for target in targets:
        if target.startswith("*"):
            target = target[2:]
            print(Fore.GREEN + Style.BRIGHT + "[+] Looking for subdomains for " + target)
            subfinder_output = subprocess.run(['src/subfinder/subfinder','--silent','-d',target], capture_output=True, text=True).stdout.split('\n')
            for subs in subfinder_output:
                temp_targets.append(subs)
        else:
            temp_targets.append(target)
    return temp_targets

def http_valid_thread(target):
    mini_list = []
    valid_https = True
    valid_http = True
    if target.startswith("http://") or target.startswith("https://"):
        mini_list.append(target)
        return mini_list
    else:
        https_url = "https://" + target
        try:
            check = requests.get(https_url,timeout=5)
        except:
            valid_https = False
        if valid_https and int(check.status_code) < 500:
            mini_list.append(https_url)
        if Xno and (no or not valid_https):
            http_url = "http://" + target
            try:
                check = requests.get(http_url,timeout=5)
            except:
                valid_http = False
            if valid_http and int(check.status_code) < 500:
                mini_list.append(http_url)
        return mini_list

def http_valid(targets,nohttp,Xnohttp,threads):
    temp_targets = []
    global no
    no = nohttp
    global Xno
    Xno = Xnohttp
    print(Fore.GREEN + Style.BRIGHT + "[+] Validating URLS")
    with multiprocessing.Pool(threads) as p:
        test = p.map(http_valid_thread,targets)
    for a in test:
        for b in a:
            if b != "":
                temp_targets.append(b)
    print(Fore.GREEN + Style.BRIGHT + "\n[+] URLS Validated")
    return temp_targets

def waf_scan(target):
    waf_results = subprocess.run(['python3','src/wafw00f/wafw00f/main.py','-a',target], capture_output=True, text=True).stdout
    waf_results = waf_results.split('\n')
    for row in waf_results:
        if '[+]' in row:
            if 'WAF' in row:
                print(Fore.RED + Style.BRIGHT + "[-] WAF Found")
                waf_type = re.search("behind (.*) WAF",row)
                return waf_type.group(1)
    print(Fore.GREEN + Style.BRIGHT + "[+] No WAF Found")
    return "N/A"

def remove_exclusions(exclusions,targets):
    exclusion_bool = False
    num = 0
    temp_targets = []
    for target in targets:
        for ex in exclusions:
            if re.match(".*" + ex + ".*",target):
                exclusion_bool = True
            else:
                print(Fore.MAGENTA + Style.BRIGHT + "[+] Removing Exclusions" + num * ".", end='\r')
                num = num + 1
                if num == 4:
                    num = 0
        if exclusion_bool:
            exclusion_bool = False
        else:
            temp_targets.append(target)
    print()
    return temp_targets

def fav_scan(target):
    hash_num = "NOT_A_VALID_HASH"
    f = open("temp_fav_target.txt","w")
    f.write(target)
    f.close()
    process_cat = subprocess.Popen(['cat','temp_fav_target.txt'], stdout=subprocess.PIPE,shell=False)
    process_fav = subprocess.Popen(['python3','src/favfreak/favfreak.py'], stdin=process_cat.stdout,stdout=subprocess.PIPE,shell=False)
    process_cat.stdout.close()
    ansi_escape_8bit = re.compile(br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])')
    fav_results = ansi_escape_8bit.sub(b'', process_fav.communicate()[0]).decode('utf-8').replace('\n\n','\n').split('\n')
    for row in fav_results:
        if '[Hash]' in row:
            hash_num = row.split(" ")[1]
        elif hash_num in row and '~' not in row:
            fav_ID = row.split(" ")[0]
            fav_ID = fav_ID.replace('[','').replace(']','')
            print(Fore.GREEN + Style.BRIGHT + "[+] Favicon Identified")
            os.remove("temp_fav_target.txt")
            return fav_ID
        elif hash_num in row and '~' in row:
            print(Fore.MAGENTA + Style.DIM + "[/] Favicon not Identified but Hash Found")
            os.remove("temp_fav_target.txt")
            return hash_num
    os.remove("temp_fav_target.txt")
    print(Fore.RED + Style.BRIGHT + "[-] Favicon could not be Identified")
    return "N/A"


import subprocess
from colorama import Fore, Back, Style
import re

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

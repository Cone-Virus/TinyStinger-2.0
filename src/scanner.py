import subprocess
from colorama import Fore, Back, Style
import re

def waf_scan(target):
    waf_results = subprocess.run(['python3','src/wafw00f/wafw00f/main.py','-a',target], capture_output=True, text=True).stdout
    waf_results = waf_results.split('\n')
    for row in waf_results:
        if '[+]' in row:
            if 'WAF' in row:
                print(Fore.RED + Style.BRIGHT + "[-] WAF Found!")
                waf_type = re.search("behind (.*) WAF",row)
                return waf_type.group(1)
    print(Fore.GREEN + Style.BRIGHT + "[+] No WAF Found!")
    return "N/A"

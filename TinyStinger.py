import subprocess
import sys
import os
from colorama import Fore, Back, Style
# Import src files
sys.path.append(os.path.abspath("src/"))
import db_maker as store
import scanner as scan
import util as util

# Get Variables
target_file = sys.argv[1]
db_name = sys.argv[2]

# Banner
util.banner()

# Create DB
db = store.create_db(db_name)

# Scan targets in file
util.file_check(target_file)
target_list =  open(target_file,'r').readlines() 
for target in target_list:
    # Reset colorama
    print(Style.RESET_ALL)
    target = target.strip('\n')
    # Ignore empty lines
    if target != "":
        print(Fore.BLUE + Style.BRIGHT + "[+] " + target)
        # WAF Scan
        waf_result = scan.waf_scan(target)
        value = [target,waf_result]
        store.insert_db(db,value)

# Close DB
store.close_db(db)


import subprocess
import sys
import os
import argparse
from colorama import Fore, Back, Style
# Import src files
sys.path.append(os.path.abspath("src/"))
import db_maker as store
import scanner as scan
import util as util

# Banner
util.banner()

# Argument Evaluation
parser = argparse.ArgumentParser()
parser.add_argument("db_name", metavar="<Database Name>", help="The name you would like to give the database")
parser.add_argument("target_list", metavar="<Target List>", help="List of Targets")
parser.add_argument("--exclude",  help="List of Out of Scope Targets")

args = parser.parse_args()
db_name = args.db_name
target_file = args.target_list
exclude_file = args.exclude

# Create DB
db = store.create_db(db_name)

# Scan targets in file
target_list = util.file_read("Target",target_file)

if exclude_file != None:
    target_list = scan.remove_exclusions(util.file_read("Exclusion",exclude_file),target_list)

for target in target_list:
    # Reset Colors
    print(Style.RESET_ALL)
    # List Target
    print(Fore.BLUE + Style.BRIGHT + "[+] " + target)
    # WAF Scan
    waf_result = scan.waf_scan(target)
    value = [target,waf_result]
    store.insert_db(db,value)

# Close DB
store.close_db(db)

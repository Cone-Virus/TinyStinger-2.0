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
args = util.arg_setup()
if args.which == "scan":
    db_name = args.db_name
    target_file = args.target_list
    exclude_file = args.exclude
elif args.which == "shell":
    db = store.load_db(args.db_name)
    store.shell_db(db)

# Create DB
db = store.create_db(db_name)

# Scan targets in file
target_list = util.target_format(scan.http_valid(util.file_read("Target",target_file),args.nohttp))

# If blacklist given
if exclude_file != None:
    target_list = scan.remove_exclusions(util.file_read("Exclusion",exclude_file),target_list)

# Scan
for target in target_list:
    # Reset Colors
    print(Style.RESET_ALL)
    # List Target
    print(Fore.BLUE + Style.BRIGHT + "[+] " + target)
    # WAF Scan
    waf_result = scan.waf_scan(target)
    # Fav Scan
    fav_result = scan.fav_scan(target)
    value = [target,waf_result,fav_result]
    store.insert_db(db,value)

# Start shell if option noshell is not set
if args.noshell:
    store.shell_db(db)


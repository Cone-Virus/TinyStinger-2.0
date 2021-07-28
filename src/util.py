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
        dumb = True
    else:
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
    return unique_list

def banner():
    banner = '''▀█▀ █ █▄░█ █▄█   █▀ ▀█▀ █ █▄░█ █▀▀ █▀▀ █▀█
░█░ █ █░▀█ ░█░   ▄█ ░█░ █ █░▀█ █▄█ ██▄ █▀▄
Version: 2.0
Created by: @Cone_Virus
                                    (\\\\
....-_...___-..-.._..-. -###)
                                     \"\"'''
    return banner


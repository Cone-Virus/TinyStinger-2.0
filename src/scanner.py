import subprocess
import re
import os
import requests
import multiprocessing

def subdomain_finder(targets):
    temp_targets = []
    for target in targets:
        if target.startswith("*"):
            target = target[2:]
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
        if valid_https and int(check.status_code) < 504:
            mini_list.append(https_url)
        if Xno and (no or not valid_https):
            http_url = "http://" + target
            try:
                check = requests.get(http_url,timeout=5)
            except:
                valid_http = False
            if valid_http and int(check.status_code) < 504:
                mini_list.append(http_url)
        return mini_list

def http_valid(targets,nohttp,Xnohttp,threads):
    temp_targets = []
    global no
    no = nohttp
    global Xno
    Xno = Xnohttp
    with multiprocessing.Pool(threads) as p:
        test = p.map(http_valid_thread,targets)
    for a in test:
        for b in a:
            if b != "":
                temp_targets.append(b)
    return temp_targets

def waf_scan(target):
    waf_results = subprocess.run(['python3','src/wafw00f/wafw00f/main.py','-a',target], capture_output=True, text=True).stdout
    waf_results = waf_results.split('\n')
    for row in waf_results:
        if '[+]' in row:
            if 'WAF' in row:
                waf_type = re.search("behind (.*) WAF",row)
                return waf_type.group(1)
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
                num = num + 1
                if num == 4:
                    num = 0
        if exclusion_bool:
            exclusion_bool = False
        else:
            temp_targets.append(target)
    return temp_targets

def fav_scan(target):
    hash_num = "NOT_A_VALID_HASH"
    f = open("temp_fav_target.txt","w")
    f.write(target)
    f.close()
    process_cat = subprocess.Popen(['cat', 'temp_fav_target.txt'], stdout=subprocess.PIPE,shell=False)
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
            os.remove("temp_fav_target.txt")
            return fav_ID
        elif hash_num in row and '~' in row:
            os.remove("temp_fav_target.txt")
            return hash_num
    os.remove("temp_fav_target.txt")
    return "N/A"

def clean_spider(spider_list):
    check = True
    trash_list = ["text/css","text/html","prev/next","text/css","image/jpeg","image/webp","image/png","mm/dd/yy","text/plain","text/javascript","text/xml","application/json","application/x-www-form-urlencoded","image/gif","mm/yy/dd"]
    clean_list = []
    cleaner_list = []
    for row in spider_list:
        for end in trash_list:
            if row.endswith(end):
                check = False
        if check:
            clean_list.append(row)
        check = True

    for row in clean_list:
        if row not in trash_list:
            if not (row.startswith("./") or row.startswith("../")):
                cleaner_list.append(row)

    return cleaner_list


def spider_scan(target,directory,depth):
    general_list = []
    link_list = []
    href_list = []
    url_list = []
    sub_list = []
    java_list = []
    robot_list = []
    gospider_output = subprocess.run(['src/gospider/gospider','-s',target,'-d',depth], capture_output=True, text=True).stdout.split('\n')
    for row in gospider_output:
        if re.match("\[linkfinder\] \- \[.*\] \- .*",row):
            linkfinder = row.split(" - ")[2]
            if linkfinder not in link_list:
                if linkfinder.startswith("//"):
                    linkfinder =  linkfinder
                elif linkfinder.startswith("/"):
                    linkfinder = target[:-1] + linkfinder
                link_list.append(linkfinder)
        elif re.match("\[linkfinder\] \- .*",row):
            linkfinder = row.split(" - ")[1]
            if linkfinder not in link_list:
                if linkfinder.startswith("//"):
                    linkfinder =  linkfinder
                elif linkfinder.startswith("/"):
                    linkfinder = target[:-1] + linkfinder
                link_list.append(linkfinder)
        elif re.match("\[href\] \- .*",row):
            href = row.split(" - ")[1]
            if href not in href_list:
                href_list.append(href)
        elif re.match("\[url\] - \[.*\] - .*",row):
            url = row.split(" - ")[2]
            if url not in url_list:
                url_list.append(url)
        elif re.match("\[javascript\] \- .*",row):
            java = row.split(" - ")[1]
            if java not in java_list:
                java_list.append(java)
        elif re.match("\[subdomains\] \- .*",row):
            sub = row.split(" - ")[1]
            if sub not in sub_list:
                sub_list.append(sub)
        elif re.match("\[robots\] \- .*",row):
            robot = row.split(" - ")[1]
            if robot not in robot_list:
                robot_list.append(robot)
    
    link_list = clean_spider(link_list)
    href_list = clean_spider(href_list)
    url_list = clean_spider(url_list)
    sub_list = clean_spider(sub_list)
    java_list = clean_spider(java_list)
    robot_list = clean_spider(robot_list)

    # Write to File
    f = open(directory + "spider.txt","w")
    
    # Links
    f.write("--------[Links Grabbed]----------\n")
    for link in link_list:
        f.write(link + '\n')

    # Href
    f.write("--------[Hrefs Grabbed]----------\n")
    for link in href_list:
        f.write(link + '\n')

    # Java
    f.write("--------[Javascripts Grabbed]----------\n")
    for link in java_list:
        f.write(link + '\n')

    # URL
    f.write("--------[URLS Grabbed]----------\n")
    for link in url_list:
        f.write(link + '\n')

    # Sub
    f.write("--------[Subdomains Grabbed]----------\n")
    for link in sub_list:
        f.write(link + '\n')

    # Robots
    f.write("--------[Robots Grabbed]----------\n")
    for link in robot_list:
        f.write(link + '\n')

    # Close File
    f.close()

    # Return path to spider.txt
    spider_txt = directory + "spider.txt"
    return spider_txt

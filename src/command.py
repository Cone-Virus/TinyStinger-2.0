import sqlite3
import os

def grab_list(db):
    cur = db.cursor()
    cur.execute("SELECT url FROM targets")
    test = cur.fetchall()
    return test

def get_values(db,url,opt):
    cur = db.cursor()
    data = opt.lower()
    if data == "stats":
        opt = " WHERE url == " + '"' + url + '"'
        cur.execute("SELECT waf,fav FROM targets" + opt)
        rows = cur.fetchone()
        stat = "-----[WAF Results]-----\n"
        if rows[0] == "N/A":
            stat = stat + "No WAF Detected\n"
        else:
            stat = stat + rows[0] + '\n'
        stat = stat + "-----[Fav Results]-----\n"
        if rows[1] == "N/A":
            stat = stat + "None Found\n"
        else:
            stat = stat + rows[1] + '\n'
        return stat
    elif data == "spider":
        opt = " WHERE url == " + '"' + url + '"'
        cur.execute("SELECT spider FROM targets" + opt) 
        rows = cur.fetchone()
        spider = open(rows[0],"r")
        all_spider = spider.read()
        return all_spider

def db_validator(name):
    result = os.popen('ls storage/').read().split("\n")
    if " " in name:
        return False
    for R in result:
        if name == R:
            return False
    return True

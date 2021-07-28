import sqlite3
import os
import magic
import command as com
import re

def target_db(target,db_name):
    prot = re.search("(.*)\:\/\/.*\/",target)
    proto = prot.group(1)
    direct = re.search("https?\:\/\/(.*)\/",target)
    result = direct.group(1).replace(".","_")
    final = "storage/" + db_name + "/" + proto + "_" + result + "/"
    os.mkdir(final, 0o755)
    return final
 

def format_db(db):
    cur = db.cursor()
    cur.execute('''CREATE TABLE targets
                   (url, waf, fav, spider)''')
    db.commit()

def insert_db(db,value):
    cur = db.cursor()
    cur.execute("INSERT INTO targets VALUES ('" + value[0] + "','" + value[1] + "','" + value[2] + "','" + value[3] +"')")
    db.commit()

def close_db(db):
    db.commit()
    db.close()
    quit()

def create_db(name):
    db_name = "storage/" + name + "/" +name + ".db"
    os.mkdir("storage/" + name, 0o755 )
    db = sqlite3.connect(db_name)
    format_db(db)
    return db
    

def load_db(db_name,switch):
    if switch == 0:
        if os.path.exists(db_name):
            if "SQLite 3.x" in magic.from_file(db_name):
                return True
            else:
                return False
        else:
            return False
    elif switch == 1:
        db = sqlite3.connect(db_name)
        return db



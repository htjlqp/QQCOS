import json

import pymongo
from flask import Flask,request
import hashlib
from pymongo import MongoClient
dataBaseIp="127.0.0.1"
#加密
sha512=hashlib.sha512()
app = Flask(__name__)
#数据库
myclient = pymongo.MongoClient("mongodb://"+dataBaseIp+"/")
mydb = myclient["mydb"]
mytb_login= mydb["login"]
#mytb_login.find({"username":"dfsdf"})

# def findPassword(username):
#     passwords=mydb.login.find_one({"username": username})
#     print(passwords.get('pw'))
# findPassword("dfsdf")
def findMydata():
    mydata = mytb_login.find({"username":"admin","pw":"123"})
    dd=mydata[0]
    del(dd["_id"])
    print(dd)
    print(json.dumps(dd))
findMydata()
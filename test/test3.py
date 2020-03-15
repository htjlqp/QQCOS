import hashlib
sha512=hashlib.sha512()
dd="sddsf"
dd=sha512.update(dd.encode())
print(sha512.hexdigest())
# import pymongo
# from pymongo import MongoClient
#
# myclient = pymongo.MongoClient("mongodb://${dataBaseIp}/")
# mydb = myclient["mydb"]
# mytb= mydb["login"]
# print(mytb)
# import hashlib
# sha512=hashlib.sha512()
# dd="sddsf"
# dd=sha512.update(dd.encode())
# print(sha512.hexdigest())
# import pymongo
# from pymongo import MongoClient
#
# myclient = pymongo.MongoClient("mongodb://${dataBaseIp}/")
# mydb = myclient["mydb"]
# mytb= mydb["login"]
# print(mytb)

# import requests, json
#
# url_json = 'http://httpbin.org/post'
# data_json = json.dumps({'key1': 'value1', 'key2': 'value2'})  # dumps：将python对象解码为json数据
# r_json = requests.post(url_json, data_json)
# print(r_json)
# print(r_json.text)
# print(r_json.content)
import json
import urllib.request
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
headers['Accept'] = 'application/json'
headers['Content-Type']="application/x-www-form-urlencoded; charset=UTF-8"
facepic1='https://qjt-1258802717.cos.ap-chengdu.myqcloud.com/data/data/com.net.myapp/pictures/nbinpic/1.jpg'
facepic2='https://qjt-1258802717.cos.ap-chengdu.myqcloud.com/data/data/com.net.myapp/pictures/nbinpic/2.jfif'
# facepic1 = facepic1.replace('/', '%2F')
# facepic1 = facepic1.replace(':', '%3A')
# facepic2 = facepic2.replace('/', '%2F')
# facepic2 = facepic2.replace(':', '%3A')
data = {}
data['image_url_a'] = facepic1
data['image_url_b'] = facepic2
url="https://ai.qq.com/cgi-bin/appdemo_facecompare?g_tk=5381"
reqdata = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,reqdata,headers)
html = urllib.request.urlopen(req).read()
print(json.loads(html.decode('ascii'))['data']['similarity'])
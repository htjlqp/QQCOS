import base64
import datetime
import time
import json
#now_time = datetime.datetime.now()
#time_str3 = datetime.strftime(now_time,'%Y%m%d%H%M%S')
#print(type(now_time.timestamp()))
#print(str(now_time.strftime('%Y%m%d')))
#print(int(now_time)-int(20200309))
# str1='{"name": "Tom", "age": 23}'
# print(json.loads(str1))
# dict = {'Name': 'Zara', 'Age': 7}
#
# print("Value : %s" %  dict.__contains__('Age'))
# print("Value : %s" %  dict.__contains__('Sex'))


import requests, json

# url_json = 'http://httpbin.org/post'
# data_json = json.dumps({'key1': 'value1', 'key2': 'value2'})  # dumps：将python对象解码为json数据
# r_json = requests.post(url_json, data_json)
# print(r_json)
# print(r_json.text)
# print(r_json.content)
def goTenXunServerCmp(facepic1, facepic2):
    # 上传到腾讯人脸识别上去比较发现》80的就可以登录
    facepic1=facepic1.replace('/', '%2F')
    facepic1 = facepic1.replace(':', '%3A')
    facepic2=facepic2.replace('/', '%2F')
    facepic2 = facepic2.replace(':', '%3A')

    # postdata = urllib.parse.urlencode(
    #     {'Content-Type': 'application/json',
    #      'image_url_a': facepic1,
    #      'image_url_b': facepic2
    #      })
    data_json = json.dumps({'image_url_a': facepic1, 'image_url_b': facepic2})
    #data_json = json.dumps({'image_url_b': datas})
    #datas="{image_url_a="+facepic1+"&"+"image_url_b="+facepic2+"}"
    headers={'Host':'ai.qq.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
             ,'Accept':'application/json','Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
             ,'Accept-Encoding':'gzip, deflate, br','Referer':'https://ai.qq.com/product/face.shtml'
             ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
             ,'Origin':'https://ai.qq.com'}
    url1 = "https://ai.qq.com/cgi-bin/appdemo_facecompare?g_tk=5381"
    # res = requests.post(url=url1,json=postdata,headers=headers)
    # print(res.text)
    # print(res.content)
    s = requests.session()
    s.headers.update(headers)

    print(s.post(url1, params =data_json,headers=headers).json())
goTenXunServerCmp("https://qjt-1258802717.cos.ap-chengdu.myqcloud.com/data/data/com.net.myapp/pictures/nbinpic/2020319222055.png","https://qjt-1258802717.cos.ap-chengdu.myqcloud.com/data/data/com.net.myapp/pictures/nbinpic/2020319222055.png")
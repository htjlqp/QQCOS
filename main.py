import base64,datetime,os,pymongo,hashlib,json,requests
import urllib

from flask import Flask, request, url_for
from pymongo import MongoClient
from werkzeug.utils import secure_filename

dataBaseIp="127.0.0.1"
#加密
sha512=hashlib.sha512()
app = Flask(__name__)
#数据库
myclient = pymongo.MongoClient("mongodb://"+dataBaseIp+"/")
mydb = myclient["mydb"]
mytb_login= mydb["login"]
#mytb_login.find({"username":"dfsdf"})
#登录后记录token
userToKen={}

def loginTimeCmpAndClearUserToKen(token):
    if(userToKen.__contains__(token)):
        if(int(datetime.datetime.now().strftime('%Y%m%d'))-int(userToKen[token])>=1):
            userToKen.pop(token)
        return True
    else:
        return False
def findPassword(username,password):
    password=mytb_login.find_one({"username": username,"pw":password})
    if  password is None:
        return ""
    else:
        sha512.update(password.get('pw').encode())
        return sha512.hexdigest()
    return ""
@app.route('/login',methods=['POST'])
def login():
    error = None
    username=request.form['username']
    password=request.form['password']
    mac = request.form['mac']

    if(username=="" and password==""):
        return ""
    getPw=findPassword(username,password)
    if(getPw==""):
        return "err"#密码错误
    else:
        userToKen[getPw+'@'+mac]=int(datetime.datetime.now().strftime('%Y%m%d'))
        return getPw
        #return json.dumps(getPw)
    #查询数据库
    return
# def allowed_file(filename):
#     return '.' in filename and \
#     filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/ImgUpload', methods=['POST'])
def upload_pic():
    # 用户头像上传——先不用
    if request.method == 'POST':
        token = request.form['token']
        username = request.form['username']
        file = request.form['img']
        loginTimeCmpAndClearUserToKen(token)
    if file:
        imgdata = base64.b64decode(file)
        now_time = datetime.datetime.now()
        file = open(username+'filename'+str(now_time.strftime("%Y%m%d"))+str(now_time.strftime("%H%M%S"))+'.jpg', 'wb')
        file.write(imgdata)
        file.close()
        return "ok"
    return "err"
@app.route('/ImgUpload2', methods=['POST'])
def upload_pic2():
    #用户头像上传
    if request.method == 'POST':
        token = request.form['token']
        username = request.form['username']
        fileurl = request.form['imgurl']
        loginTimeCmpAndClearUserToKen(token)
    if fileurl:
        mydata = mytb_login.find_one({"username": username})
        if(len(mydata)>0):
            mydata = mytb_login.update({'username': username},{'$set': {'imgurl': fileurl}})
            return '{"ret":"ok","result":[{"data":"ok"}]}'
    return '{"ret":"ok","result":[{"data":"err"}]}'
@app.route('/my', methods=['POST'])
def findMydata():
    #得到我的数据
    if request.method == 'POST':
        token = request.form['token']
        username = request.form['username']
        if loginTimeCmpAndClearUserToKen(token)==False:
            return '{"Redirect":"login"}'
        mydata = mytb_login.find_one({"username": username})
        if(len(mydata)>0):
            del (mydata["_id"])
            del (mydata["pw"])
            return '{"ret":"ok","result":['+json.dumps(mydata)+ ']}'
    return '{"ret":"Redirect","result":[{"data":"login"}]}'
@app.route('/myupdate', methods=['POST'])
def updateMydata():
    if request.method == 'POST':
        token = request.form['token']
        username = request.form['username']
        age = request.form['age']
        tel = request.form['tel']
        birthday = request.form['birthday']
        rmk = request.form['rmk']
        if loginTimeCmpAndClearUserToKen(token)==False:
            return '{"Redirect":"login"}'
        mydata = mytb_login.update({'username':username},{'$set':{'age':age,'tel':tel,'birthday':birthday,'rmk':rmk}})
        if(len(mydata)>0):
            return '{"ret":"ok","result":[{"data":"ok"}]}'
    return '{"ret":"Redirect","result":[{"data":"login"}]}'
@app.route('/manface', methods=['POST'])
def manFace():
    #人脸登录,手机端上传地址后跟原数据库中的地址上传到腾讯人脸识别上去比较发现》80的就可以登录
    if request.method == 'POST':
        username = request.form['username']
        facepic = request.form['facepic']
        mac = request.form['mac']
        mydata = mytb_login.find_one({"username": username})
        imgurl=""
        password=""
        if(len(mydata)>0):
            del (mydata["_id"])
            imgurl=mydata["imgurl"]
            password=mydata["pw"]
        if(goTenXunServerCmp(imgurl,facepic)>80):
            #模拟登录
            getPw = findPassword(username, password)
            userToKen[getPw + '@' + mac] = int(datetime.datetime.now().strftime('%Y%m%d'))
            return  '{"ret":"ok","result":[{"token":'+getPw+ '}]}'
    return '{"ret":"Redirect","result":[{"data":"login"}]}'
def goTenXunServerCmp(facepic1,facepic2):
    #上传到腾讯人脸识别上去比较发现》80的就可以登录
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    headers['Accept'] = 'application/json'
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    data = {}
    data['image_url_a'] = facepic1
    data['image_url_b'] = facepic2
    url = "https://ai.qq.com/cgi-bin/appdemo_facecompare?g_tk=5381"
    reqdata = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, reqdata, headers)
    html = urllib.request.urlopen(req).read()
    return json.loads(html.decode('ascii'))['data']['similarity']
if __name__ == '__main__':
    app.run(debug=True,host='192.168.3.253',port=5000)
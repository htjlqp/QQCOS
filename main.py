import base64,datetime,os,pymongo,hashlib,json
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

@app.route('/my', methods=['POST'])
def findMydata():
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
            return '{"ret":"ok","result":[{"data":"okdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdg"}]}'
    return '{"ret":"Redirect","result":[{"data":"login"}]}'
if __name__ == '__main__':
    app.run(debug=True,host='192.168.3.112',port=5000)
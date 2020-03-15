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
dict = {'Name': 'Zara', 'Age': 7}

print("Value : %s" %  dict.__contains__('Age'))
print("Value : %s" %  dict.__contains__('Sex'))
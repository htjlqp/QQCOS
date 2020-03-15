from sqlalchemy import create_engine
import pymysql
def connDataGetconn():
    hostname='127.0.0.1'
    port='3306'
    database='mydatabase'
    username='root'
    password='www.56.com'
    DB_URL='mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset-utf8'\
        .format(username=username,password=password,hostname=hostname,port=port,database=database)
    engine = create_engine(DB_URL)
    #conn=engine.connect()
    #result=conn.execute("select 1")
    #print(result.fetchone())
    return engine
connDataGetconn()
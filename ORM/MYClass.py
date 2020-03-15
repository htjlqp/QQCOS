from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from dataConn import connDataGetconn
engine=connDataGetconn()
Base= declarative_base(engine)
class Login(Base):
    __tablename__='login'
    id=Column(Integer,primary_key=True,autoincrement=True)
    userName=Column(String(255))
    passWord = Column(String(255))
    key=Column(String(255))
    sex = Column(String(1))
    qq = Column(String(50))
    tel = Column(String(20))
Base.metadata.create_all()#一但生成表后，添加新的字段就没办法添加了，要手动添加
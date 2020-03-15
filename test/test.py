from sqlalchemy.orm import sessionmaker
from ORM.MYClass import *

session=sessionmaker(engine)()
#增加
# login=Login(userName='hts',passWord='123456',key='dsfsfds',sex='1',qq='113123123',tel='18677777777')
# session.add(login)
# session.commit()
#查询
# rets=session.query(Login).all()
# for i in rets:
#     print(i.tel)
#条件查询
# rets=session.query(Login).filter(Login.tel=='18677777777')
# for i in rets:
#     print(i.id)
#条件查询2
# rets=session.query(Login).filter_by(tel='18677777777')
# for i in rets:
#     print(i.tel)
#条件查询4
# rets=session.query(Login).filter(Login.tel.like('186%')).all()
# for i in rets:
#     print(i.tel)
#条件查询5不区分大小写
# rets=session.query(Login).filter(Login.tel.ilike('186%')).all()
# for i in rets:
#     print(i.tel)
#条件查询6-in_(列表)
# rets=session.query(Login).filter(Login.tel.in_(['18677777777','18633333333'])).all()
# for i in rets:
#     print(i.tel)
#条件查询7-上取反
# rets=session.query(Login).filter(~Login.tel.in_(['18677777777','18633333333'])).all()
# for i in rets:
#     print(i.tel)
#条件查询8-做用同上
# rets=session.query(Login).filter(Login.tel.notin_(['18677777777','18633333333'])).all()
# for i in rets:
#     print(i.tel)
#条件查询9-is null
# rets=session.query(Login).filter(Login.tel==None).all()
# for i in rets:
#     print(i.tel)
#条件查询11-and
# rets=session.query(Login).filter(Login.tel=='18677777777',Login.id=='2').all()
# for i in rets:
#     print(i.tel)
#条件查询12-and
# rets=session.query(Login).filter(and_(Login.tel=='18677777777',Login.id=='2')).all()
# for i in rets:
#     print(i.tel)
#条件查询13-or
# rets=session.query(Login).filter(or_(Login.tel=='18677777777',Login.id=='1')).all()
# for i in rets:
#     print(i.tel)
#条件查询13-or
# rets=session.query(Login).filter(or_(Login.tel=='18677777777',Login.id=='1')).all()
# for i in rets:
#     print(i.tel)
#删除
# rets=session.query(Login).filter(or_(Login.tel=='18677777777',Login.id=='1')).first()
# session.delete(rets)
# session.commit()
#正排序
# rets=session.query(Login).order_by(Login.id)
# for i in rets:
#     print(i.tel)
#排序
# rets=session.query(Login).order_by("id")
# for i in rets:
#     print(i.tel)
#排序
# rets=session.query(Login).order_by("id")
# for i in rets:
#     print(i.tel)
#反排序
# rets=session.query(Login).order_by(Login.id.asc())
# for i in rets:
#     print(i.tel)
#数据加载大小
# rets=session.query(Login).limit(1).all()
# for i in rets:
#     print(i.tel)
#数据加载切片
# rets=session.query(Login).offset(1).limit(1).all()
# for i in rets:
#     print(i.tel)
#数据加载切片
# rets=session.query(Login)[0:1]
# for i in rets:
#     print(i.tel)



#聚合查询1
# rets=session.query(func.avg(Login.id)).all()
# print(rets)
#聚合查询2
# rets=session.query(func.count(Login.id)).all()
# print(rets)
#聚合查询3
# rets=session.query(func.max(Login.id)).all()
# print(rets)
#聚合查询4
# rets=session.query(func.min(Login.id)).all()
# print(rets)
#聚合查询5
# rets=session.query(func.sum(Login.id)).all()
# print(rets)
#聚合查询6
# rets=session.query(func.sum(Login.id)).group_by(Login.id).all()
# print(rets)
#聚合查询7
# rets=session.query(func.sum(Login.id)).group_by(Login.id).having(Login.id>=1).all()
# print(rets)



#coding:utf-8
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class tclass(Base):
	__tablename__='tclass'
	
	id=Column(Integer,primary_key=True)
	name=Column(String(20))

engine=create_engine('mysql+mysqldb://root:111111@localhost:3306/testmodel')

DBsession=sessionmaker(bind=engine)

session=DBsession()

Base.metadata.create_all(engine)

session.commit()

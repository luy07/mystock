#coding:utf-8
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import session_maker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

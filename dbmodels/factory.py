#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
# Copyright (c) 2017 luy. All Rights Reserved
#
# @author luy(luy007@msn.cn)
#
######################################################################
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()
engine = create_engine('mysql+mysqldb://root:111111@localhost/mystock?charset=utf8')

def getSession():
    DBsession=sessionmaker(bind=engine)
    session=DBsession()
    return session

def createSchema():
    Base.metadata.create_all(engine)
    session=getSession()
    session.commit()


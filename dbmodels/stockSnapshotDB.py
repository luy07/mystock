#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class stockSnapshot(Base):
    '''present a stock snapshot'''
    __tablename__='stockSnapshot'
    gid=Column(Integer,primary_key=True)					#股票编号
    increPer=Column(Integer)              #涨跌百分比
    increase=Column(Integer)              #涨跌额
    name=Column(String(10))                 #股票名称
    todayStartPri=Column(Integer)			#今日开盘价
    yestodEndPri=Column(Integer)			#昨日收盘价
    nowPri=Column(Integer)				#当前价格
    todayMax=Column(Integer)				#今日最高价
    todayMin=Column(Integer)				#今日最低价
    competitivePri=Column(Integer)		#竞买价
    reservePri=Column(Integer)			#竞卖价
    traNumber=Column(Integer)				#成交量
    traAmount=Column(Integer)				#成交金额
    buyOne=Column(Integer)				#买一
    buyOnePri=Column(Integer)				#买一报价
    buyTwo=Column(Integer)				#买二
    buyTwoPri=Column(Integer)				#买二报价
    buyThree=Column(Integer)				#买三
    buyThreePri=Column(Integer)			#买三报价
    buyFour=Column(Integer)				#买四
    buyFourPri=Column(Integer)			#买四报价
    buyFive=Column(Integer)				#买五
    buyFivePri=Column(Integer)			#买五报价
    sellOne=Column(Integer)				#卖一
    sellOnePri=Column(Integer)			#卖一报价
    sellTwo=Column(Integer)				#卖二
    sellTwoPri=Column(Integer)			#卖二报价
    sellThree=Column(Integer)				#卖三
    sellThreePri=Column(Integer)			#卖三报价
    sellFour=Column(Integer)				#卖四
    sellFourPri=Column(Integer)			#卖四报价
    sellFive=Column(Integer)				#卖五
    sellFivePri=Column(Integer)			#卖五报价
    date=Column(String)
    time=Column(String)

    def __init__(self):
       self.testa=1

    def __str__(self):
       rint(u'''股票编号:%s
             涨跌百分比:%s
             涨跌额:%s
             股票名称:%s
             今日开盘价:%s
             昨日收盘价:%s
             当前价格:%s
             今日最高价:%s
             今日最低价:%s
             竞买价:%s
             竞卖价:%s
             成交量:%s
             成交金额:%s
             买一:%s
             买一报价:%s
             买二:%s
             买二报价:%s
             买三:%s
             买三报价:%s
             买四:%s
             买四报价:%s
             买五:%s
             买五报价:%s
             卖一:%s
             卖一报价:%s
             卖二:%s
             卖二报价:%s
             卖三:%s
             卖三报价:%s
             卖四:%s
             卖四报价:%s
             卖五:%s
             卖五报价:%s
             日期:%s
             时间:%s''' %
             ())

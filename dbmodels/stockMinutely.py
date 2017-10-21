#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,Float,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import factory


class stockMinutely(factory.Base):
    '''present a stock snapshot'''
    __tablename__='stockMinutely'
    gid=Column(String(10),primary_key=True)					#股票编号
    name=Column(String(10))             #股票名称
    increPer=Column(Float)              #涨跌百分比
    increase=Column(Float)              #涨跌额
    openPri=Column(Float)			#今日开盘价
    yesterdayPri=Column(Float)			#昨日收盘价
    nowPri=Column(Float)				#当前价格
    highPri=Column(Float)				#今日最高价
    lowPri=Column(Float)				#今日最低价
    competitivePri=Column(Float)		#竞买价
    reservePri=Column(Float)			#竞卖价
    traNumber=Column(Integer)			#成交量
    traAmount=Column(Float)				#成交金额
    buyOne=Column(Integer)				#买一
    buyOnePri=Column(Float)				#买一报价
    buyTwo=Column(Integer)				#买二
    buyTwoPri=Column(Float)				#买二报价
    buyThree=Column(Integer)				#买三
    buyThreePri=Column(Float)			#买三报价
    buyFour=Column(Integer)				#买四
    buyFourPri=Column(Float)			#买四报价
    buyFive=Column(Integer)				#买五
    buyFivePri=Column(Float)			#买五报价
    sellOne=Column(Integer)				#卖一
    sellOnePri=Column(Float)			#卖一报价
    sellTwo=Column(Integer)#卖二
    sellTwoPri=Column(Float)			#卖二报价
    sellThree=Column(Integer)				#卖三
    sellThreePri=Column(Float)			#卖三报价
    sellFour=Column(Integer)				#卖四
    sellFourPri=Column(Float)			#卖四报价
    sellFive=Column(Integer)				#卖五
    sellFivePri=Column(Float)			#卖五报价
    date=Column(String(10))
    time=Column(String(10))

    def __init__(self,stock):
        keys=dir(stock)
        for key in keys:
            if key.startswith('__')==False:
                setattr(self,key,getattr(stock,key))

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


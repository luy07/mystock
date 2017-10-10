#!/usr/bin/env python
# -*- coding: utf-8 -*-
class stockSnapshot(object):
    '''present a stock snapshot'''
    gid=''					#股票编号
    increPer=0              #涨跌百分比
    increase=0              #涨跌额
    name=''                 #股票名称
    todayStartPri=0			#今日开盘价
    yestodEndPri=0			#昨日收盘价
    nowPri=0				#当前价格
    todayMax=0				#今日最高价
    todayMin=0				#今日最低价
    competitivePri=0		#竞买价
    reservePri=0			#竞卖价
    traNumber=0				#成交量
    traAmount=0				#成交金额
    buyOne=0				#买一
    buyOnePri=0				#买一报价
    buyTwo=0				#买二
    buyTwoPri=0				#买二报价
    buyThree=0				#买三
    buyThreePri=0			#买三报价
    buyFour=0				#买四
    buyFourPri=0			#买四报价
    buyFive=0				#买五
    buyFivePri=0			#买五报价
    sellOne=0				#卖一
    sellOnePri=0			#卖一报价
    sellTwo=0				#卖二
    sellTwoPri=0			#卖二报价
    sellThree=0				#卖三
    sellThreePri=0			#卖三报价
    sellFour=0				#卖四
    sellFourPri=0			#卖四报价
    sellFive=0				#卖五
    sellFivePri=0			#卖五报价
    date=''                 #日期
    time=''                 #时间

    def __init__(self):
       self.testa=1

    def __str__(self):
       print(u'''股票编号:%s
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

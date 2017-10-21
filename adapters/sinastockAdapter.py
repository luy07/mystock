#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
# Copyright (c) 2017 luy. All Rights Reserved
#
# @author luy(luy007@msn.cn)
#
######################################################################
# sh603129,春风动力,34.110,34.160,34.370,34.400,33.560,34.370,34.380,1790347,60680277.000,700,34.370,10400,34.360,400,34.350,1000,34.340,5000,34.330,3900,34.380,8400,34.390,3500,34.400,100,34.410,500,34.420,2017-10-20,15:00:00,00
# import sys
# sys.path.insert('..')
from models import stockSnapshot

def convertToModel(dataItem):
    if isinstance(dataItem, unicode):
        itemArray=dataItem.split(',')
        if len(itemArray) == 34:
            model=stockSnapshot()
            model.gid=itemArray[0]
            model.name=itemArray[1]
            model.openPri = float(itemArray[2])
            model.yesterdayPri=float(itemArray[3])
            model.nowPri=float(itemArray[4])
            model.highPri=float(itemArray[5])
            model.lowPri=float(itemArray[6])
            model.traNumber=float(itemArray[8])
            model.traAmount=float(itemArray[9])
            model.increase= float(itemArray[4]) - float(itemArray[3])
            model.increPer=  model.increase/ float(itemArray[4])
            model.date=itemArray[-3]
            model.time=itemArray[-2]
            return model
        else:
            print('convert fail:data splited result length no match')
    else:
        print('convert fail:input data type error')



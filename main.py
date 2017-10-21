#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
# Copyright (c) 2017 luy. All Rights Reserved
#
# @author luy(luy007@msn.cn)
#
######################################################################
from requestors import sinaStockRequestor
from adapters import sinastockAdapter
from dbmodels import stockMinutely,factory

factory.createSchema()

data=sinaStockRequestor.getStockCurrent('sh603129,sz002558')

session=factory.getSession()

for item in data:
    stockSnap= sinastockAdapter.convertToModel(item)
    if stockSnap!=None:
        stockDbModel=stockMinutely(stockSnap)
        session.add(stockDbModel)
        print ('dbmodel have add to session')
    else:
        print('convert fail,no data inserted.')
    print('one loop.')

if  len(session.new)!=0:
    session.commit()
    print('session committed successfully!')

session.close()
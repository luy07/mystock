#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
# Copyright (c) 2017 luy. All Rights Reserved
#
# @author luy(luy007@msn.cn)
#
######################################################################
from models import stockSnapshot
from requestors import sinaStockRequestor
from  dbmodels import factory,stockMinutely

list=sinaStockRequestor.getStockCurrent('sh600001')



for item in list:

    session=factory.getSession()

    stockN=stockSnapshot()


    stockM=stockMinutely()


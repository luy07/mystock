#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
# Copyright (c) 2017 luy. All Rights Reserved
#
# @author luy(luy007@msn.cn)
#
######################################################################
from demo import sinaStockRequestor
from models import stockSnapshot

data=sinaStockRequestor.getStockCurrent('sh603129')

for item in data:
    print(item)



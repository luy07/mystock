#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
# Copyright (c) 2017 luy. All Rights Reserved
#
# @author luy(luy007@msn.cn)
#
######################################################################
import sys

class car:
    price=1

    def __init__(self):
        self['price']=999

    def __setitem__(self,**kv):
        :

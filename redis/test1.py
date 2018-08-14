#!/usr/bin/python
#-*-coding:utf-8-*-
from test import RedisHelper

obj = RedisHelper()
obj.publish('this is a test')


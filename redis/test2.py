#!/usr/bin/python
#-*-coding:utf-8-*-

from test import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
#!/usr/bin/python
# -*-coding:utf-8-*-
import redis

#单独链接
# r = redis.Redis(host="127.0.0.1", port=6379, db=0)
# r.set('name', 'liangweile')
# print(r.get('name'))

#链接池链接
# pool = redis.ConnectionPool(host="127.0.0.1", port=6379)
# r = redis.Redis(connection_pool=pool)
# r.set('name', 'liangweile')
# print(r.get('name'))


# pool = redis.ConnectionPool(host="127.0.0.1", port=6379)
# r = redis.Redis(connection_pool=pool)
# pipe = r.pipeline(transaction=True)
# r.set('name', 'liangweile')
# r.set('name', 'lisi')
# pipe.execute()


class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1', prot=6379)
        self.channel = 'liangweile'

    def publish(self, msg):
        self.__conn.publish(self.channel, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub
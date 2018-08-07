#coding:utf-8
import sys
import inspect

def foo():
    pass

class Cat(object):
    def __init__(self, name='kitty'):
        self.name = name

    def sayHi(self):
        print(self.name, 'say Hi')

cat = Cat()

print Cat.sayHi
print cat.sayHi

#1访问对象的属性

cat = Cat('liangweile')
print cat.name
cat.sayHi()

print dir(cat)
if hasattr(cat, 'name'):
    setattr(cat, 'name', 'tiger')
print getattr(cat, 'name')

getattr(cat, 'sayHi')()

import fnmatch as m
print m.__doc__.splitlines()[0]
print m.__name__
print m.__file__
print m.__dict__.items()[0]


print Cat.__doc__
print Cat.__name__
print Cat.__module__
print Cat.__bases__
print Cat.__dict__
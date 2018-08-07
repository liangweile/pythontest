#单例模式的实现方式
#使用模块  定义一个python文件第一次导入时生成pyc文件,第二次导入直接加载pyc文件
#filename:mysingleton.py
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton
#from mysingleton import singleton导入对象

#使用装饰器

def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton
@Singleton
class A(object):
    a = 1
    def __init__(self, x=0):
        self.x = x


#使用类

class Singleten(object):
    def __init__(self):
        pass
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance



#基于__new__方法实现
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, _instance):
            with Singleton._instance_lock:
                if not hasattr(Singleton, _instance):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

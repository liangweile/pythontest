#coding:utf-8

def Foo():
    n = 1
    def bar():
        print n
    n = 2
    return bar

foo = Foo()
# print foo.func_defaults
# print foo.func_code
# print foo.func_globals
print foo.func_closure

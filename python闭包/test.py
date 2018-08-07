class test:
    def fun1(self):
        x = 5
        def fun2():
            nonlocal x
            x += 1
            return x
    return fun2

__closure__#闭包属性 存有变量
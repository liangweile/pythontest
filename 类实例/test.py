#-*-coding:utf-8-*-
#类和实例


#类变量和实例变量
class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name = name
#类Dog中，类属性kind为所有实例所共享；实例属性name为每个Dog的实例独有。

#类对象和实例对象
class Dog:
    pass
# 总的来说，类对象仅支持两个操作：
#
# 实例化；使用instance_name = class_name()的方式实例化，实例化操作创建该类的实例。
# 属性引用；使用class_name.attr_name的方式引用类属性。
#属性绑定objects.attr = attr_value
#类属性绑定
# 类定义时；
# 运行时任意阶段。
class Dog:
    kind = 'canine'
Dog.country = 'China'
# 实例属性绑定
# 与类属性绑定相同，实例属性绑定也发生在两个地方：
#
# 类定义时；
# 运行时任意阶段。

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog = Dog('lily', 3)
dog.fur_color = 'red'



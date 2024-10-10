"""
私有属性和方法的定义和调用方法

类中：
    att        一般属性，无限制
    _att       习惯私有属性，可以获取，但一般不获取
    __att      绝对私有属性，无法直接获取，可以通过 _obj__att 获取
    att_       重名时定义属性的习惯方法
    __define__
    __att__

模块中：
    _xxx       当使用 from module import * 时不会导入，只能通过 from module import _xxx
    __xxx      当使用 from module import * 时不会导入，只能通过 from module import _xxx
    __xxx__
    xxx_       特殊方法名，重名时用该名


"""
class C1:

    y = 2
    _x = 1
    __n = 123
    __y__ = 1234

    def __init__(self, name, age):
        self.name = name
        # 定义私有属性
        # __属性
        self.__age = age
        print(self)

    # 私有方法的定义
    # __方法名
    def __fuck(self):
        self.__age += 20

    def introduce(self):
        print('my name is {0}, i am {1} years old'.format(self.name, self.__age))


c = C1('fuck', 18)
print(c._x)
# print(c.__n)
print(c.__y__)
c.introduce()
# 调用私有方法
# 对象._类名__方法名()
c._C1__fuck()
c.introduce()
# 调用私有属性的方法
# 对象._类名__属性
print(c._C1__age)
print(c._C1__n)
print(dir(c))

print("---------------------------------------")

from test1class类 import *
print(t)
# print(_e)
# print(__mol)

from test1class类 import _t,__t,__t__
print(_t)
print(__t)
print(__t__)
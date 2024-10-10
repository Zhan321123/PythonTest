"""
测试对象和类的某些继承相关的方法
"""


class A:
    a = 'a'

    def aa(self):
        print('aa')


class B(A):
    b = 'b'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bb(self):
        print('bb')


# class.mro()类的继承关系集合
print(B.mro())
# class.__dict__获取类的属性字典
print(B.__dict__)
b = B('zhan', 18)
# object.__dict__获取对象构造器的属性字典
print(b.__dict__)
# object.__dict__获取获取对象的类
print(b.__class__)
# class.__base__获取类的直接父类
print(B.__base__)
# class.__bases__获取类的直接父类元组
print(B.__bases__)
# class.__module__获取类的模块
print(B.__module__)
# class.__subclasses__()获取类的子类集合
print(A.__subclasses__())

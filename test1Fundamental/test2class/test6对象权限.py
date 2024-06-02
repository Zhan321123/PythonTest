"""
私有属性和方法的定义和调用方法

_att       习惯私有属性，可以获取，但一般不获取
__att      绝对私有属性，无法直接获取，可以通过 _obj__att 获取
att_
"""
class C1:

    y = 2
    _x = 1
    __n = 123

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

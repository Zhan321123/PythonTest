"""
正规的写法包含Getter和Setter用来获取和修改数据
1用property注释
2用property方法
"""


class C1:

    def __init__(self, id):
        self.__id = id

    # property注解注释私有属性同名的方法
    @property
    def id(self):
        return self.__id

    # 私有属性.setter注释私有属性同名的方法，可以实现合理修改
    @id.setter
    def id(self, name):
        if name == 'zhan':
            print('please input ready name')
        else:
            self.__id = name


c = C1('xiao')
print(c.id)
# 仍然按照属性的方法修改，实际上是调用了该属性的setter方法
c.id = 'zhan'
print(c.id)

print('*********************')

class C2:
    def __init__(self, age):
        self.__age = age

    def setAge(self, age):
        if isinstance(age, int) and 0 <= age <= 120:
            self.__age = age
        else:
            print('age error')

    def getAge(self):
        return self.__age

    # x = property(getX,setX)将属性的修改方法转为纯修改
    age = property(getAge,setAge)

c = C2(20)
c.age = -10
print(c.age)




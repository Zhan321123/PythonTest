"""
注解property的测试
直接将方法变成属性
调用时按照属性调用，不用()

正规的写法包含Getter和Setter用来获取和修改数据
1用property注释
2用property方法
"""


class Matrix:

    def __init__(self, data: list[list]):
        self.data = data

    # 注解property将方法变成属性
    @property
    def T(self):
        return Matrix([[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))])

    def __str__(self):
        s = ""
        for i in self.data:
            s += str(i) + "\n"
        return s


m = Matrix([[1, 2, 3], [4, 5, 6]])
# 调用注解property的方法可以直接用属性的方法调用
x = m.T
print(x)
print(m.T)

print("--------------getter and setter----------------")


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
    age = property(getAge, setAge)


c = C2(20)
c.age = -10
print(c.age)

"""
def参数的测试

*  序列解包
    可用于方法参数顺序传参
    可用于多对象传值
    可用于交换变量
** 字典解包
    用于对应方法参数名传参
"""


def f1(a, b, c=3, d=4):
    print(a, b, c, d)


f1(1, 2)
f1(1, 2, 5, 6)
f1(1, 2, 7)
f1(b=1, a=2)
f1(a=9, d=1, b=0)


# 注入多个（数量未知）数据类型参数
# *pragma，注入结果转化为元组
# **pragma，注入结果转化为字典
def f2(a=1, b=2, *c):
    print(a, b, c)


f2(1, 2, 3, 4, 5)


def f3(a, b, **c):
    print(a, b, c)


f3(1, 2, name='liu', age='18', id='2022')


def f4(a, *b, **c):
    print(a, b, c)


f4(8, 2, 3, 4, 5, d=1, b=2, c=3)


def f5(*a, b, c):
    print(a, b, c)


f5(1, b=2, c=3)



a = [1, 2, 3]
print(a)
print(*a)
print(1, 2, 3)
x,y,z = a
print(x, y, z)

print("--------------0-----------------")


def add(x, y, z):
    return x + y + z


result = add(*a)
print(result)

print("--------------1-----------------")

b = {'a': 1, 'b': 2, 'c': 3}
print(b)
print(*b)
print(b.keys())
print('a', 'b', 'c')
x,y,z = b.values()
print(x, y, z)

print("--------------2-----------------")


def func(a, b, c):
    return a + b + c


result = func(**b)
print(result)

print("--------------交换变量-----------------")

a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

print("--------------lambda-----------------")
l1 = lambda a, b, c: a * b + c
print(l1(1, 2, 3))
print(l1)

l2 = [lambda a: a ** 2, lambda b: b ** 3, lambda c: c ** 4]
print(l2[0](5), l2[1](6), l2[2](7))
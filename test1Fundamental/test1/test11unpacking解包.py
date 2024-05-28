"""
unpacking object

*  序列解包
    可用于方法参数顺序传参
    可用于多对象传值
    可用于交换变量
** 字典解包
    用于对应方法参数名传参
"""

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

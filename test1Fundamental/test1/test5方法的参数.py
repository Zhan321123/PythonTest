"""
def参数的测试
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

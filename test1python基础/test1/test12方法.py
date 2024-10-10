"""
方法
function.
    __doc__->str，返回解释文档

locals()->dict,返回当前作用域下的变量
globals()->dict,返回全局作用域下的变量

lambda
    快速定义简单的方法
"""
def show():
    print('fuck')


show()
print(type(show))


def fuck(a, b):
    """comparable a and b"""
    if a > b:
        print(a)
    else:
        print(b)


fuck(3, 7)
fuck('a', 'b')
# 获取函数下的解释文档
help(fuck.__doc__)


def shit(a, b, c, d):
    for i in range(0, d):
        if i % 3 == 0:
            a += b
        elif i % 3 == 1:
            b += c
        else:
            c += a
    return a + b + c


print(shit(1, 2, 3, 100))

print("---------1------------------")
def get():
    a=300
    print(a)

    print(locals())
    print(globals())
    print('########################')
    for i in globals():
        print(i)

get()

print("--------将方法作为参数传递-----------")
import time
# 函数当参数用测试函数效率
def efficiency(function):
    t1 = time.time()
    function()
    t2 = time.time()
    return t2 - t1


def f1():
    a = 100
    for i in range(0, 10 ** 7):
        a += 100
    print(a)


a = 100


def f2():
    global a
    for i in range(0, 10 ** 7):
        a += 100
    print(a)


print(efficiency(f1))
print(efficiency(f2))

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

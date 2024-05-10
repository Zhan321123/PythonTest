"""
关键字global和nonlocal
内层调用外层对象的声明
"""
def outer():
    a = 10

    def inner():
        # nonlocal 外层函数的变量
        # 相当于外部函数的global
        nonlocal a
        a = 20
        print('inner:', a)

    inner()
    print(a)


outer()

# 用global声明之后不能
a = 100


def f1():
    global a
    b = 300

    def f2():
        # 用global声明外部函数global声明的变量
        global a
        a = 200
        print(a)
        nonlocal b
        b=400
        print(b)

    f2()

    print(a)
    print(b)


f1()

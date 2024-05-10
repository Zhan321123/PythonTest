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

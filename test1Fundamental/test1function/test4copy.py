from copy import copy, deepcopy

"""
浅拷贝copy
深拷贝deepcopy
"""
a = 100


# 传入参数为不可变对象时，修改会创建新的对象
def f1(n):
    print('id(n):', id(n))  # 传入的参数n的地址
    n += 100
    print('id(n)', id(n))  # 新的对象n


f1(a)
print('id(a)', id(a))

# 测试copy

# 浅拷贝
a = [1, 2, 3, ['a', 'b', 'c']]
a1 = copy(a)
# 不是直接把b=a，而是指向a的堆，并创建新的地址
print(a1 is a)
a1.append(4)
print(a1)
print(a)
# 直接改变a内容的地址
a[2] = 100
print(a)
print(a1)
# 没有改变a的内容的地址
a[3][0] = 'z'
print(a)
print(a1)

# 深拷贝
a2 = deepcopy(a)
print(a2 is a)
a[1] = 10000
a[3][0] = 'asd'
a2[2] = 3
a2[3][1] = 't'
print(a)
print(a2)

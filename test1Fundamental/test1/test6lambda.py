"""
lambda的测试
快速定义简单的方法
"""
l1 = lambda a, b, c: a * b + c
print(l1(1, 2, 3))
print(l1)

l2 = [lambda a: a ** 2, lambda b: b ** 3, lambda c: c ** 4]
print(l2[0](5), l2[1](6), l2[2](7))

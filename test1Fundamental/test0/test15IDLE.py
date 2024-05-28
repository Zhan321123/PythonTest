"""
原生IDLE和Pycharm产生的差别

1 整数池
IDLE中只会存储一定数量的整数
pycharm中不需要

2 导入模块后模块内容发生变化
IDLE中需要reload module
pycharm中不需要

"""

# 数字的地址
a = 10
b = 10
print(a is b)
a = 10000000000000000000000000
b = 10000000000000000000000000
print(a is b)
# 在pycharm中为True，在IDLE中为False
# 因为IDLE中的小整数池范围为[-5,256]

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 == list2)
"""
enumerate函数
    用于序列遍历时的数字索引
    enumerate(list) = ((0, e1), (1, e2), ...)
    for index, e in Sequence:



"""

a = 'abcd'
for i in a:
    print(i)
for index, i in enumerate(a):
    print(f"第{index}个字符为：{i}")

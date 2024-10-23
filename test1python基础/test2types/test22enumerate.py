"""
enumerate函数
    用于序列遍历时的数字索引

for e1 in list:
for index,e2 in enumerate(list):
    e1 == e2
"""

a = 'abcd'
for i in a:
    print(i)
for index, i in enumerate(a):
    print(f"第{index}个字符为：{i}")

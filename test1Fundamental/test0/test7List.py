import random
"""
列表list的测试
可删减的列表
"""
a = list()
print(a)
b = []
print(b)
# list()，将任何可以迭代的数据类型转化为列表
a = range(0, 10)
print(a)
print(list(a))

# range[(start=0,) end (step=1,))
list1 = [x ** 2 for x in range(1, 6)]
print(list1)
list2 = [x ** 2 for x in range(1, 100) if x % 9 == 0]
print(list2)

# 关于列表相加的内存机制
a = [1, 2]
id1 = id(a)
# list=list+newList，会创建新对象
a = a + [3, 4]
id2 = id(a)
print(id1 == id2)
# 不会创建新对象
# list+=newList
# list.extend(list)
# list.append(element)
a += [5, 6]
print(id2 == id(a))
a.extend([7, 8])
print(id2 == id(a))
a.append(9)
print(id2 == id(a))

# list方法
a = [0, 1, 1, 2, 3, 1, 4, 5, 8, 2, 6, 5, 1, 9, 0]
# 插入element
a.insert(2, 'asd')
print(a)
# 删除element
del a[2]
print(a)
# 删除顶部element
print(a.pop())
print(a)
# 删除首次出现的element
a.remove(1)
print(a)
# 查找首次出现元素的索引
# list.index(element[,start[,end]])
print(a.index(1))
print(a.index(1, 2))
# 出现次数
print(a.count(1))
# 是否含有
print(4 in a)
# 遍历
for i in a:
    print(i)
# 排序
a.sort()  # 升序
print(a)
a.sort(reverse=True)  # 降序
print(a)
random.shuffle(a)  # 打乱
print(a)
b = sorted(a)  # 升序，创建新对象
c = sorted(a, reverse=True)  # 降序，创建新对象
print(id(a) == id(b))
# 迭代器
a = [5, 6, 4, 7, 3, 7]
b = reversed(a)
print(b)
print(list(b))
# 求和
print(sum(a))

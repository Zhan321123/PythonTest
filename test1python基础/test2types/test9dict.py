"""
字典dict的测试
包含一一对应的关系key：value
key不可重复
"""
# 创建字典的方式
a = {'name': 'zhan', 'age': 18, 'id': 2022}
print(a)
b = dict(name='zhan', age=18, id=2022)
e = dict()
f = {}
# 通过两个元素的元组创建字典
t1 = ('name', 'zhan')
t2 = ('age', 18)
t3 = ('id', 2022)
l = [t1, t2, t3]
d = dict(l)
# 通过zip两个列表创建字典
l1 = ['name', 'age', 'id']
l2 = ['zhan', 18, 2022]
a = dict(zip(l1, l2))
print(a)
# 创建value为none的字典
g = dict.fromkeys(['name', 'age', 'id'])
print(g)

# 获取元组数据
print(a.get('name'))
print(a['name'])
print(a.get('sex'))
print(a.get('sex', 'no exist'))
print(len(a))

# 遍历
print(a.items())
# 获取所有key
print(a.keys())
print(list(a.keys()))
for i in a.keys():
    print(a[i])

# 修改字典
# 添加和修改
a['sex'] = 'male'
a['name'] = 'zhang'
print(a)
# 删除
del a['name']
print(a)
# 覆盖
b = {'name': 'xiao', 'sex': 'female', 'degree': 'doctor'}
b.update(a)
print(a)
print(b)
# 全删
b.clear()
print(b)
# pop()指定弹出
print(a.pop('sex'))
print(a)
# popitem()随机弹出
print(a.popitem())
print(a)


# 集合，相当于字典的key，不可重复，无顺序
a = {1, 2, 3}
print(a)
# 添加删除元素
a.add(4)
a.add(1)
print(a)
a.remove(1)
print(a)
a.clear()
print(a)
# set()将可迭代对象转化为集合，相同数据会保留一个
b = [1, 2, 3]
a = set(b)
print(a)

# 集合的并集、交集、差集
a = {1, 2, 3}
b = {2, 3, 4}
# 并集
print(a | b)
print(a.union(b))
# 交集
print(a & b)
print(a.intersection(b))
# 差集
print(a - b)
print(a.difference(b))

print("-----------应用--------------")
import random

for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + '*' + str(i) + '=' + str(i * j), end='\t')
    print()

# for下的else，当for语句没有被break时，else会执行
for i in range(1, 11):
    a = random.randint(0, 10)
    print(a)
    if a == 5:
        break
else:
    print('successful')

#
a = ('zhan', 'xiao', 'duo')
b = (12, 34, 56)
c = ('male', 'female', 'male')
for i, j, k in zip(a, b, c):
    print('{0}-{1}-{2}'.format(i,j,k))
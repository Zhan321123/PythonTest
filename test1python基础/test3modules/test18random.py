"""
random
"""
import random

# 设置随机数种子
random.seed(100)

# (a,b) [a,b]中随机整数
print(random.randint(0,10))
# 产生[0,1)中的随机数
print(random.random())
# 产生range(start,end,step)中的一个随机数
print(random.randrange(0,100,10))
# 产生[a,b]中的一个随机数
print(random.uniform(0,10))

a = ['a','b','c','d']
b = ('z','x','c','v')
# 中序列中随机选一个元素
print(random.choice(a))
print(random.choice(b))
print(random.choice('qwer'))

# 随机打乱序列
random.shuffle(a)
print(a)
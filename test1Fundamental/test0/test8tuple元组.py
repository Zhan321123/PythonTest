"""
元组tuple的测试
长度len不可变
"""
a = (1, 2, 3,)
print(type(a))
print(len(a))
# 创建一个元素的元组的方法
b = ('a')
print(type(b))
b = ('a',)
print(type(b))
# 细节注意1
b = tuple
print(type(b))
b = tuple()
print(type(b))
b = ()
print(type(b))
# 细节2
b = tuple('string')
print(b)
b = tuple('string', )
print(b)
b = ('string',)
print(b)
b = list('string')
print(b)
b = tuple(range(5))
print(b)

# sorted
a = tuple('abcdefghijklmnopqrstuvwxyz')
print(a)
print(a[::-1])
b = sorted(a)
print(b)

# 加法操作
a = (1, 2, 3)
b = ('a', 'b')
c = a + b
print(a)
print(b)
print(c)

# zip
d = zip(a, b, c)
print(d)
print(list(d))

# 生成器
s = (x ** 2 for x in range(6))
a = tuple(s)
print(a)
# 生成器只能用一次，第二次就成了
b = tuple(s)
print(b)

print("------------1--------")
a = tuple((x, y) for x in range(1, 17) for y in range(1, 17))
for i in range(0, 16):
    for j in range(0, 16):
        print(a[i * 16 + j], end='  \t')
    print()

print("----------句子的词频统计----------")
s = 'x am zhan, x love minecraft, x dont love family'
a = tuple(s)
char={i:s.count(i) for i in s}
print(char)

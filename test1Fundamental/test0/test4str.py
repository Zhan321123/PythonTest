import time
"""
字符串str的测试
"""
# 用'\'换行续写
a = 'abcdefg\
hijklmn\
opqrst\
uvwxyz'
print(a)

# 用r，让转移字符失效
r'\t'

# 对象地址
print(id(a))
# 对象类型
print(type(a))

# 回收对象
del a
# print(a)

# /浮点除法，//整数除法
# *乘法，**幂

#
print(divmod(20, 6))

#
print(int('123'))

print(time.time())
print(time.ctime())

# unicode编码
print(ord('刘'))
print(ord('高'))
print(ord('瞻'))

# ‘’‘字符串’‘’
a = '''liu say:"what are you doing"'''
print(a)

# 字符串长度
print(len(a))

# print函数
print('abc', end=' ok! \n')

# replace函数
b = 'abababab'.replace('a','b')
print(b)

# 字符串的提取
print(a[:])
print(a[5:]) #[start:]
print(a[:10]) #[0:end]
print(a[3:6]) #[start:end]
print(a[2:10:2]) #[start:end:step]
print(a[::2]) #[0::step]
print(a[10::3])
# 反转str
print(a[len(a)::-1])
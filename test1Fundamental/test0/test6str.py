import io

a = 'abcdefggfedcba'
print(a.startswith('abc'))
print(a.endswith('cba'))
print(a.find('a'))
print(a.rfind('a'))
print(a.find('z'))
print(a.count('g'))
# 是否全是字母和数字
print(a.isalnum())

# 清除前后字符
c = '** 123*'
print(c.strip('*'))
print(c.lstrip('*'))
print(c.rstrip('*'))
b = ' 123asd ddd '
# 去掉前后空格
print(b.strip())
print(b)

d = 'I love you very much'
# 大写句子首字母
print(d.capitalize())
# 大写单次首字母
print(d.title())
# 大写所有字母
print(d.upper())
# 小写所有字母
print(d.lower())
# 大写变小，小写变大
print(d.swapcase())
# 都会产生新的对象

# 字符串居中，不够填充
print('LGZ'.center(9, '*'))
print('lgz'.center(9))

# 检测字符串含有
# 字母和数字
print('abc123'.isalnum())
# 字母和汉字
print('asd瞻'.isalpha())
# 数字
print('123'.isdigit())
print('1.23'.isdigit())
# 空格
print(' \n \t'.isspace())
# 大写字母
print('ASD'.isupper())
# 小写字母
print('asd'.islower())

# 格式化字符串
s1 = 'My name is {0}, I am {1} years old, {0} is beautiful'
print(s1.format('zhan', 12))
s2 = 'My name is {name}, I ma {age}, {name} is a good boy'
print(s2.format(age='18', name='zhan', dd=''))
# {参数:填充字符+居中^或居左<或居右>+字符数}
print('your name is {0:*^8},your age is {1: >10}'.format('zhan', 12))
# 格式
print('{0:.3f}'.format(123.456789))
print('{0:.1%}'.format(0.123456))

# 字符串的修改
s = 'hello, zhan'
sio = io.StringIO(s)
print(sio.getvalue())
print(sio.seek(9))
print(sio.write('e'))
print(sio.getvalue())

# 连续比较
print(1 < 2 < 3 < 4)
# 将数字转为二进制
print(bin(34))
# 字符串乘法
print('zhan '*3)
# 列表乘法
print(['liu','gao','zhan']*3)
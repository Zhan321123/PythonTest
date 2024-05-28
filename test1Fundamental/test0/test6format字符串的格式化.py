"""
string's format

"""
import io

# 格式化字符串
s1 = 'My name is {0}, I am {1} years old, {0} is beautiful'
print(s1.format('zhan', 12))
s2 = 'My name is {name}, I ma {age}, {name} is a good boy'
print(s2.format(age='18', name='zhan', dd=''))
print(f"{io} hello")
# {参数:填充字符+居中^或居左<或居右>+字符数}
print('your name is {0:*^8},your age is {1: >10}'.format('zhan', 12))

print("-----------格式-------------")
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
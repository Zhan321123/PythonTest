"""
进制转换
"""
n = 100
# 将数字转化为2进制的字符串
b = bin(n)
# 0b开头为二进制数字
print(type(b))
print(b)

c = 0b101010
print(type(c))

# 2进制转10进制int('binary',2)
a = int(b, 2)
print(a)

print('********************')

# 10进制转2进制
def toBinary(n):
    l = []
    while n != 0:
        l.append(str(n % 2))
        n = int(n / 2)

    return '0b'+''.join(l[::-1])

# 2进制转10进制
def toInt(s):
    n = 0
    s = s[2:len(s)][::-1]
    for i in range(0, len(s)):
        n += int(s[i]) * (2 ** i)
    return n


print(toInt(bin(1000)))
print(toBinary(1000))
print(toInt(toBinary(2000)))

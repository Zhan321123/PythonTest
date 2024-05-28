"""
str.
    replace(str,new str)，替换字符
    split()->list[str]，分割字符，返回字符串列表，以空格为分割
    split(str)->list[str]，分隔字符，以str为分割，结果不含str
    join(list[str2])->str，返回str+str2[0]+str+str2[1]+...，效率高

    startswith(str)->boolean
    endswith(str)->boolean
    find(str)->int，从左向又查找，返回str的位置，找不到返回-1
    rfind(str)->int，从右向左查找，返回str在str中的位置，找不到返回-1
    count(str)->int，返回str在str中的个数

    isalnum()->boolean，判断是否全为字母和数字
    isalpha()->boolean，是否全为字母
    isdigit()->boolean，是否全为数字
    isspace()->boolean，是否全为空格
    isupper()->boolean，是否全为大写
    islower()->boolean，是否全为小写


    strip(str)->str，去除左右str，不填为空格
    lstrip(str)->str，去除左边str
    rstrip(str)->str
    capitalize()->str，首字母大写
    title()->str，每个单词首字母大写
    upper()->str，全部大写
    lower()->str，全部小写
    swapcase()->str，大小写转换
    center(int, str)->，将str居中，用str填充int个，不填str为空格

len(str)返回字符长度
id(object)返回对象的内存地址
type(object)返回对象的类型

str[start:end:step]字符切片

字母""
    r转义字符失效
    b转为二进制
    f格式化字符串

ord编码
    ord(str)->int返回字符的unicode编码

表示str类型：
    ‘’
    “”
    “”“”“”

"""

print(ord('a'))

a = 'abc'
a = "abc"
a = """abc"""
# 用r，让转移字符失效
b = r'\t'
print(b)

# 对象地址
print(id(a))
# 对象类型
print(type(a))
# 字符串长度
print(len(a))

# replace函数
b = 'abababab'.replace('a', 'b')
print(b)

print("-----------字符串的提取------------")
print(a[:])
print(a[5:])  # [start:]
print(a[:10])  # [0:end]
print(a[3:6])  # [start:end]
print(a[2:10:2])  # [start:end:step]
print(a[::2])  # [0::step]
print(a[10::3])
# 反转str
print(a[len(a)::-1])


print("----------字符串驻留机制--------------")
a='abc_123'
b='abc_123'
print(a is b)
a='h@1#'
b='h@1#'
print(a is b)

print('a' in 'abc')
print('a' not in 'abc')
print(not 'a' in 'abc')

print('-----------split--------------')
a = 'to be or not to be, do you know!'
for i in a.split():
    print(i)
print(a.split('to'))

print('-----------join--------------')
l=['a','b','c','d']
print('*'.join(l))

print('-----------other--------------')
a = 'abcdefggfedcba'
print(a.startswith('abc'))
print(a.endswith('cba'))
print(a.find('a'))
print(a.rfind('a'))
print(a.find('z'))
print(a.count('g'))
# 是否全是字母和数字
print(a.isalnum())

print("-----------str函数--------------")
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

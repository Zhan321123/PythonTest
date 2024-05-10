import time

a = 'to be or not to be, do you know!'
# 分割字符串的单次，返回[]
for i in a.split():
    print(i)

print(a.split('to'))

list=['a','b','c','d']
print('*'.join(list))
print('*'.join(a.split()))

# 效率测试
# str+测试效率
time1=time.time()
s=''
for i in range(1000000):
    s+=str('liugaozhan')
time2=time.time()
print(time2-time1)
# join函数效率
time1=time.time()
s=''
list=[]
for i in range(1000000):
    list.append('liugaozhan')
s.join(list)
time2=time.time()
print(time2-time1)

# 字符串驻留机制
a='abc_123'
b='abc_123'
print(a is b)
a='h@1#'
b='h@1#'
print(a is b)

print('a' in 'abc')
print('a' not in 'abc')
print(not 'a' in 'abc')
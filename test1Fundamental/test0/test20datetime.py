"""
测试datetime包中的datetime和timedelta
"""
import datetime

# 获取当前日期
n = datetime.datetime.now()
print(n)

# 新建日期时间
d = datetime.datetime(2004,8,28)
print(d)
print(d.year)

# 日期的计算
a = n-d
print(type(a))
print('now you live{0} '.format(a))

a = datetime.timedelta(100)
print(a)
d = datetime.datetime.now()+a
print(d)
"""
测试time
"""
import time
# 现在的时间戳
print(time.time())

# 本地时间对象，class=struct_time
t = time.localtime()
print(t)
print(type(t))
# 获取时间
print('now is {0} year {1} month {2} day'.format(t.tm_year,t.tm_mon,t.tm_mday))

# 转化时间为易读的字符串
print(time.ctime())

# 格式化时间字符串
# %对应的时间
print(time.strftime('%Y--%m--%d, %H:%M:%S',time.localtime()))

print(time.strptime('2024 year 2 month 16 day','%Y year %m month %d day'))

# 线程休息秒数
time.sleep(5)
print('thread sleep 5 seconds')


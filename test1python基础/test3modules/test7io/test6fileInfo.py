"""
用os获取文件属性信息
st_size文件大小，多少byte
st_ctime文件创建时间

用os打开文件
"""
import os

info = os.stat('file/a.txt')
print(type(info))
print(info)

print (info.st_size/1024,'kB')


os.startfile('calc.exe')
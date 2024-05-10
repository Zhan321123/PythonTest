"""
os.path模块
"""
import os.path as op

# abspath获取文件绝对路径
print(op.abspath('file/a.txt'))
# exists判断文件或文件夹是否存在
print(op.exists('file/a.txt'))
print(op.exists('file'))
# splitext分离文件名和后缀名
dirs, suffix = op.splitext('file/a.txt')
print(dirs, suffix)
# basename从目录中提取文件名
print(op.basename('file/a.txt'))
# dirname从目录中提取目录名
print(op.dirname('file/a.txt'))
# join拼接路径和文件名
print(op.join('file','a.txt'))
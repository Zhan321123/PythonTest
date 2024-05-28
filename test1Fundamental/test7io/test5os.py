"""
os模块的使用
"""
import os

# getcwd获取模块的路径
print(os.getcwd())
# listdir获取模块所在文件夹的所有文件和文件夹
l = os.listdir()
print(l)
print(os.listdir('../test1'))

# mkdir创建文件夹，只能创建单层文件夹
# 如果有该文件夹，则会异常
os.mkdir('file2')

# makedirs创建文件夹，可以是多层
# 如果最后一个文件夹存在，则会异常
os.makedirs('file/file2/file3/file4')

# 删除文件夹，不能是文件，且文件夹必须为空
os.rmdir('file2')
os.removedirs('file/file2/file3/file4')

# chdir 改变当前工作目录
os.chdir(os.getcwd())
# walk获取文件夹遍历树元组
for dirs,dirlist,filelist in os.walk(os.getcwd()):
    print(dirs)
    print(dirlist)
    print(filelist)
    print('--------------------------')

# 删除文件，非文件夹
# os.remove('file/b.txt')
# 重命名文件或文件夹
# 也会更改路径
# os.rename('file','files')
# os.rename('file/a.txt','b.txt')
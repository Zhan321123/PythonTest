"""
测试文件夹的路径问题
"""

# 绝对路径
open('D:/code/pythonProject/Test/test1Fundamental/test7io/file/a.txt')
# 相对路径之后
open('file/a.txt')
# 相对路径之前，...../，点的个数表示表示退回几层文件夹
open('./file/a.txt')
open('../test7io/file/a.txt')
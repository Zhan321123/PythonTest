"""
导入其他项目的模块
一：
手动在导入包对象的导入目录添加
sys.path.append('module package')
二：（导入模块）
（1）（正规的方法）
    将创建出的'name'-'version'.tar.gz解压
    进入解压的界面，该界面应当有setup.py，打开cmd
    执行命令python setup.py install --prefix='install path'
（2）（暴力方法，包小的时候方便完成）
    将包拖曳到外部库的site-packages下
注意：
外部库下的python下的site-packages是系统库，不在python的安装目录，但可以在所有正在写的模块使用该库下的模块
当要删除包时，直接右键删除即可
"""

# sys引入的包
import sys
# sys.path，包的目录
l = sys.path
print(type(l))
for i in l:
    print(i)

# 手动加入包
# 然后导入即可
sys.path.append('*/*/*/*')
print(sys.path)
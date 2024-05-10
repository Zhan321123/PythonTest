"""
模块的导出：
    一：
创建setup.py
在该py导入 from distutils.core import setup
执行set(name, version, author, description, py_modules=[module1,module2...],)
    二：
将setup.py和要导出的模块放到一个文件夹中
在该文件夹中打开cmd
执行python setup.py build创建出build文件夹
    三：
执行python setup.py sdist创建出dist文件夹，包含'name'-'version'.tar.gz
"""
from distutils.core import setup
setup(name='自定义压缩包1',version='1.0',author='zhan',py_modules=['test3module.test3package',])
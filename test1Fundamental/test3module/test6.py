"""
测试下划线标注的属性导入
    _xxx
导入*时不会导入该属性
    __xxx
私有属性
会改名为_class__xxx
    __xxx__
特殊方法名
    xxx_
重名时用该名
"""

from test6test import *
print(pi)
# print(_e)
# print(__mol)

from test6test import _e,__mol
print(_e)
print(__mol)

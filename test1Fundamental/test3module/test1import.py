"""
测试模块的导入
导入模块时会执行module中的非main主程序，多次导入时只会执行一次

    一：
import module,module
导入模块
使用时 module.object
    二：
from module import object1,class2
导入模块的具体object
使用时 object，不用module.
    三：
from module import *
默认导入模块的所有object
当module中有__all__列表时导入的未all中的str对应的object
不建议在python3中使用__all__
    四：
from package import *
执行package下__init_.py，所以包括init导入的内容，导入包下所有模块
在init模块中导入自己包from .module import ...
使用时 module.object
"""

# import module1,module2
import random, math

print(math.sin(0))
print(random.randint(1, 10))

# from module import object
from test0 import add

print(add(2, 3))

import test0

print(test0.divide(3, 4))

# from module import class
from test0 import C1

c = C1(100)
c.fuck()

# from module import *
# 默认导入模块的所有object
# 当module中有__all__列表时导入的未all中的str对应的object
from test0 import *
print(divide(1, 2))
# print(multiply(2,3))


from test3package.test0 import *
print(add(2,3))

import test3package.test0
print(test3package.test0.add(3,4))


from test3package import *
print(add(7, 8))
# print(divide(4,2))
print(test0.divide(9,3))
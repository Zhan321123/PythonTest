"""
模块会默认导入builtins

sys存储模块的模块
sys.path所有导入的模块的路径
sys.path.append('要导入的模块')
"""

import sys
for i in sys.path:
    print(i)

sys.path.append('导入路径')
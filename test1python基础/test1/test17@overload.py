"""
@overload方法重载器
    但是只是指定了不同的类型,然后可以查看类型提示，仅此而已
    仍然要自己不停判断变量类型
"""
from typing import overload


class Li:
    def __init__(self, li=[]):
        self.li = li

    @overload
    def __getitem__(self, item: int) -> float:
        ...

    @overload
    def __getitem__(self, item: slice) -> list:
        ...

    @overload
    def __getitem__(self, item: [bool]) -> list:
        ...

    # 这里仍然要一直判断类型
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.li[item]
        elif isinstance(item, slice):
            return self.li[item]
        elif isinstance(item, list):
            if isinstance(item[0], bool):
                return [self.li[i] for i in range(len(self.li)) if item[i]]
            elif isinstance(item[0], int):
                return [self.li[i] for i in item]


l = Li([1, 2, 3, 4, 5])
a = l[0]
b = l[0:2]
c = l[[True, False, True, False, True]]

# 这里就有了类型提示
print(a)
print(b)
print(c)

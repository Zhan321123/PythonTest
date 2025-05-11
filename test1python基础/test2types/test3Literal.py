"""
Literal

字符串字面量类型
"""
from typing import Literal


def s(t:Literal["a", "b"]):
    if t == "a":
        print("a")
    elif t == "b":
        print("b")
    else:
        raise ValueError(f'type: {t}')

s('a')
s('b')
s('c')
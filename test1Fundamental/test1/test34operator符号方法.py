"""
重写运算符的方法，使对象可以用符号运算
符号对应方法：
+     __add__
-     __sub__
*     __mul__
/     __div__
//    __floordiv__
**    __pow__
[]    __getitem__
%     __mod__
&     __and__
|     __or__
^     __xor__
<<    __lshift__
>>    __rshift__
~     __invert__
!=    __ne__
==    __eq__
<     __lt__
<=    __le__
>     __gt__
>=    __ge__


"""
class Fraction:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return self.value + other.value
        elif isinstance(other, int):
            return self.value * other
        else:
            return "can't mul"


f1 = Fraction('1/2')
f2 = Fraction('2/3')
print(f1 * f2)
print(f1 * 3)

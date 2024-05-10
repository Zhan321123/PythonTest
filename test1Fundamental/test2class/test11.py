"""
重写运算符的方法，使对象可以用符号运算
符号对应方法：
+     __add__
-     __
*     __mul__
/     __
**    __


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

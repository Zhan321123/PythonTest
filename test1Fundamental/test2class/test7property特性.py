"""
注解property的测试
直接将方法变成属性
调用时按照属性调用，不用()
"""
class Matrix:

    def __init__(self,data:list[list]):
        self.data = data
    # 注解property将方法变成属性
    @property
    def T(self):
        return Matrix([[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))])

    def __str__(self):
        s = ""
        for i in self.data:
            s += str(i) + "\n"
        return s


m = Matrix([[1,2,3],[4,5,6]])
# 调用注解property的方法可以直接用属性的方法调用
x = m.T
print(x)
print(m.T)
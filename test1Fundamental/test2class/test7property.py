"""
注解property的测试
直接将方法变成属性
调用时按照属性调用，不用()
"""
class C:

    # 注解property将方法变成属性
    @property
    def say(self):
        print('fuck you')
        return 1000



c = C()
# 调用注解property的方法可以直接用属性的方法调用
print(c.say)
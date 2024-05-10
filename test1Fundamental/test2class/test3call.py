"""
类中的call方法
对象变成方法使用时执行
"""
class Stu:

    # call，对象变成方法使用时执行
    def __call__(self, *args, **kwargs):
        print('call method')


s1 = Stu()
# 这里直接将对象变成方法使用
s1()

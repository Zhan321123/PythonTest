"""
测试方法的重载
python中没有方法的重载，只会执行最后一个同名的方法
"""

class Stu:
    def fuck(self):
        print('fuck')

    def fuck(self,name):
        print(name+'fuck')


s1 = Stu()
# s1.fuck()
s1.fuck('zhan')
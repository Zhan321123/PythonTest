"""
自定义异常
class 类型Exception(继承一个异常类):
    def __init__(self):
        super().__init__()最好执行父类的构造器
"""


class GenderException(Exception):
    def __init__(self):
        super().__init__()
        self.message = 'gender error'


class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def setGender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise GenderException()

    def __str__(self):
        return 'my name is {0}, i am {1}'.format(self.name, self.__gender)


s = Student('zhan', 'male')
try:
    s.setGender('male or female')
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.message)
print(s)

"""
对象的基本
"""
class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def say(self):
        return self.name + ' fuck you'


s1 = Student('zhan', 120, 2022)
print(s1.say())
print(s1.name)
s1.age = 12
print(s1.age)

# 解释器调用方法：class.method(对象self)
print(Student.say(s1))

# dir获取该对象类的所有方法和属性
for i in dir(s1):
    print(i)
print(dir(s1))


class Genshin:
    pass


print(isinstance(s1, Student))
print(isinstance(s1, Genshin))

print(type(s1))
print(type(Student))

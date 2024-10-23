"""
iter test

next(iterator)输出一个迭代器中的下一个元素

"""
# 将序列转换为迭代器：
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration as e:
    print(e)

# 将迭代器转换为序列：
iterator = iter(numbers)
l = list(iterator)
print(l)

iterator = iter(numbers)
s = set(iterator)
print(s)

# iter(object)，object必须是可迭代对象
try:
    iterator = iter(1)
except TypeError as e:
    print(e)

# iter读取文件方法
with open("../file/ttt.txt", "r") as file:
    for line in iter(file.readline, ""):
        print(line, end="")

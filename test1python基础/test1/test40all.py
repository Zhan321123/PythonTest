"""
all()

all(iterable)

"""
# 列表示例
print(all([True, True, True]))  # 输出: True
print(all([True, False, True])) # 输出: False

# 字符串示例，空字符串视为False
print(all("hello"))            # 输出: True
print(all(""))                 # 输出: False

# 判断列表中的所有数字是否都大于0
numbers = [1, 2, 3, 4]
print(all(x > 0 for x in numbers)) # 输出: True

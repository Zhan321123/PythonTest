"""
all([bool]) -> bool
"""
# 列表示例
print(all([True, True, True]))  # 输出: True
print(all([True, False, True])) # 输出: False

print("---------判断列表元素是否都大于0------------")
numbers = [1, 2, 3, 4]
print(all(x > 0 for x in numbers)) # 输出: True

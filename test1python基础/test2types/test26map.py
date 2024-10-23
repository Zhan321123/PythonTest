"""
map object test
function:
批量处理：对可迭代对象中的每个元素应用相同的处理逻辑。
类型转换：常见用途之一是进行类型转换，如将字符串列表转换为整数列表。
函数应用：无需显式循环，直接应用函数到序列的每个元素上。
并行计算友好：虽然标准库中的map()不直接支持并行计算，但其概念易于扩展到并行处理场景中，如使用multiprocessing.Pool.map()。
"""
# 将一个整数列表中的每个元素平方。
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 输出: [1, 4, 9, 16]

# 将一个字符串列表转换为整数列表。
str_numbers = ['1', '2', '3']
int_numbers = map(int, str_numbers)
print(list(int_numbers))  # 输出: [1, 2, 3]


# 假设有一个函数用于计算字符串长度，使用map()计算列表中每个字符串的长度。
def string_length(s):
    return len(s)


words = ["apple", "banana", "cherry"]
lengths = map(string_length, words)
print(list(lengths))  # 输出: [5, 6, 6]

# exchange two objects' mapping
a = 1
b = 2
a, b = b, a
print(a, b)

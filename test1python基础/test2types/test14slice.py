"""
slice(start, end, step)，切片，含start，不包含end，步长维step
    不能转化为list

"""


l = [1,2,3,4,5]
s = slice(1, 13, 2)
print(s)
print(l[s])

"""
用json模块读取和写入高维数组
"""
import json

l = [
    {'name':'zhan','age':18,'id':2022,'hobby':('minecraft','study')},
    {'name':'xiao','age':17,'habit':'f','marry':False},
    {'name':'duo','id':2025,'marry':True}
]

# dumps读取高维序列，返回好看的string
# Ascii不包含中文，不填False会乱码
# indent换行时缩进空格数
s =json.dumps(l,ensure_ascii=False,indent=4)
print(s)
print(type(s))

# json解码，相当于把json文件转为序列对象
l2 = json.loads(s)
print(l2)
print(type(l2))

# 编码到文件中
with open('file/json1.json','w') as file:
    json.dump(l,file,ensure_ascii=False,indent=1)

# 读取json文件
with open('file/json1.json','r') as file:
    j = json.load(file)
    print(type(j))
    print(j)
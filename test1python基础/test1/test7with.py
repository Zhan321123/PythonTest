"""
with关键字
文件操作，使语句更好看，更简单
不用close
"""


with open('file/a.txt','r') as file:
    print(file.read())

def copy():
    with open('file/a.txt','rb') as file:
        with open('file/b.txt','wb') as file2:
            file2.write(file.read())

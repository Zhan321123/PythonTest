"""
测试文件的写入和读取

    一、操作模式
r       只读，指针在开头，文件不存在则异常
w       覆写，文件不存在则创建，文件存在则内容覆盖
rb      只读模式打开二进制文件
wb      覆写模式写入二进制数据
a       追加，在文件最后追加文件不存在则创建
+       与w、r、a等一同使用，在原功能基础上增加同时读写功能

    二、具体操作
read(n)             读取n个字符或字节，无n则读取全部
readline(n)         读取一行数据中的n个字节字符，无n则读取完整一行
readlines()         读取所有行，返回每行的数据成一个列表
write(string)            写入字符串s
writelines(list)    将序列写入文件，不会换行
seek(位置offset)        移动指针位置，english占一个字节，中文gbk占2个字节，utf-8占3个字节

"""
def write():
    # open(文件及路径filename,操作模式,编码encoding)，创建打开文件对象，
    file = open('file/a.txt','w',encoding='utf-8')
    # write写入操作
    file.write('abcdefghijklmnopqrstuvwxyz')

    file.writelines(('fuck','you','do','you','know'))

    # file.flush()

    # 关闭文件对象
    file.close()


def read():
    file = open('file/a.txt','r',encoding='utf-8')
    # read读取操作
    print(file.read())
    file.close()

def writeAndRead():
    file = open('file/a.txt','w+',encoding='utf-8')
    file.write('fuck you everyone')
    # 移动光标
    file.seek(2)
    # 将光标移到前面写不是插入，而是覆写
    file.write('hello,zhan')
    file.seek(0)
    print(file.read(5))
    file.close()

if __name__ == '__main__':
    write()
    read()
    writeAndRead()
r"""
文件写入和读取
    file = open(filePath:str, 读写模式:str, encoding='utf-8') 打开文件启动模式

读写模式
    r       只读，指针在开头，文件不存在则异常
    w       覆写，文件不存在则创建，文件存在则内容覆盖
    rb      只读模式打开二进制文件
    wb      覆写模式写入二进制数据
    a       追加，在文件最后追加文件不存在则创建
    +       与w、r、a等一同使用，在原功能基础上增加同时读写功能

file.
    write(string),写入字符串s，根据读写模式来确定是覆写还是追加和什么位置
    writelines(list),将序列写入文件，不会换行和空格
    flush(),刷新缓冲区

    readlines(),读取所有行，返回每行的数据成一个列表
    read(n),读取n个字符或字节，无n则读取全部
    readline(n),读取一行数据中的n个字节字符，无n则读取完整一行
    seek(位置offset),移动指针位置，english占一个字节，中文gbk占2个字节，utf-8占3个字节

路径的相对和绝对
    绝对路径：C:\Users\Administrator\Desktop\test.txt 具体位置的文件
    相对路径：
        test.txt 与当前文件同目录下的文件
        .\test.txt 同上
        ..\file\text 上级文件夹
        \text.txt 根目录下的text.txt，运行环境下也可以有

"""


def write(filePath: str, string: str):
    """写入文件，会覆盖文件原内容"""
    file = open(filePath, 'w', encoding='utf-8')
    file.write(string)  # write写入操作
    file.write('\n')
    file.writelines(list(string))
    file.flush()  # 刷新缓冲区
    file.close()  # 关闭文件对象


def read(filePath: str):
    """读取文件内容"""
    file = open(filePath, 'r', encoding='utf-8')
    print(file.read())
    file.close()


def append(filePath: str, string: str):
    """在文件末尾追加内容"""
    file = open(filePath, 'a', encoding='utf-8')
    file.write(string)
    file.flush()
    file.close()


def insert(filePath: str, string: str):
    """在文件开头覆写内容"""
    file = open(filePath, 'r+', encoding='utf-8')
    file.write(string)
    file.flush()
    file.close()


if __name__ == '__main__':
    f = '../file/a.txt'
    s = 'ssss'
    s2 = 'abcd'
    # write(f, s)
    # read(f)
    # append(f, s)
    # read(f)
    # insert(f, s2)
    # read(f)

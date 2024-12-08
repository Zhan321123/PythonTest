r"""
os.
    getcwd()，获取本模块的绝对路径
    listdir()，获取本模块所在文件夹中的所有文件和文件夹list
    listdir(dir/)，dir下的所有文件名list，不包含目录，"/"可要可不要
    chdir() 改变当前工作目录
    remove(file),删除文件，非文件夹
    os.rename('filePath','newFilePath')，重命名文件
    mkdir(path/),创建文件夹，只能创建单层文件夹,如果存在该文件夹，则会异常
    makedirs(path/)创建文件夹，可以是多层，如果最后一个文件夹存在，则会异常
    rmdir(path/)删除文件夹，不能是文件，且文件夹必须为空
    walk(files:list) = list(dirs, dirList, fileList)
        遍历文件，返回所有(目录，子目录，目录下文件)，会迭代出所有子目录
        for dir, dirList, fileList in walk(os.getcwd()):...
    os.startfile('calc.exe')打开文件
    os.environ['USERPROFILE'], 获取用户个人文件夹,相当于 "C:\Users\[username]"

info = os.stat('file/a.txt')
info.
    st_size,文件大小，单位byte
    st_ctime.文件创建时间
    info.st_mtime,文件最后修改时间
    info.st_atime,文件最后访问时间

os子模块path
os.path.
    abspath(filePath),获取文件绝对路径
    exists(filePath),判断文件或文件夹是否存在
    splitext(filePath) = (dir, suffix),分离文件路径和后缀名
    basename(filePath)->fileName:str,提取文件名
    dirname(filePath)->dirName:str,提取目录名，提取结果不含"\"
    join(dir,file)，拼接dir和file

获取桌面路径字符串: desktopPath = rf"{os.environ['USERPROFILE']}\Desktop"
"""
import os
import time
import os.path as op


def getDirFiles(dirPath: str) -> list:
    """获取文件夹下的所有文件，返回一个list"""
    if not os.path.exists(dirPath):
        print(f'{dirPath}不存在')
        return []
    return os.listdir(dirPath)  # 获取文件夹所有文件和文件夹


def createDir(dirName: str):
    """创建文件夹，如果存在则不创建"""
    if os.path.exists(dirName):
        print(f'{dirName}已存在')
        return
    os.makedirs(dirName)


def walk(files: list):
    """遍历文件，返回所有(目录，子目录，目录下文件)，会迭代出所有子目录"""
    for dirs, dirlist, filelist in os.walk(files):
        print(dirs)
        print(dirlist)
        print(filelist)
        print('-')


def fileAttribute(file: str):
    """获取文件属性"""
    info = os.stat(file)
    print("文件大小：", info.st_size / 1024, 'kB')
    createTime = time.ctime(info.st_ctime)
    print("文件创建时间：", createTime)
    print("文件最后修改时间：", time.ctime(info.st_mtime))
    print("文件最后访问时间：", time.ctime(info.st_atime))


def copyFile(filePath: str, newDirPath: str, newName: str = None):
    """复制文件到新文件夹"""
    if not op.exists(newDirPath):
        print(f'{newDirPath}不存在')
        return
    if newName:
        newFilePath = op.join(newDirPath, newName)
    else:
        newFilePath = op.join(newDirPath, op.basename(filePath))
    if op.exists(newFilePath):
        print(f'{newFilePath}已存在')
        return
    with open(filePath, 'rb') as file:
        with open(newFilePath, 'wb') as nf:
            nf.write(file.read())
    print(f'复制文件{filePath}到{newDirPath}成功')


def readTxtList(filePath: str) -> list:
    """读取txt文件，每行的数据放到list，清除两端空格"""
    if not op.exists(filePath):
        print(f'{filePath}不存在')
        return []
    # 既然作为字符对象，那就应该是utf-8编码，不是就去掉
    with open(filePath, 'r', encoding='utf-8') as file:
        result = file.readlines()
        result = [i.strip() for i in result]
        return result

def writeTxtList(filePath: str, data: list):
    """将list写入txt文件，一行写一个元素，最后不要换行"""
    if op.exists(filePath):
        print(f'{filePath}已存在')
        return
    with open(filePath, 'w', encoding='utf-8') as file:
        for i in data[:-1]:
            file.write(i + '\n')
        file.write(data[-1])
    print(f'list写入文件{filePath}成功')

def renameFile(oldFilePath: str, newFileName: str):
    """重命名文件"""
    if not op.exists(oldFilePath):
        print(f'{oldFilePath}不存在')
        return
    os.rename(oldFilePath, op.join(op.dirname(oldFilePath), newFileName))


if __name__ == '__main__':
    f = '../file/a.txt'
    d = '../file'
    print(os.getcwd())  # 获取本模块的路径
    print(os.listdir())
    dirs, file = op.split(f)  # 将f的目录和文件名分开
    print(dirs,file)
    print(op.dirname(f))
    print(op.basename(f))

    # getDirFiles(d)
    # walk(os.getcwd())
    # fileAttribute(f)
    # print(op.abspath(f))
    # print(op.exists(f))
    print(op.exists(r"C:\Users\Administrator"))  # False
    # dirs, suffix = op.splitext(f)
    # print(dirs, suffix)
    # print(op.basename(f))
    # print(op.dirname(f))
    # print(op.join('file','a.txt'))
    # print(rf"{os.environ['USERPROFILE']}\Desktop")
    # copyFile(f, d, 'newFile.txt')
    # print(readTxtList(f))
    # writeTxtList('../file/newFile.txt', ['a', 'b', 'c'])
    # renameFile('../file/newFile.txt', 'new.txt')
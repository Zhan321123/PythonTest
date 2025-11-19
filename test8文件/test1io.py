r"""

__file__ 当前文件路径
pathlib.Path(__file__).resolve().parent 获取当前文件夹绝对路径

os.
    getcwd()，获取模块(运行时)的绝对路径
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

"""
import os
import pathlib
import re
import shutil
import time
import os.path


def getDesktopDir():
  """获取本机桌面路径"""
  return rf"{os.environ['USERPROFILE']}\Desktop"


def getDirsNameInDir(dirPath: str) -> list:
  """获取文件夹下的所有文件和文件夹名称，返回一个list"""
  if not os.path.exists(dirPath):
    print(f'{dirPath}不存在')
    return []
  return os.listdir(dirPath)  # 获取文件夹所有文件和文件夹


def getDirPathsInDir(dirPath: str) -> list:
  """获取文件夹下的所有文件和文件夹路径，返回一个list"""
  if not os.path.exists(dirPath):
    print(f'{dirPath}不存在')
    return []
  return [os.path.join(dirPath, i) for i in os.listdir(dirPath)]


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


def getAllFiles(dirPath: str) -> [str]:
  """
  获取文件夹中下及其子孙文件夹下的所有文件路径
  不包含文件夹
  """
  result = []
  for dirs, dirlist, filelist in os.walk(dirPath):
    result.extend([os.path.join(dirs, i) for i in filelist])
  return result


def fileAttribute(file: str):
  """获取文件属性"""
  info = os.stat(file)
  print("文件大小：", info.st_size / 1024, 'kB')
  createTime = time.ctime(info.st_ctime)
  print("文件创建时间：", createTime)
  print("文件最后修改时间：", time.ctime(info.st_mtime))
  print("文件最后访问时间：", time.ctime(info.st_atime))


def copyFile(filePath: str, newDirPath: str, newName: str = None) -> bool:
  """
  复制文件到新文件夹

  :param filePath: 需要复制的文件路径
  :param newDirPath: 目标文件夹
  :param newName: 目标文件名，None就是原名
  """
  if not os.path.exists(filePath):
    raise Exception(f'源文件{filePath}不存在')
  if not os.path.exists(newDirPath):
    os.makedirs(newDirPath)
    print(f'目标目录{newDirPath}不存在，创建目录')
  if newName:
    newFilePath = os.path.join(newDirPath, newName)
  else:
    newFilePath = os.path.join(newDirPath, os.path.basename(filePath))
  if os.path.exists(newFilePath):
    print(f'{newFilePath}已存在，跳过该文件')
    return False
  else:
    with open(filePath, 'rb') as file:
      with open(newFilePath, 'wb') as nf:
        nf.write(file.read())
    print(f'复制文件{filePath}到{newDirPath}成功')
    return True


def renameFile(oldFilePath: str, newFileName: str) -> bool:
  """重命名文件"""
  if not os.path.exists(oldFilePath):
    print(f'{oldFilePath}不存在')
    return False
  os.rename(oldFilePath, os.path.join(os.path.dirname(oldFilePath), newFileName))
  print(f'重命名文件{oldFilePath}为{newFileName}成功')
  return True


def copyDir(oldDirPath: str, newDirPath: str) -> bool:
  """
  复制文件夹到新目录

  :param oldDirPath: 需要复制的目录
  :param newDirPath: 目标目录
  :return: 复制文件夹是否成功
  """
  if not os.path.exists(oldDirPath):
    print(f'源目录{oldDirPath}不存在')
    return False
  if not os.path.exists(newDirPath):
    print(f'{newDirPath}不存在，将会创建目录')
  try:
    shutil.copytree(oldDirPath, newDirPath)
    print(f"成功将 {oldDirPath} 复制到 {newDirPath}")
    return True
  except PermissionError:
    print("没有足够的权限进行复制操作，请检查文件和目录权限。")
  except Exception as e:
    print(f"发生了其他错误: {e}")


def increasePath(filePath: pathlib.Path) -> pathlib.Path:
  """
  路径名递增（确保返回的路径不存在）
  :param filePath: 原始路径
  :return: 递增后的新路径（不存在）
  """
  if not filePath.parent.exists():
    raise Exception(f"父级目录 {filePath.parent} 不存在")
  if not filePath.exists():
    return filePath

  name, ext = os.path.splitext(filePath.name)
  pattern = r'^(.*?)\((\d+)\)$'
  match = re.match(pattern, name)

  # 确定基础前缀和起始数字
  if match:
    # 已有数字后缀，从下一个数字开始
    prefix = match.group(1)
    current_number = int(match.group(2)) + 1
  else:
    # 无数字后缀，从 1 开始
    prefix = name
    current_number = 1

  # 循环查找不存在的路径
  while True:
    new_name = f"{prefix}({current_number}){ext}"
    new_path = filePath.parent / new_name
    if not new_path.exists():
      return new_path
    current_number += 1

if __name__ == '__main__':
  print(__file__)
  f = '../file/a.txt'
  # d = '../file'
  # print(os.getcwd())  # 获取本模块运行时的路径
  # print(pathlib.Path(__file__).resolve().parent)  # 获取本py文件的路径
  print(increasePath(pathlib.Path(__file__).parent))
  # print(os.listdir())
  # dirs, file = op.split(f)  # 将f的目录和文件名分开
  # print(dirs, file)
  # print(op.dirname(f))
  # print(op.basename(f))
  # getDirFiles(d)
  # walk(os.getcwd())
  # fileAttribute(f)
  # print(op.abspath(f))
  # print(op.exists(f))
  # print(op.exists(r"C:\Users\Administrator"))  # False
  # dirs, suffix = op.splitext(f)
  # print(dirs, suffix)
  # print(op.basename(f))
  # print(op.dirname(f))
  # print(op.join('file','a.txt'))
  # print(getHomeDir())
  # copyFile(f, d, 'newFile.txt')
  # print(readTxtList(f))
  # writeTxtList('../file/newFile.txt', ['a', 'b', 'c'])
  # renameFile('../file/newFile.txt', 'new.txt')
  # copyDir('file/META-INF', 'file/dir1')
  # print(getDirPathsInDir('file/META-INF'))
  # l = getAllFiles('file')
  # print(l)

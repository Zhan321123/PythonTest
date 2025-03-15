import os


def numberOfFile(filePath: str) -> int:
    """
    统计文件中的词数
    :param filePath: 文件路径
    :return: 词数
    """
    if not os.path.exists(filePath):
        raise Exception(f'{filePath}不存在')
    with open(filePath, 'r', encoding='utf-8') as file:
        result = file.read()
        result = result.replace('\n', '').replace(' ', '')
        return len(result)


def getAllFiles(dirPath: str) -> [str]:
    result = []
    for dirs, dirlist, filelist in os.walk(dirPath):
        result.extend([os.path.join(dirs, i) for i in filelist])
    return result


fileTypes = ['.py', '.md', '.java', '.html']


def allNumberOfDir(dirPath: str) -> int:
    """
    统计一个文件夹中所有文本的字数之和
    :param dirPath:
    :return:
    """
    if not os.path.exists(dirPath):
        raise Exception(f'{dirPath}不存在')
    files = getAllFiles(dirPath)
    result = 0
    for file in files:
        if os.path.splitext(file)[1] in fileTypes:
            result += numberOfFile(file)
    print(f'统计[{dirPath}]成功')
    print(f'{dirPath}中{fileTypes}文件的字数之和是{result}')
    return result


if __name__ == '__main__':
    filePaths = [r"D:\code\pythonProject\PythonTest\introduction",
                 r"D:\code\pythonProject\PythonTest\lib",
                 r"D:\code\pythonProject\PythonTest\other",
                 r"D:\code\pythonProject\PythonTest\test1python基础",
                 r"D:\code\pythonProject\PythonTest\test2科学绘图",
                 r"D:\code\pythonProject\PythonTest\test4pyqt5",
                 r"D:\code\pythonProject\PythonTest\test5系统",
                 r"D:\code\pythonProject\PythonTest\test6媒体",
                 r"D:\code\pythonProject\PythonTest\test7翻译",
                 r"D:\code\pythonProject\PythonTest\test8文件",
                 r"D:\code\pythonProject\PythonTest\test9服务",
                 r"D:\code\pythonProject\PythonTest\test10数据分析",
                 ]
    n = 0
    for filePath in filePaths:
        n += allNumberOfDir(filePath)
    print(n)

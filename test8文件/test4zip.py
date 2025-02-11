"""
zip文件解析
"""
import os
import zipfile


def checkZip(zipFile: str) -> bool:
    """检查文件是否为有效的ZIP文件"""
    if not os.path.exists(zipFile):
        print(f'{zipFile}不存在')
        return False
    if zipfile.is_zipfile(zipFile):
        return True
    else:
        return False


def getZipInfo(zipFile: str):
    """获取zip文件信息"""
    with zipfile.ZipFile(zipFile, 'r') as ref:
        infos = ref.infolist()
        for info in infos:
            print(info.filename)
            print(info.file_size)
            print(info.date_time)
            print(info.comment)


def readZip(zipFile: str):
    """获取zip内部文件路径"""
    with zipfile.ZipFile(zipFile, 'r') as ref:
        names = ref.namelist()
        for name in names:
            n = name.encode('cp437').decode('gbk')
            print(n)


def extractZipAll(zipFile: str, path: str) -> bool:
    """
    解压zip文件，相当于解压到该path文件夹，会自动path创建文件夹

    TODO 中文编码问题
    """
    try:
        with zipfile.ZipFile(zipFile, 'r') as ref:
            ref.extractall(path)
        print(f'已经将{zipFile}解压到{path}')
        return True
    except Exception as e:
        print(f'解压失败：{e}')
        return False


def extractZip(zipFile: str, file: str, path: str) -> bool:
    """
    提取zip文件其中一个文件

    注意点：最终的path=path+/+file，意味着file包含目录时，path也嵌套目录
    TODO 中文编码问题
    """
    try:
        with zipfile.ZipFile(zipFile, 'r') as ref:
            ref.extract(file, path)
        print(f'已经将{zipFile}的{file}解压到{path}')
        return True
    except Exception as e:
        print(f'解压失败：{e}')
        return False


def zip_directory(fileAndDirs: list, zip_path: str) -> bool:
    """
    压缩多个文件

    :param fileAndDirs: 文件夹和文件列表
    :param zip_path: 目标目录
    :return:
    """
    try:
        # 定义要压缩的文件和文件夹路径
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for fileOrDir in fileAndDirs:
                # 压缩单个文件
                if os.path.isfile(fileOrDir):
                    zipf.write(fileOrDir, os.path.basename(fileOrDir))
                # 压缩文件夹
                if os.path.isdir(fileOrDir):
                    for root, dirs, files in os.walk(fileOrDir):
                        for file in files:
                            folder = os.path.join(root, file)
                            arcname = os.path.relpath(folder, os.path.dirname(fileOrDir))
                            zipf.write(folder, arcname)
        print(f'已经将{fileAndDirs}压缩到{zip_path}')
        return True
    except Exception as e:
        print(f'压缩失败：{e}')
        return False


if __name__ == '__main__':
    zip1 = 'file/jar文件.jar'
    zip2 = 'file/zip文件.zip'
    zip3 = 'file/files zip.zip'
    # print(checkZip(zip3))
    # readZip(zip2)
    # getZipInfo(zip2)
    # extractZipAll(zip2,'file')
    # extractZip(zip1,'META-INF/mods.toml','file')
    # zip_directory(['file/META-INF', 'file/t.txt','file/中文.txt'],'file/t.zip')

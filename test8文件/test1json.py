"""
用json模块读取和写入高维数组
"""
import json


def writeJson(filePath: str, data: list,indent: int = 2) -> bool:
    """
    写入json文件

    :param filePath: 文件路径
    :param data: 多维数据
    :param indent: 缩进空格数，填0也会换行，填None则为最min
    :return: bool
    """
    try:
        with open(filePath, 'w') as file:
            # ensure_ascii=False不包含中文，不填False会乱码
            # indent换行时缩进空格数
            json.dump(data, file, ensure_ascii=False, indent=indent)
        print(f"写入文件{filePath}成功")
        return True
    except Exception as e:
        raise Exception(f"写入时发生错误：{e}")

def readJson(filePath: str) -> list:
    """
    读取json文件
    """
    try:
        with open(filePath, 'r') as file:
            data = json.load(file)
        print(f"读取文件{filePath}成功")
        return data
    except Exception as e:
        raise Exception(f"读取时发生错误：{e}")

if __name__ == '__main__':
    l = [
        {'name': 'zhan', 'age': 18, 'id': 2022, 'hobby': ('minecraft', 'study')},
        {'name': 'xiao', 'age': 17, 'habit': 'f', 'marry': False},
        {'name': 'duo', 'id': 2025, 'marry': True}
    ]
    writeJson('file/test.json', l)

    l2 = readJson('file/test.json')
    print(l2)
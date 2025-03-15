import os


def readTxtList(filePath: str) -> list[str]:
    """
    读取txt文件，每行的数据放到list，清除两端空格
    """
    if not os.path.exists(filePath):
        print(f'{filePath}不存在')
        return []
    # 既然作为字符对象，那就应该是utf-8编码，不是就去掉
    with open(filePath, 'r', encoding='utf-8') as file:
        result = file.readlines()
        result = [i.strip() for i in result]
        print(f'{filePath}读取成功')
        return result


def writeTxtList(filePath: str, data: list) -> bool:
    """
    将list写入txt文件，一行写一个元素，最后不要换行

    :param filePath: 写入文件路径
    :param data: 写入列表
    :return 写入是否成功
    """
    if os.path.exists(filePath):
        print(f'{filePath}已存在，不覆写')
        return False
    try:
        with open(filePath, 'w', encoding='utf-8') as file:
            for i in data[:-1]:
                file.write(i + '\n')
            file.write(data[-1])
        print(f'list写入文件{filePath}成功')
        return True
    except Exception as e:
        raise Exception(f'data写入文件{filePath}失败: {e}')


def clearTxt(filePath: str, newFilePath: str = None) -> bool:
    """
    将一个txt文件的空格和换行清除，保存到另一个文件
    :param filePath: txt文件路径
    :param newFilePath: 新文件路径，为None时覆盖原文件
    :return: 是否成功
    """
    if not os.path.exists(filePath):
        raise Exception(f'{filePath}不存在')
    if newFilePath is None:
        newFilePath = filePath
    elif os.path.exists(newFilePath):
        raise Exception(f'{newFilePath}已存在，不覆写')
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            result = file.read()
            result = result.replace('\n', '').replace(' ', '')
        with open(newFilePath, 'w', encoding='utf-8') as file:
            file.write(result)
        print(f'{filePath}清除空格和换行成功')
        return True
    except Exception as e:
        raise Exception(f'{filePath}清除空格和换行文件执行失败: {e}')


if __name__ == '__main__':
    tf = r"C:\Users\刘高瞻\Desktop\新建 文本文档.txt"
    clearTxt(tf)

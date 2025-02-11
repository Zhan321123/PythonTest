import os.path

import pandas


def writeCsv(file: str, dss: list[list]) -> bool:
    """
    将二维数据dss写入file.csv

    :param file: 文件路径
    :param dss: 二维数据
    :return: 是否成功
    """
    if os.path.exists(os.path.dirname(file)):
        raise Exception(f"文件目录{os.path.dirname(file)}不存在")
    if os.path.exists(file):
        raise Exception(f"文件{file}已存在，不替换")
    try:
        pandas.DataFrame(dss).to_csv(file, header=False, index=False)
    except Exception as e:
        raise Exception(e)

def readCsv(file: str) -> list[list]:
    """
    读取file.csv文件，返回二维数据

    :param file: 文件路径
    :return: 二维数据
    """
    if not os.path.exists(file):
        raise Exception(f"文件{file}不存在")
    try:
        dss = pandas.read_csv(file, header=None, encoding='gbk', low_memory=False).to_numpy().tolist()
        print(f"读取文件{file}成功")
        return dss
    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    d = [[1, 2, 3], [4, 5, 6]]
    # writeCsv('../file/csv1.csv', d)
    print(readCsv('../file/csv1.csv'))

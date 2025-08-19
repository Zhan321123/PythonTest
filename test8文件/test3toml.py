"""
toml文件解析

第三方库toml
"""
import toml

def readToml(filePath: str) -> dict:
    """
    读取toml文件
    """
    with open(filePath, 'r', encoding='utf-8') as f:
        return toml.load(f)

if __name__ == '__main__':
    path = 'file/mods.toml'
    data = readToml(path)
    for i in data.keys():
        print(i, data[i])
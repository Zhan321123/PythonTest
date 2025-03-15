"""
markdown处理

表格
"""
import pyperclip


def mdTableToList(mdTable):
    lines = mdTable.strip().split('\n')  # 按行分割表格
    del lines[1]  # 去除分隔行（第二行）
    table = []
    for line in lines:
        line = line.strip(' ')
        line = line.strip('|')  # 去除每行的首尾竖线
        cells = [cell.strip() for cell in line.split('|')]  # 按竖线分割单元格
        table.append(cells)
    return table

def writeClip(content: str) -> bool:
    """将字符串写入剪贴板"""
    try:
        pyperclip.copy(content)
        print("字符串写入剪贴板成功")
        return True
    except Exception as e:
        print(f"字符串写入剪贴板失败：{e}")

if __name__ == '__main__':
    t = pyperclip.paste()


    # 转换为二维列表
    result = mdTableToList(t)
    result = [[j.strip('*').strip('`') for j in i] for i in result]

    s = ''
    for i in result:
        for index, j in enumerate(i):
            if index == len(i)-1:
                s += j
            else:
                s += j + '\t'
        s+='\n'
    # print(s)
    writeClip(s)

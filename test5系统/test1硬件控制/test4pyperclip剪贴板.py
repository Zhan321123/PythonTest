"""
剪贴板控制模块
pyperclip

"""
import pyperclip


def readClip() -> str:
    """读取剪贴板"""
    content = pyperclip.paste()
    return content


def writeClip(content: str) -> bool:
    """将字符串写入剪贴板"""
    try:
        pyperclip.copy(content)
        print("字符串写入剪贴板成功")
        return True
    except Exception as e:
        print(f"字符串写入剪贴板失败：{e}")


if __name__ == '__main__':
    # s = 'hello'

    # writeClip(s)

    r = readClip()
    print(r)

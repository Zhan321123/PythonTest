"""
剪贴板控制模块
pyperclip

"""
import pyperclip

# 读取剪贴板
content = pyperclip.paste()

print(content)

s = "fuck you"
# 写入剪贴板
pyperclip.copy(s)

print(pyperclip.paste())
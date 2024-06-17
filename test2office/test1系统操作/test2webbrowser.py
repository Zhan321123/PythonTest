"""
webbrowser模块
用你浏览器打开html和pdf等文件
注意：
只能用同级目录或者绝对路径
相对不同级路径先用os.path获取绝对路径
"""
import webbrowser
import os.path as op


path = op.abspath("file/bar3d_punch_card.html")
print(path)
webbrowser.open_new(path)

# 无法用这样的相对路径打开
# 打开为空
# webbrowser.open('file/p.pdf')
# 打开为搜索
# webbrowser.open('./file/p.pdf')
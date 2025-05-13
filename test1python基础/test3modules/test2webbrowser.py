"""
webbrowser模块
用你浏览器打开html和pdf等文件
注意：
只能用同级目录或者绝对路径
相对不同级路径先用os.path获取绝对路径
"""
import webbrowser

webbrowser.open('127.0.0.1:5000')
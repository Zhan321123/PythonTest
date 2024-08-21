chcp 65001
:: chcp 65001 让编码为utf-8

:: 教程地址
:: https://blog.csdn.net/qq_46092061/article/details/119983907

:: 双冒号注释

:: 默认应用打开文件
:: start 程序 文件
start "" "file\path"
start "file path"

:: 打开文件夹
start "" "folder\path\"

:: 打开网页
start 360chrome.exe "http://www.baidu.com"

:: 进入路径
cd /d "C:\Users\Administrator\Desktop\test"

:: 定时关机
shutdown -s -t 600
:: 取消定时关机
shutdown -a
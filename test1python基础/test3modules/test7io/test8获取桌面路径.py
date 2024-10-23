"""
os模块在不知道用户名的情况下获取桌面路径

os.environ['USERPROFILE'] 获取用户个人文件夹
相当于 "C:\user\Administrator"
相当于 "C:\user\username"

os.path.join(dir:str, file or dir)
桌面路径 "Desktop"

获取桌面路径字符串:
    path = rf"{os.environ['USERPROFILE']}\Desktop"

"""
import os

# 使用环境变量获取用户个人文件夹
user = os.environ['USERPROFILE']
path = rf"{os.environ['USERPROFILE']}\Desktop"
# 拼接桌面路径
desktop = os.path.join(user, 'Desktop')

# 如果你想创建一个文件或目录
fileName = 'example.txt'
full = os.path.join(desktop, fileName)

with open(full, 'w') as f:
    f.write('Hello World!')
    f.close()

# 创建文件或目录
# os.makedirs(full_file_path, exist_ok=True)  # 如果是目录
# 或者
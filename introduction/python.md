<h1 style="text-align:center">Python</h1>

---

![python](https://img.shields.io/badge/python-3.9-blue)

### python国内库源

#### 库源

- 第三方库清华源 https://pypi.tuna.tsinghua.edu.cn/simple
- 官方库阿里云源 https://mirrors.aliyun.com/pypi/simple
- 官方库豆瓣源 https://pypi.douban.com/simple
- 官方库腾讯云源 https://mirrors.cloud.tencent.com/pypi/simple

#### 使用方法（拿清华源举例）

- 安装单个第三方库
  pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
- 配置全局第三方库
  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

### 配置python库的环境

#### venv环境

1. 创建虚拟环境
   在项目根目录下创建一个新的虚拟环境（venv）。这里以Python 3为例：
   ```shell```{
    - 在项目根目录下创建虚拟环境:
      ```python3 -m venv venv```
    - 激活虚拟环境：
      ```.\venv\Scripts\activate```
      }
2. 在虚拟环境中安装第三方库
   在激活虚拟环境后，使用pip安装你需要的第三方库，
   只会安装在当前虚拟环境中，而不会影响到全局Python环境
   ```shell```{
   ```pip install [库名]```
   }
3. 退出虚拟环境：
   当完成项目开发并希望回到全局Python环境时，可以执行如下命令退出虚拟环境：
   ```shell```{
   ```deactivate```
   }
4. 直接在特定venv目录安装库，以该项目所在venv环境为例
   ```shell```{
   ```pip install --target=D:\code\pythonProject\PythonTest\venv\Lib\site-packages [库名]```
   }
5. 显示安装的所有库
    ```pip list```

#### conda环境

- 默认环境目录
  C:\Users\[username]\Anaconda3\envs
- 默认在默认目录下新建环境
  ```conda create -n [环境名称] (python=[版本])```
- 在其他地方新建环境
  ```conda create -p [绝对目录+环境名称] (python=[版本])```
- 激活默认目录的环境
  ```conda activate [环境名称]```
- 激活其他目录的环境
  ```conda activate [目录+环境名称]```
- 查看所有环境
  ```conda en[test3modules](test1python%E5%9F%BA%E7%A1%80%2Ftest3modules)v list```
- 安装第三方库
  ```conda install [库名]```

### pyinstaller将项目打包为exe文件

#### 安装pyinstaller库

```pip install pyinstaller```

#### 使用方法

- 打包为单个大文件
  pyinstaller -F [py] (-i [图标])
- 打包为文件夹
  pyinstaller -d [py] (-i [图标])

### 卸载python系统环境变量的所有第三方库
```batch
@echo off
   setlocal enabledelayedexpansion

   for /f "tokens=1* delims==" %%a in ('pip freeze') do (
     set pkg_name=%%a
     if "!pkg_name!" neq "-e" (
       pip uninstall -y "!pkg_name!"
     )
   )
```
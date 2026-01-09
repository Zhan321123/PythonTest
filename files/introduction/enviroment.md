<h1 style="text-align:center">Enviroment</h1>

<div style="text-align:center">
  <img src="https://img.shields.io/badge/python-3.9-blue">
  <img src="https://img.shields.io/badge/python-3.10-yellow">
  <img src="https://img.shields.io/badge/python-3.11-green">
  <img src="https://img.shields.io/badge/python-3.12-red">
</div>

### python国内库源

#### 库源

**镜像库可能不完全**

- 第三方库清华源 `https://pypi.tuna.tsinghua.edu.cn/simple`
- 官方库阿里云源 `https://mirrors.aliyun.com/pypi/simple`
- 官方库豆瓣源 `https://pypi.douban.com/simple`
- 官方库腾讯云源 `https://mirrors.cloud.tencent.com/pypi/simple`

#### 使用方法

- 安装单个第三方库
  ```pip install [libname]```
  ```pip install [libname] -i [库源]```
- 配置全局第三方库
  ```pip config set global.index-url [库源]```

### 配置python库的环境

#### venv环境

1. 创建虚拟环境，在**项目根目录**打开cmd下创建一个新的虚拟环境venv
   ```python3 -m venv venv```
2. 激活虚拟环境再使用pip安装，否则安装到了系统环境中
   ```.\venv\Scripts\activate```
3. 在虚拟环境中安装第三方库
   在激活虚拟环境后，使用pip安装第三方库，
   只会安装在当前虚拟环境中，而不会影响到全局Python环境
   ```pip install [libname]```
4. 退出虚拟环境，回到全局Python环境时：
   ```deactivate```

注意事项

- venv环境一旦位置确定好，就不能更改目录，否则无法激活环境，就不能使用`pip install [libname]`，就只能使用`--target=[rootDir/venv/Lib/site-packages/]`
- 直接在特定venv目录安装库，以该项目所在venv环境为例
  ```pip install --target=D:\code\pythonProject\PythonTest\venv\Lib\site-packages [libname]```
- 显示安装的所有库
  ```pip list```
- 直接安装whl环境文件，pypi库文件通常为`[libname]-[libversion]-[os]-[32/64].whl`
  ```pip install [filename]```

#### conda环境

conda优点在于把环境单独拎出来放到一个地方统一管理，也预备了许多常用库，缺点就是占用外存有点大，显得臃肿

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
- 安装第三方库
  ```conda install [库名]```

### 卸载python环境里所有第三方库

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

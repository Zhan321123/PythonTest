<h1  style="text-align: center;">Pyinstaller</h1>

<hr>

### 链接

[pyinstaller官方文档](https://pyinstaller.org/en/stable/)

### 使用方法

1. `(venv) PS ...> pip install -U pyinstaller`
2. `pyinstaller [file.py]`

### 配置

- `-i [icon.ico]` 配置图标
- `-F` 打包为单个大文件
- `-d` 打包为文件夹
- `--hidden-import [module]` 添加第三方库
- `--onefile` 打包为单个大文件
- `--add-data [file;destination]` 添加文件
- `--name [name]` 配置打包后的文件名

### 可能出现的问题

- pyinstaller 命令未识别
  1. 可将`venv\Scripts`添加到环境变量中
  2. 将pyinstaller改为`.\venv\Scripts\pyinstaller.exe`
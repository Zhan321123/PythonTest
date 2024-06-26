# encoding:utf-8
r"""
一、
    要在项目专属的虚拟环境中安装第三方库，而不将其安装到全局Python环境中，请按照以下步骤操作：

1.创建虚拟环境： 在项目根目录下创建一个新的虚拟环境（venv）。这里以Python 3为例：
shell{
    # 在项目根目录下:
    python3 -m venv venv
    # 激活虚拟环境：
    .\venv\Scripts\activate
}
3.在虚拟环境中安装第三方库： 在激活虚拟环境后，使用pip安装你需要的第三方库，
只会安装在当前虚拟环境中，而不会影响到全局Python环境
shell{
    pip install <library-name>
}
4.在虚拟环境中工作： 在虚拟环境激活的情况下，你可以运行项目代码并使用已安装的第三方库。
5.退出虚拟环境： 当完成项目开发并希望回到全局Python环境时，可以执行如下命令退出虚拟环境：
shell{
    deactivate
}
如此一来，你就可以在项目中拥有一个干净且独立的Python环境，其中仅包含该项目所需的第三方库。
当你需要在另一个项目中使用不同版本的库时，只需为那个项目创建并激活新的虚拟环境，然后在该环境中安装相应的库即可。

二、
    在特定目录安装库
shell{
    pip install --target=D:\code\pythonProject\PythonTest\venv\Lib\site-packages <library-name>
}

"""

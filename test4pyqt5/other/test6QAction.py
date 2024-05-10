"""
QAction()
    .setShortcut('Ctrl+Z')设置快捷键
    .setStatusTip()状态栏提示

QAction(name:string,master,checkable=boolean)
    checkable，设置是否可以选中，当Action再菜单上时有选择状态
    .triggered.connect(method)连接方法

"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建action
        qa = QAction(QIcon('exit.png'), 'Exit', self)
        qa.setShortcut('Ctrl+Q')
        qa.setStatusTip('Exit application')
        qa.triggered.connect(self.close)

        exitAct = QAction(QIcon('../file/image1.png'), 'Exit', self)
        # 设置快捷键
        exitAct.setShortcut('Ctrl+Q')
        # 状态栏提示
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

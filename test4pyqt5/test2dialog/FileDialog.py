"""
QFileDialog
    .getOpenFileName(master, title:string, dir)打开一个文件选择框，返回选择的文件列表

"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
        QFileDialog, QApplication, QAction)
from PyQt5.QtGui import QIcon
from pathlib import Path
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 创建一个多行文本编辑器
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):
        # 获取当前用户目录
        home_dir = str(Path.home())
        # QFileDialog.getOpenFileName()返回一个元组，第一个元素是文件名，第二个元素是文件类型
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        if fname[0]:
            print("fileName:", fname[0], "fileType:", fname[1])
            f = open(fname[0], 'r')
            with f:

                data = f.read()
                self.textEdit.setText(data)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

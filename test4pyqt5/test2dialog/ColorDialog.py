"""
QColorDialog
    .QColorDialog.getColor()打开颜色选择对话框，返回一个QColor对象
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
        QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # QColor(red, green, blue, alpha)
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)
        # QFrame 是显示一个矩形框的部件
        self.frm = QFrame(self)
        # setStyleSheet()是设置样式表的方法
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 200, 200)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Color dialog')
        self.show()


    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():

            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

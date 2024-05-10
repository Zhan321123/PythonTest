"""
QApplication(sys.argv)
    sys.exit(qApplication.exec())

QWidget
    .setWindowTitle(string)
    .setWindowIcon(QIcon())设置组件的图标
    .resize(QSize())设置组件的大小
    .setGeometry(int,int,int,int)设置组件的精确几何位置和大小
    .setFixedSize(int,int)设置组件的固定大小
    .setMinimumSize(int,int)
    .setMaximumSize(int,int)设置组件的最大和最小大小
    .move(QPoint())
    .show()

QMainWindow
    .setCentralWidget(qWidget) 设置为主窗口的中央部件
    .statusBar() -> QStatuBar增加左下角信息框

QStatuBar
    .showMessage(string)
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('minecraft 1.99.0')
        self.setWindowIcon(QIcon('../resources/image/pearl.png'))
        self.resize(250, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec())

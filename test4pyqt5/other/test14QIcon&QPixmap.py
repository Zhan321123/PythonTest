"""
QPixmap("file path")

QIcon("file path")

"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QIcon
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        # QPixmap是QT的图像类，可以加载图片，
        # 并将其转换为QPixmap对象
        pixmap = QPixmap('../file/image1.png')
        icon = QIcon('../file/image1.png')
        self.setWindowIcon(icon)

        lbl = QLabel()
        # setPixmap()方法设置QLabel的图像
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Sid')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

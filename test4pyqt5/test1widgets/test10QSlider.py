"""
Slider(方向) 滚动条
    setFocusPolicy(焦点)
    valueChanged[int].connect(method)传入int给method
    setValue(int)

    方向：
Qt.Orientation.Horizontal 表示水平方向，默认
Qt.Orientation.Vertical 表示垂直方向
    焦点：
Qt.FocusPolicy.NoFocus 表示不能获得焦点
Qt.FocusPolicy.ClickFocus 表示点击控件时获得焦点
Qt.FocusPolicy.TabFocus 表示按Tab键可以获得焦点
Qt.FocusPolicy.StrongFocus 表示获得焦点时，鼠标可以移动到控件内


"""

from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QSlider是滑动条，可以设置滑动条的滑动方向，滑动条的滑动范围，滑动条的滑动步长等
        # 默认是水平方向
        # Qt.Orientation.Horizontal表示水平方向
        sld = QSlider(Qt.Orientation.Horizontal, self)
        # setFocusPolicy()设置控件是否可以获得焦点
        # 默认是Qt.FocusPolicy.TabFocus，即按Tab键可以获得焦点
        # Qt.FocusPolicy.NoFocus表示不能获得焦点
        sld.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        sld.setGeometry(30, 40, 200, 30)
        # valueChanged[int]表示当滑动条的值改变时，会发送一个int类型的信号
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../file/image1.png'))
        self.label.setGeometry(250, 40, 80, 30)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('../file/i1.png'))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('../file/i2.png'))
        elif 30 < value < 80:
            self.label.setPixmap(QPixmap('../file/i3.png'))
        else:
            self.label.setPixmap(QPixmap('../file/i4.png'))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

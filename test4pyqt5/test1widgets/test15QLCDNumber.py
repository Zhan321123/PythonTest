"""
QLCDNumber() 时钟数字显示器
    .display(int)设置值

"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QLCDNumber 是一个显示数字的部件，可以显示 0 到 99 之间的数字。
        self.lcd = QLCDNumber(self)
        # QSlider 是一个滑块，可以拖动。
        # Qt.Orientation.Horizontal 表示水平方向
        self.sld = QSlider(Qt.Orientation.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.sld)

        self.setLayout(vbox)
        # 绑定 QSlider 的 valueChanged 信号和 QLCDNumber 的 display 槽
        self.sld.valueChanged.connect(self.lcd.display)

        b = QPushButton(self)
        b.setText("test")
        b.move(30,50)
        b.clicked.connect(self.bu)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Signal and slot')
        self.show()
    def bu(self):
        self.lcd.display(10)
        self.sld.setValue(10)
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

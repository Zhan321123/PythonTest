"""
QPushButton()点击按钮

method
    setIcon(QIcon())
    setText(string)
    clicked.connect(method) 点击执行方法
    setCheckable(boolean) 设置为选中模式


"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(300, 200, 800, 700, )
        self.c2 = C2(self)
        self.c2.move(300, 300)

    def initUI(self):
        # 创建pushButton按钮
        btn = QPushButton('Button', self)
        # 设置按钮位置
        btn.move(20, 20)
        btn.clicked.connect(self.onClicked)

        b2 = QPushButton('B2', self)
        b2.setIcon(QIcon('../file/image1.png'))
        b2.setText("")

    def onClicked(self):
        print('button clicked')


class C2(QWidget):

    def __init__(self, master):
        super().__init__(master)

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        # 将按钮设置为可切换
        redb.setCheckable(True)
        redb.move(10, 10)
        # 绑定信号槽
        # clicked[bool]信号
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        # setStyleSheet() 设置样式
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        # sender() 返回发送信号的对象
        source = self.sender()
        # pressed 为True时，按钮被按下
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == "Red":
            # setRed() 设置红色的值
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

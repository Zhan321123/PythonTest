"""
QProgressBar(master)进度条
    .setValue(int)设置进度

QBasicTimer()
    .isActive() 是一个定时器是否激活的方法
    .stop()计时器暂停
    .start(int, master)，int 是定时器时间，单位是毫秒, QObject 是一个定时器所属的对象

"""

from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QProgressBar 是 一个显示进度条的控件
        # 默认情况下，进度条的初始值为0，最大值为100
        # 进度条的当前值可以通过调用setValue()方法来设置
        # 进度条的进度条颜色可以通过调用setStyleSheet()方法来设置
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        # QBasicTimer 是一个定时器，可以设置定时器时间
        # QBasicTimer 的构造函数需要一个参数，该参数是定时器时间，单位是毫秒
        # 当定时器启动后，定时器会自动调用timerEvent()事件
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    # timerEvent() 是一个定时器事件，当定时器启动时，定时器会自动调用该事件
    def timerEvent(self, e):

        if self.step >= 100:
            # stop() 是一个定时器停止的方法
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        # isActive() 是一个定时器是否激活的方法
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # start(int, QObject) 是一个定时器启动的方法
            # int 是定时器时间，单位是毫秒, QObject 是一个定时器所属的对象
            self.timer.start(100, self)
            self.btn.setText('Stop')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

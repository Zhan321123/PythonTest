"""
QLabel

method
    setPixmap(QPixmap("file path"))
    text()
    move(QPoint())
    toolTip()
    setFrameShape(QFrame.Shape.外框)


外框:
    Panel：面板，用于显示面板的边框。
    PanelBevel：面板，用于显示面板的凹陷。
    HLine：水平线。
    VLine：垂直线。
    Box：矩形框。
    StyledPanel：面板，用于显示面板的边框。
    NoFrame：无边框。
    WinPanel：面板，用于显示面板的边框。
"""

import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建QLabel文本
        lbl1 = QLabel('ZetCode', self)
        lbl1.move(150, 100)
        lbl1.setToolTip("<img src='../file/bigImage1.png'>")

        lb2 = QLabel('tutorial', self)
        lb2.move(0, 0)
        lb2.setPixmap(QPixmap('../file/image1.png'))
        lb2.setToolTip('This is a <u>tool</u> tip')

        lb3 = QLabel('', self)
        lb3.move(30,30)
        lb3.setText('PyQt5 is a \n<b>foolish</b> software! ')
        lb3.setToolTip('This is a <font color="red">red<font color> tool tip')
        print(lb3.text())
        print(lb3.toolTip())
        lb3.setFrameShape(1)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Absolute')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

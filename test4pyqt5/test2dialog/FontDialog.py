"""
QFontDialog
    .QFontDialog.getFont()打开字体对话框，返回QFont对象
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        # setSizePolicy()设置按钮的尺寸策略
        # QSizePolicy.Policy.Fixed表示按钮的尺寸是固定的
        btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        # 显示字体对话框
        # QFontDialog.getFont()返回一个元组，第一个元素是字体，第二个元素是一个布尔值，
        # 如果用户点击了确定按钮，则为True，否则为False。
        font, ok = QFontDialog.getFont()

        if ok:
            # setFont()设置标签的字体
            self.lbl.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

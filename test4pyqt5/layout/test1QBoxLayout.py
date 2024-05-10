"""
布局器
QHBoxLayout() 水平布局
QVBoxLayout() 垂直布局
    .setSpacing(int)设置间距
    .setAlignment(Qt.Alignment)设置对齐方式
    .addStretch(int)添加一个拉伸因子，相当于此时增加一个空白组件
    .addWidget(QWidget,stretch:int,alignment:int)添加组件
    .addLayout(QBoxLayout,stretch:int)添加布局

QWidget
    .setLayout(QBoxLayout)设置布局给组件
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # 创建水平布局
        hbox = QHBoxLayout()
        # 添加一个拉伸因子
        hbox.addStretch(1)
        # 添加按钮
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 创建垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        # 添加水平布局对象
        vbox.addLayout(hbox)

        # 设置窗口布局
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Buttons')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

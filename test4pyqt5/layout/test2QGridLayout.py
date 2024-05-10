"""
网格布局器
QGridLayout().
    setSpacing(int)设置网格间距
    addWidget(widget, row, column, rowSpan, columnSpan)

Widget.
    setLayout(QGridLayout)

"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建网格布局器
        grid = QGridLayout()
        # 设置网格间距
        grid.setSpacing(30)
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QPushButton(name)
            # grid.addWidget(button, position[0], position[1])

            # addWidget(widget, row, column, rowspan, colspan)
            # row 和 column 分别代表行和列，从0开始
            # rowspan 和 colspan 分别代表行数和列数
            grid.addWidget(button, *position, 1, 1)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

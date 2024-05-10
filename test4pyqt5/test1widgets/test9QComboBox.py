"""
ComboBox() 下拉菜单
    addItem(string)
    textActivated[str].connect(method)连接函数，传入选中的str

"""

import sys

from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Ubuntu', self)
        # QComboBox是一种下拉菜单，可以显示一个列表，用户可以点击列表中的项目，也可以使用键盘上下键选择项目。
        combo = QComboBox(self)

        # QComboBox的addItem()方法用于添加项目。
        combo.addItem('Ubuntu')
        combo.addItem('Mandriva')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')

        combo.move(50, 50)
        self.lbl.move(50, 150)
        # QComboBox的textActivated()信号返回当前选中的文本。
        combo.textActivated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

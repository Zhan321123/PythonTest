"""
QCheckBox()
    stateChanged[int].connect(method)是否选中的状态连接函数
    toggle()设置选中，创建时未选中

QGroupBox()
    setTitle(string)

"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        group = QGroupBox(self, )
        group.setTitle('GroupBox')
        # QCheckBox 是一个单选按钮，可以选中或取消选中。

        cb1 = QCheckBox('Show title')
        cb1.toggle()
        # 状态改变时，发射一个状态改变信号
        cb1.stateChanged[int].connect(self.change)

        cb2 = QCheckBox('Show date')
        cb3 = QCheckBox('Show time')
        cb2.stateChanged[int].connect(self.change)
        cb3.stateChanged[int].connect(self.change)

        bLayout = QVBoxLayout()
        group.setLayout(bLayout)
        bLayout.addWidget(cb1)
        bLayout.addWidget(cb2)
        bLayout.addWidget(cb3)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QCheckBox')
        self.show()

    def change(self, state):
        # Qt.CheckState.Checked.value是2是选中
        if state == Qt.Checked:
            print('checked', state)
        else:
            print('unchecked', state)
        sender = self.sender()
        print(sender.text())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

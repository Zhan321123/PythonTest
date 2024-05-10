"""
QDoubleSpinBox(master)
QSpinBox(master)
    .setValue(int)设置值
    .setMaximum(int)设置最大值
    .setMinimum(int)设置最小值

    .value()获取值
    .valueChanged[int].connect(method)绑定值改变事件，传入int变量
"""
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QSpinBox, QDoubleSpinBox, QApplication, QMainWindow, \
    QGroupBox, QVBoxLayout, QLabel
import sys


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(533, 435)

        groupBox = QGroupBox("spin", MainWindow)
        groupBox.setGeometry(QRect(50, 40, 191, 141))
        v = QWidget(groupBox)
        v.setGeometry(QRect(10, 20, 171, 111))
        v2 = QVBoxLayout(v)

        doubleSpin = QDoubleSpinBox(v)
        spin = QSpinBox(v)
        self.label = QLabel(v)

        spin.setValue(0)
        spin.setMaximum(3)
        spin.setMinimum(-2)
        doubleSpin.setValue(1.00)
        doubleSpin.setMaximum(10.00)

        v2.addWidget(doubleSpin)
        v2.addWidget(spin)
        v2.addWidget(self.label)

        spin.setToolTip("spin tooltip")
        spin.setStatusTip("spin status tip")

        self.statusbar = MainWindow.statusBar()

        def change(value):
            print(value)
            self.statusbar.showMessage(f'Value:{value}')
            self.label.setText(f'Value:{value}')

        spin.valueChanged[int].connect(change)
        doubleSpin.valueChanged[float].connect(change)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Window().setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

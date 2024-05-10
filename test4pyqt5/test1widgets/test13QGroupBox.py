"""
QGroupBox()文字边框
    .setLayout(QLayout)
    .layout()，返回QLayout对象
    .layout().addWidget(QWidget)添加对象

"""

from PyQt5.QtWidgets import QGroupBox, QWidget, QCheckBox, QRadioButton, QBoxLayout, QApplication
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建QGroupBox
        gb1 = QGroupBox('QGroupBox1')
        gb2 = QGroupBox('QGroupBox2')
        gb3 = QGroupBox('QGroupBox3')

        cb1 = QCheckBox('CheckBox1')
        cb2 = QCheckBox('CheckBox2')
        cb3 = QCheckBox('CheckBox3')

        rb1 = QRadioButton('RadioButton1')
        rb2 = QRadioButton('RadioButton2')
        rb3 = QRadioButton('RadioButton3')

        rb4 = QRadioButton('RadioButton4')
        rb5 = QRadioButton('RadioButton5')
        rb6 = QRadioButton('RadioButton6')

        gb1.setLayout(QBoxLayout(QBoxLayout.Up))
        gb1.layout().addWidget(cb1)
        gb1.layout().addWidget(cb2)
        gb1.layout().addWidget(cb3)

        gb2.setLayout(QBoxLayout(QBoxLayout.Up))
        gb2.layout().addWidget(rb1)
        gb2.layout().addWidget(rb2)
        gb2.layout().addWidget(rb3)

        gb3.setLayout(QBoxLayout(QBoxLayout.Up))
        gb3.layout().addWidget(rb4)
        gb3.layout().addWidget(rb5)
        gb3.layout().addWidget(rb6)

        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight))
        self.layout().addWidget(gb1)
        self.layout().addWidget(gb2)
        self.layout().addWidget(gb3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

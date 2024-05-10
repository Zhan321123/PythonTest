"""
QCalendarWidget(master)
    .selectedDate()返回选中的日期 QDate
    .setGridVisible(boolean)设置是否显示网格
    .clicked[QDate]方法返回一个信号，当用户点击一个日期时，信号会发送一个QDate类型的参数
    .clicked[QDate].connect(method)选择日期的事件绑定

"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)
        # QCalendarWidget是一个日历控件，可以显示一个月的日期
        # 默认情况下，日历控件显示当前月份
        # QCalendarWidget.selectedDate()方法返回当前选中的日期
        cal = QCalendarWidget(self)
        # QCalendarWidget.setGridVisible()方法可以设置是否显示网格
        cal.setGridVisible(True)
        # QCalendarWidget.clicked[QDate]方法返回一个信号，当用户点击一个日期时，
        # 信号会发送一个QDate类型的参数
        # QDate是QtCore中的一个类，用于表示日期
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

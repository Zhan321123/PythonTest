"""
QListView
QTreeView
QAbstractListModel
QStandardItemModel
QStyledItemDelegate
QListViewDelegate
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MyListView(QWidget):
    def __init__(self):
        super(MyListView, self).__init__()
        self.setWindowTitle("QListView")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        list_view = QListView(self)
        list_view.setGeometry(10, 10, 200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyListView()
    main.show()
    sys.exit(app.exec_())

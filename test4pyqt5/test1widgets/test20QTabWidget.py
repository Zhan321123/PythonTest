"""
QTabWidget(master)
    .setCurrentIndex(index:int)显示指定索引的标签页，从0开始
    .addTab(Widget, name:string)添加该widget为标签页
    .currentIndex()当前选中的页面索引
    .isTabEnabled(index)某个标签页是否不可可用
    .setTabEnabled(index, boolean)设置标签页是否可用
    .count()返回标签页的数量
    .removeTab(index)移除指定索引的标签页
    .setTabIcon(index, QIcon)设置标签页图标
    .setTabText(index, string)设置标签页文本
    .setTabPosition(QTabWidget.North/East/South/West)设置标签页位置

"""
import sys
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QTabWidget, QGridLayout, QPushButton, QLabel, QGroupBox, QApplication, QMainWindow


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(530, 433)
        self.centralwidget = QWidget(MainWindow)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(0, 0, 531, 431))
        self.tab = QWidget()
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout = QGridLayout()

        self.pushButton = QPushButton("button", self.tab, )
        self.label = QLabel("l a b e l", self.tab)
        self.pushButton_2 = QPushButton("pushButton", self.tab)
        self.label_2 = QLabel("LL", self.tab)

        def printTab():
            print(self.tabWidget.currentIndex())
            # tabWidget的标签页数量
            self.tabWidget.addTab(QWidget(), "tab" + str(self.tabWidget.count()))

        self.pushButton.clicked.connect(printTab)

        def banTab2():
            self.tabWidget.removeTab(self.tabWidget.count() - 1)
            if self.tabWidget.isTabEnabled(1):
                b = False
            else:
                b = True
            self.tabWidget.setTabEnabled(1, b)

        self.pushButton_2.clicked.connect(banTab2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "tab1")
        self.tab_2 = QWidget()
        self.groupBox = QGroupBox("Group Box Page", self.tab_2)
        self.groupBox.setGeometry(QRect(0, 0, 521, 401))
        self.tabWidget.addTab(self.tab_2, "tab2")

        MainWindow.setCentralWidget(self.centralwidget)  # 设置主窗口
        self.tabWidget.setCurrentIndex(1)  # 设置默认显示的tab
        self.tabWidget.setTabPosition(QTabWidget.West)  # 设置tabWidget显示在西面
        self.tabWidget.setTabIcon(0, QIcon("../file/villager2.png"))  # 修改tab1的图标
        self.tabWidget.setTabText(0, "")  # 设置tab1的标题


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Window().setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

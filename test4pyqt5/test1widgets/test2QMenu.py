"""
QMenu().
    addMenu(QMenu)
    addAction(QAction)

QMenubar.
    addMenu(name:string)，返回一个QMenu

QWidget.
    menuBar()，返回一个菜单栏对象QMenubar

QAction(name:string,master,checkable=boolean).
    checkable，设置是否可以选中

string:
    前加&，可以Alt+首字母，快捷键
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        self.initUI()

    def initUI(self):
        # 创建菜单栏
        menubar = self.menuBar()
        # 创建菜单
        fileMenu = menubar.addMenu('&QMenu1')
        # 创建子菜单
        impMenu = QMenu('QMenu2', self, )
        # 创建子菜单的子菜单
        impAct = QAction('QAction1', self, checkable=True,)
        impAct.setStatusTip('View statusbar')
        # 将子菜单添加到菜单栏
        impMenu.addAction(impAct)
        # 创建一个菜单项
        newAct = QAction('QAction2', self)
        # 将菜单项添加到菜单栏
        fileMenu.addAction(newAct)
        # 将子菜单添加到菜单栏
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Submenu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

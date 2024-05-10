"""
典型登录界面的制作
"""
from login import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 隐藏窗口标题和边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # 设置窗口可拖动
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if (event.button() == QtCore.Qt.LeftButton) and self.isMaximized() == False:
            self.flag = True
            self.position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if QtCore.Qt.LeftButton and self.flag:
            self.move(event.globalPos() - self.position)
            event.accept()
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.flag = False
        self.setCursor(QtCore.Qt.ArrowCursor)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        login = Window()
        login.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)

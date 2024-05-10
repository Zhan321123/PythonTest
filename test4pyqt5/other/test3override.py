"""
Widget() @Override
    dragEnterEvent(self, e)
        e.mimeData()返回一个MimeData对象，该对象包含拖放事件中的数据
        e.mimeData().hasFormat('text/plain')是否包含文本对象，返回boolean
        e.accept()接受拖放事件，鼠标样式变为加号
        e.ignore()忽略拖放事件，鼠标样式变为禁止
    dropEvent(self, e)拖放事件，前提为拖放事件被接受

    paintEvent(self, event)重绘组件窗口事件

    keyPressEvent(self, e: QKeyEvent)键盘点击事件
        e.key()返回键盘对应的int值
        Qt.Key_value直接获取键盘对应的int值，用法：e.key()==Qt.Key_Enter->boolean

    mousePressEvent(self, e: QMouseEvent)鼠标点击事件

    mouseMoveEvent(self, e: QMouseEvent)鼠标移动事件
        e.pos()鼠标位置
        e.x()
        e.y()

Widget
    .setMouseTracking(boolean)设置鼠标移动事件
"""

import sys

from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        # setAcceptDrops()设置窗口是否接受拖放事件
        self.setAcceptDrops(True)


    # 拖动进入事件，默认情况下，该事件被忽略
    # 忽略后改变鼠标样式为禁止
    # 允许后改变鼠标样式为加号
    def dragEnterEvent(self, e):
        # e.mimeData()返回一个MimeData对象，该对象包含拖放事件中的数据
        # hasFormat()返回一个布尔值，指示MimeData对象是否包含指定类型的数据
        # 文本数据用text/plain表示
        # 文件数据用application/x-qabstractitemmodeldatalist表示
        if e.mimeData().hasFormat('text/plain'):
            # 接受拖放事件
            e.accept()
        else:
            # 忽略拖放事件
            e.ignore()

    # 拖动事件
    def dropEvent(self, e):
        # setText()设置按钮的文本
        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()

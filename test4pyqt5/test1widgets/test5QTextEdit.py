"""
QTextEdit
    toPlainText()获取文本
    setText("string")设置文本
    append("string")追加文本
    textCursor().selectedText()获取光标选中的文本
    textCursor().position()获取光标位置
    setFont(QFont())

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QAction, QWidget, QPushButton, QBoxLayout
from PyQt5.QtGui import QIcon, QFont


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        q = QWidget(self)
        layout = QBoxLayout(QBoxLayout.LeftToRight, q)
        q.setLayout(layout)
        # 创建一个文本编辑器
        self.textEdit = QTextEdit(q)
        self.textEdit.setGeometry(0, 0, 300, 200)
        b = QPushButton("fuck",self.textEdit)
        b.move(200,200)
        b.clicked.connect(self.p)

        b2 = QPushButton("fuck2",self.textEdit)
        b2.move(100,200)
        b2.clicked.connect(self.p2)

        # 设置为主窗口的中央部件
        self.setCentralWidget(self.textEdit)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main root')
        self.show()

    def p(self):
        print(self.textEdit.textCursor().selectedText())
        print(self.textEdit.textCursor().position())
        print(self.textEdit.textCursor().selectionStart())
        print(self.textEdit.textCursor().selectionEnd())
        print(self.textEdit.toPlainText())

    def p2(self):
        self.textEdit.append("fuck2")
        self.textEdit.setFont(QFont("Times", 12, QFont.Bold))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

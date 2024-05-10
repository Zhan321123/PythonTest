"""
QLineEdit()
    .textChanged[str].connect(method)内容改变触发事件连接方法
    .setText(string)设置text
    .adjustSize()根据文本自动调节大小
    .text()获取text
    .setDragEnabled(boolean)设置是否可以拖入输入

"""
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QTextEdit, QGridLayout, QPushButton


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        # 输入框
        self.titleEdit = QLineEdit()
        self.authorEdit = QLineEdit()
        self.authorEdit.setText("author")
        print(self.authorEdit.text())
        reviewEdit = QTextEdit()
        self.authorEdit.textChanged[str].connect(self.change)

        grid = QGridLayout()
        # setSpacing 设置控件之间的间距
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(self.authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.b = QPushButton('Submit', self)
        # self.b.clicked.connect(self.sub)
        grid.addWidget(self.b, 9, 0, 1, 2)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def sub(self):
        print("title", self.titleEdit.text())
        self.titleEdit.setText("title")

    def change(self, text):
        print(text)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

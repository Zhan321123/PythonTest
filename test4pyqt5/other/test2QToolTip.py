"""
tooltip

widget类名.set()是整体设置
widget.setToolTip(string)添加单个widget的提示

string可用的标签有：
    <b>text</b> 表示加粗
    <i>text</i> 表示斜体
    <u>text</u> 表示下划线
    <center>text</center> 表示居中
    <font color="red">text</font color> 表示颜色
    <img src="file.png"> 表示图片
    <a href="http://www.baidu.com">baidu</a> 表示超链接
    <pre>text</pre> 表示预格式化文本
    <code>text</code> 表示代码


"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置提示字体
        QToolTip.setFont(QFont('SansSerif', 10))
        # 设置提示
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 设置点击按钮
        btn = QPushButton('Button', self)
        # 设置按钮提示

        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 设置按钮大小
        # sizeHint() 返回按钮建议大小
        btn.resize(btn.sizeHint())
        # 设置按钮位置，移动到(50, 50)
        btn.move(50, 50)

        # 设置窗口大小
        self.setGeometry(300, 300, 300, 200)

        self.setWindowTitle('Tooltips')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

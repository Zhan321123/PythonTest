"""
QPainter()画画对象
    .begin(Widget)在widget上开始绘制
    .end()结束绘制
    .setRenderHint(QPainter.RenderHint.Antialiasing)设置渲染提示，设置抗锯齿
    .setPen(QColor, width, style)设置画笔
    .setBrush(QBrush)设置画刷
    .setFont(QFont)设置字体

    .drawText(event.rect(), Qt.AlignmentFlag.model, text:string)绘制文本
        event.rect()是窗口大小

        Qt.AlignmentFlag.AlignCenter居中
        Qt.AlignmentFlag.AlignLeft左对齐
        Qt.AlignmentFlag.AlignRight右对齐
        Qt.AlignmentFlag.AlignTop上对齐
        Qt.AlignmentFlag.AlignBottom下对齐
        Qt.AlignmentFlag.AlignHCenter水平居中
        Qt.AlignmentFlag.AlignVCenter垂直居中
    .drawPixmap(QPixmap)绘制图片
    .drawImage(QImage)绘制图像
    .drawPoint()绘制点
    .drawLine(QLine)绘制线
    .drawRect()绘制矩形
    .drawPolygon()绘制多边形
    .drawEllipse()绘制椭圆
    .drawPath(QPainterPath)画路径

QPen(QColor/Qt.GlobalColor, width, Qt.PenStyle)画笔样式
    .setStyle(Qt.PenStyle)设置画笔样式
        Qt.PenStyle.SolidLine实线
        Qt.PenStyle.DashLine虚线
        Qt.PenStyle.DotLine点线
        Qt.PenStyle.DashDotLine点划线
        Qt.PenStyle.DashDotDotLine点划点线
        Qt.PenStyle.CustomDashLine自定义

QBrush(Qt.BrushStyle)刷子即填充样式
    .setStyle(Qt.BrushStyle)设置画刷样式
        Qt.BrushStyle.SolidPattern纯色
        Qt.BrushStyle.Dense1Pattern密度1
        Qt.BrushStyle.Dense2Pattern密度2
        Qt.BrushStyle.DiagCrossPattern斜线交叉
        Qt.BrushStyle.Dense5Pattern密度5
        Qt.BrushStyle.Dense6Pattern密度6
        Qt.BrushStyle.HorPattern横线
        Qt.BrushStyle.VerPattern竖线
        Qt.BrushStyle.BDiagPattern斜线

QPainterPath()画画路径
    .moveTo()方法用于移动画笔到指定的坐标
    cubicTo(QPoint, QPoint, QPoint)方法用于绘制三次贝塞尔曲线

"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Drawing text')
        self.show()

    # 绘制事件，重绘组件
    def paintEvent(self, event):
        # QPainter是绘图工具，用于绘制各种图形
        qp = QPainter()
        # begin(master)开始绘制，master是绘图区域
        qp.begin(self)

        self.drawText(event, qp)
        # end()结束绘制
        qp.end()

    def drawText(self, event, qp):
        # 设置画笔属性
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        # drawText()绘制文本
        qp.drawText(event.rect(), Qt.AlignmentFlag.AlignCenter, self.text)

        qb =QBrush(Qt.BrushStyle.SolidPattern)
        qp.setBrush(qb)
        qp.drawRect(10,10,20,20)

        qp.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.DashDotDotLine))
        qp.drawLine(100,100,10,100)



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

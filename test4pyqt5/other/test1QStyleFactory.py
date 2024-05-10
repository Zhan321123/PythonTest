"""
QStyleFactory
    .key() contain:['windowsvista', 'Windows', 'Fusion']
    .create(styleString)

QWidget
    .setStyle(QStyleFactory.create('windowsvista'))
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyleFactory, QCommonStyle, QPushButton, QMainWindow, QWidget, QApplication, QVBoxLayout, \
    QGroupBox, QFrame

print(QStyleFactory.keys())
print(QStyleFactory.create('windowsvista'))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    g = QGroupBox("styles")
    w = QFrame(g)

    qv = QVBoxLayout()
    qv.setSpacing(20)
    qv.setAlignment(Qt.AlignAbsolute)
    b1 = QPushButton("windowsvista")
    b1.setStyle(QStyleFactory.create('windowsvista'))
    b2 = QPushButton("Windows")
    b2.setStyle(QStyleFactory.create('Windows'))
    b3 = QPushButton("Fusion")
    b3.setStyle(QStyleFactory.create('Fusion'))

    qv.addWidget(b1)
    qv.addWidget(b2)
    qv.addWidget(b3)

    w.setLayout(qv)

    g.setGeometry(100, 100, 300, 200)
    g.show()
    sys.exit(app.exec_())

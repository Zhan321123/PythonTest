"""
QRadioButton()
    setChecked(boolean)设置是否选择
    clicked.connect(method)绑定点击事件

QButtonGroup()，同一个组内的按钮只能选择一个按钮组
    addButton(QRadioButton)添加按钮
    buttonClicked.connect(method)绑定组内点击事件
"""

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QApplication, QButtonGroup, QStyleFactory


class ColorPreferenceWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建按钮组
        self.color_group = QButtonGroup(self)

        # 定义颜色选项及其对应的QRadioButton
        color_options = {
            "红色": QRadioButton("红色", self),
            "蓝色": QRadioButton("蓝色", self),
            "绿色": QRadioButton("绿色", self)
        }

        # 将QRadioButton添加到按钮组中，确保互斥
        for radio_button in color_options.values():
            self.color_group.addButton(radio_button)

        # 布局管理
        layout = QVBoxLayout()

        # 添加单选按钮到布局
        for option_text, radio_button in color_options.items():
            layout.addWidget(radio_button)

        # 设置窗口布局
        self.setLayout(layout)

        # 连接信号槽，处理单选按钮被点击时的事件
        self.color_group.buttonClicked.connect(self.handle_color_selection)

    def handle_color_selection(self, selected_button):
        """处理用户选择颜色事件"""
        selected_color = selected_button.text()
        print(f"用户选择了颜色：{selected_color}")
        selected_button.setStyle(QStyleFactory.create("Fusion"))

        # 在实际应用中，可以在此处执行与所选颜色相关的逻辑操作


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ColorPreferenceWindow()
    window.setWindowTitle("颜色偏好选择")
    window.resize(300, 100)
    window.show()

    sys.exit(app.exec_())

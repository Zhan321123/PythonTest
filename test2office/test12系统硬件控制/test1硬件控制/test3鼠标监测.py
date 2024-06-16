"""
TODO 未完成
"""
import pynput

# 如果鼠标移动到左上角，就输出hello
from pynput.mouse import Listener

while True:
    mouse = pynput.mouse.Controller()
    if mouse.position[0] < 100 and mouse.position[1] < 100:
        print("hello")
        break

# 如果鼠标左键点击，就输出hello
# def on_click(x, y, button, pressed):
#     """点击事件的回调函数"""
#     if button.name == 'left' and pressed:  # 只有在按钮被按下时才输出
#         print("Hello")
# with Listener(on_click=on_click) as listener:
#     listener.join()

# 监听鼠标滚轮滚动事件与数据
def on_scroll(x, y, dx, dy):
    """滚动事件的回调函数"""
    print('Mouse scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

with Listener(on_scroll=on_scroll) as listener:
    listener.join()
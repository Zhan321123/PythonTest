"""
TODO 未完成
"""
import pynput

# 如果鼠标移动到左上角，就输出hello
from pynput import mouse
from pynput.keyboard import Key
# from pynput.keyboard import Listener
from pynput.mouse import Listener, Button

# while True:
#     mouse = pynput.mouse.Controller()
#     if mouse.position[0] < 100 and mouse.position[1] < 100:
#         print("hello")
#         break

# 如果鼠标左键点击，就输出hello


def on_click(x, y, button, pressed):
    """点击事件的回调函数"""
    global stop_listener
    if button == Button.left and pressed:  # 直接比较Button对象
        print(f"Clicked at point: {x}, {y}")
        # 设置标志位为True准备停止监听
        stop_listener = True

stop_listener = False
with mouse.Listener(on_click=on_click) as listener_instance:
    # 监听会在这里运行，直到stop_listener变为True
    while not stop_listener:
        listener_instance.join(0.1)  # 每100毫秒检查一次stop_listener状态
print("end")



# stop = False
# def on_click(x, y, button, pressed):
#     """点击事件的回调函数"""
#     global stop
#     if button.name == 'left' and pressed:  # 只有在按钮被按下时才输出
#         print(f"point: {x}, {y}")
#         stop = True
# with Listener(on_click=on_click) as listener:
#     if not stop:
#         listener.join()
#     else:
#         listener.stop()
# print("end")

# 监听鼠标滚轮滚动事件与数据
# def on_scroll(x, y, dx, dy):
#     """滚动事件的回调函数"""
#     print('Mouse scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))
#
# with Listener(on_scroll=on_scroll) as listener:
#     listener.join()

# 如果鼠标点击左键，就打印鼠标的位置
# def on_click(x, y, button, pressed):
#     """点击事件的回调函数"""
#     if pressed:
#         print('Mouse clicked at {0}'.format(
#             (x, y)))
#
# with Listener(on_click=on_click) as listener:
#     listener.join()


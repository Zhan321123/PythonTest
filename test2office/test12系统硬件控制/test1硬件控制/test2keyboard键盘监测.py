"""
keyboard库
可以实现：
    监测键盘点击事件
不能实现：
    监测鼠标点击事件

keyboard
    .is_pressed(" ") 监测键盘是否按住了空格
    .is_pressed("ctrl") and .is_pressed("c") 监测 ctrl+c
    .press_and_release('g') 键盘点击一下G键
"""
import time

import keyboard

# 按空格时输出hello
# while True:
#     if keyboard.is_pressed(' '):
#         print("hello")
#         break

# 键盘点击一下G键
# keyboard.press_and_release('g')

def on_key_press(event):
    """按键事件的回调函数"""
    print(f"Key pressed: {event.name}")
# 开始监听键盘事件
keyboard.on_press(on_key_press)
# 使程序保持运行，以便持续监听
while True:
    if keyboard.is_pressed("esc"):
        keyboard.unhook_all()
        break
    else:
        time.sleep(0.1)
print("Listening stopped.")

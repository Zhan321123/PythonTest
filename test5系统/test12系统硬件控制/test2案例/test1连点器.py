"""
"""
import pyautogui as og
import keyboard as kb
import pynput as pp
from objprint import objprint


def click2():
    def on_click(x, y, button, pressed):
        """鼠标点击事件的回调函数"""
        if button == pp.mouse.Button.right and pressed:  # 检查是否为鼠标右键按下
            print(f"Right mouse button clicked at ({x}, {y})")

    while True:
        if kb.is_pressed('ctrl'):
            with pp.mouse.Listener(on_click=on_click) as listener:
                listener.join()
            if kb.is_pressed('q'):
                print('end')
                break



if __name__ == '__main__':
    click2()

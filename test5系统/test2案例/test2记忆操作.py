"""
TODO 目前完成一半
"""

import time
import threading

import keyboard as kb
import pynput as pp
import pyautogui as pg


# class MemoryClicks:
#     def __init__(self):
#         pass
#
#     stop = False
#     points = []
#
#     def __onClick(self, x, y, button, pressed):
#         """点击事件的回调函数"""
#         if button == pp.mouse.Button.left and pressed:  # 直接比较Button对象
#             print(f"Clicked at point: {x}, {y}")
#             self.points.append(["mouse", x, y])
#             # 设置标志位为True准备停止监听
#             self.stop = True
#
#     def __onKeyPress(self, event):
#         """按键事件的回调函数"""
#         print(f"Key pressed: {event.name}")
#         self.points.append(['key', event.name])
#
#
#     def _recordClick(self):
#         isStop = False
#         while not isStop:
#
#     def _startMemory(self):
#         threading.Thread().start()
#         threading.Thread().start()
#
#     def _startOperation(self):
#         pass
#
#     def start(self):
#         self._startMemory()

class MemoryClicks:
    """
        使用方法：
    先运行 -> 按q开始记录 -> 左击需要点击的东西 -> 按右键结束记录 -> 按q开始重复操作
        注意：
    仅记录鼠标的点击行为
    点击Esc结束程序
    """

    def __init__(self):
        pass

    points = []
    stop = False

    def on_click(self, x, y, button, pressed):
        if pressed:
            if button == pp.mouse.Button.left:
                print(f"Clicked at point: {x}, {y}")
                self.points.append([x, y])
            if button == pp.mouse.Button.right:
                self.stop = True

    def startRecord(self):
        with pp.mouse.Listener(on_click=self.on_click) as listener:
            while not self.stop:
                listener.join(0.1)
        print(self.points)
        self.stopRecord()

    def stopRecord(self):
        while True:
            if kb.is_pressed('q'):
                self.startOperation()
                break

    def startOperation(self):
        for x, y in self.points:
            time.sleep(0.2)
            pg.moveTo(x, y)
            time.sleep(0.1)
            pg.click(button='left')

    def start(self):
        while True:
            if kb.is_pressed('q'):
                print("q")
                self.startRecord()
                break
        while True:
            if kb.is_pressed('q'):
                self.startOperation()
            elif kb.is_pressed('esc'):
                break


if __name__ == '__main__':
    m = MemoryClicks()
    m.start()

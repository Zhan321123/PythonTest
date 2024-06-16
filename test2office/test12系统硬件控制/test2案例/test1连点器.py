"""
实现案例：
    当按下 ctrl 和 q 时，右击10下鼠标
"""
import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
        for i in range(10):
            pyautogui.leftClick()
            print('ctrl+q')


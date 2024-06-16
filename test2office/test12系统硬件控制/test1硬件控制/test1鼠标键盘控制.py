"""
pyautogui库的使用
可以实现：
    控制鼠标移动，点击，滚动，拖拽
    控制键盘点击，按住
不能实现：
    监测鼠标点击，键盘点击

pyautogui
    .position() 获取鼠标位置，左上角(0,0) ~ 右下角(1920,1080)
    .moveTo(x:int, y:int, duration=float) 移动鼠标到指定位置，可以指定时间
    .click(x=int,y=int) 鼠标左点击一下
    .click(button='right') 鼠标右击一下
    .click(button='middle') 鼠标中键一下
    .dragTo(x:int,y:int, duration:float, button=str) 按住鼠标移动至指定位置
    .scroll(h:int) h为正时向上滚动，为负时向下滚动，按住shift的同时，变为左右滚动
    .keyDown('shift') 按下shift按键，不松开 .keyUp('shift') 松开按键
    .press('a') 按一下a键
    .hotkey('ctrl', 'c') 同时按下ctrl和c键

"""

import pyautogui as pg

print(pg.position())  # 获取鼠标位置
# pg.click()  # 鼠标点击
# pg.moveTo(100, 100, duration=1)  # 将鼠标移动到(100,100)，持续时间5秒
# pg.click(button='right')  # 鼠标右击
# pg.click(button='middle')# 鼠标中键
# pg.dragTo(1082, 528, 1, button='left')# 按住左键移动到1082，528

# 滑动鼠标滚轮
# pg.scroll(100)
# pg.scroll(-100)

# pg.keyDown('shift')# 按住shift键
# pg.scroll(-100)
# pg.keyUp('shift')

# pg.press('a')# 按一下a键
pg.hotkey('ctrl', 'c')# 同时按下ctrl和c键

"""
动态数据gif
"""
import os
from typing import Sequence
import numpy as np
from matplotlib import pyplot as plt
import io
from PIL import Image


def movingImage(dss: Sequence[Sequence], xs: Sequence, titles:Sequence,savePath: str):
    imgs = []
    for i in range(len(dss)):
        buf = io.BytesIO()
        plt.figure()
        plt.barh(xs, dss[i])
        plt.title(titles[i])
        plt.savefig(buf, format='png')
        buf.seek(0)
        image = Image.open(buf)
        imgs.append(image)
        plt.close() # 关闭当前图片减少运存占用
    imgs[0].save(savePath+'.gif', save_all=True, append_images=imgs[1:], duration=50, loop=0)


if __name__ == '__main__':
    # 假设四种手机100年的销量变化
    d = np.array((np.arange(0, 300, 3),
                  np.arange(0, 400, 4),
                  np.arange(400, 300, -1),
                  np.arange(1000, 0, -10))).T # 数据
    x = ['apple', 'huawei', 'xiaomi', 'vivo'] # x轴
    t = np.arange(2000,2100) # 标题
    sp = rf"{os.environ['USERPROFILE']}\Desktop\output" # 保存路径为桌面

    movingImage(d, x,t, sp)

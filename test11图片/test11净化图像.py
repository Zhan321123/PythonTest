import os

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


def purifyImage(image, num_colors):
    """
    净化图像，聚集颜色以减少颜色数量

    :param image: 图像
    :param num_colors: 颜色数量
    :return: 净化后的图像
    """
    image = image.convert("RGBA")  # 将图像转换为RGBA模式
    width, height = image.size
    pixels = np.array(image)  # 将图像数据转换为NumPy数组
    # 提取非透明像素
    non_transparent_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[y, x]
            if a > 0:
                non_transparent_pixels.append([r, g, b])

    non_transparent_pixels = np.array(non_transparent_pixels)

    if len(non_transparent_pixels) > 0:
        # 使用KMeans聚类算法将非透明像素分为num_colors类
        kmeans = KMeans(n_clusters=num_colors, random_state=42)
        kmeans.fit(non_transparent_pixels)

        new_colors = kmeans.cluster_centers_.astype(int)  # 获取聚类中心，即代表颜色

        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[y, x]
                if a > 0:
                    # 找到该像素所属的聚类
                    cluster_index = kmeans.predict([[r, g, b]])[0]
                    # 将该像素的颜色设置为聚类中心的颜色
                    new_r, new_g, new_b = new_colors[cluster_index]
                    pixels[y, x] = [new_r, new_g, new_b, a]

    new_image = Image.fromarray(pixels)  # 将NumPy数组转换回PIL图像
    return new_image


if __name__ == '__main__':
    dirty = r"D:\code\minecraft\WorldFillMachine\worldFillMachine-forge-1.20.1\src\main\resources\assets\worldfill\textures\mob_effect\falling_immunity.png"
    img = Image.open(dirty)
    new_image = purifyImage(img, 24)
    new_image.save(r"D:\code\minecraft\WorldFillMachine\worldFillMachine-forge-1.20.1\src\main\resources\assets\worldfill\textures\mob_effect\falling_immunity1.png")

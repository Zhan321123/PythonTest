"""
生成二维码


"""
import matplotlib
import qrcode
from PIL import Image
import json

# JSON序列化
text_data = json.dumps({'name': '张三', 'age': 18, 'sex': '男'})

# 创建二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(text_data)
qr.make(fit=True)

# 生成二维码图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图片
img.save("file/qrCode.png")

# 若需在matplotlib中显示（非必需，但可以）
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# 将二维码图像转换为matplotlib可用的形式
img_matplotlib = plt.imread("file/qrCode.png")

# 显示二维码
plt.imshow(img_matplotlib)
plt.axis('off')  # 移除坐标轴
plt.show()
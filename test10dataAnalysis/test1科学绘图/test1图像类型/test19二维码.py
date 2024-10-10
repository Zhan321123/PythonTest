"""
生成二维码与解析二维码


"""
import matplotlib
import qrcode
from PIL import Image
import json
from pyzbar.pyzbar import decode


def encodeQR(text,savePath="qrCode.png"):
    """生成二维码方法"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    text = json.dumps(text)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"file/{savePath}")

def decodeQR(imgPath):
    """解析二维码方法"""
    img = Image.open(imgPath)
    de = decode(img)
    print(de)

encodeQR({'name': '张三', 'age': 18, 'sex': '男'})
decodeQR("file/qrCode.png")
decodeQR('file/wifiPassword.jpg')


import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
img_matplotlib = plt.imread("../file/qrCode.png")
plt.imshow(img_matplotlib)
plt.axis('off')  # 移除坐标轴
plt.show()
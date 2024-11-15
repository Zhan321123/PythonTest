from lxml import etree
from docx import Document
from docx.shared import Cm
import os

def save_images_from_docx(docx_path, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开文档
    doc = Document(docx_path)

    # 计数器，用于给图片命名
    img_count = 1

    # 遍历文档中的所有图片
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            # 获取图片数据
            image_part = rel.target_part
            image_ext = image_part.partname.split('.')[-1]

            # 构建图片文件名
            image_filename = f'image_{img_count}.{image_ext}'
            image_filepath = os.path.join(output_folder, image_filename)

            # 写入图片数据到文件
            with open(image_filepath, 'wb') as f:
                f.write(image_part.blob)

            print(f'Saved {image_filepath}')
            img_count += 1

# 指定.docx文件路径和输出文件夹
docx_path = r"C:\Users\刘高瞻\Desktop\2024-7-2023毕业设计整合论文\4毕设整合3.0.docx"
output_folder = r"C:\Users\刘高瞻\Desktop"

# 调用函数
save_images_from_docx(docx_path, output_folder)

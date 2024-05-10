"""
第三方包pdfplumber的测试
用于pdf的读取
"""
import pdfplumber

with pdfplumber.open('../file/p.pdf') as pdf:
    for i in pdf.pages:
        print(i.extract_text())
        print(f'-----------------page {i.page_number}')

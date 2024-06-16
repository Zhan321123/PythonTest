"""
第三方包openpyxl的测试
保存表格
"""

import openpyxl
# 新建表格工作簿
workbook = openpyxl.Workbook()
# 新建表格sheet
sheet = workbook.create_sheet('sheet-1')

# sheet.append(序列)，写入操作
for i in [(1,'zhan',18,'male'),(2,'xiao',20,'female'),(2,'duo',23,'male')]:
    sheet.append(i)
# 保存表格
workbook.save('file/excel2.xlsx')
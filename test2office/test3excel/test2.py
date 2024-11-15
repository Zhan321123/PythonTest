"""
查看表格
"""
import openpyxl

# 打开表格工作簿
workbook = openpyxl.load_workbook('../file/excel2.xlsx')
# 打开表格
sheet = workbook['sheet-1']

# sheet.rows，获取表格行对象
# sheet.rows[i].value，获取单元格数据
l = []
for i in sheet.rows:
    rs = []
    for j in i:
        rs.append(j.value)
    l.append(rs)

for i in l:
    print(i)

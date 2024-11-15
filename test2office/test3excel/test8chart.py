"""
在excel创建图表chart

BarChart()
PieChart()
"""
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active

rows = [
    ('月份', '苹果', '香蕉'),
    (1, 43, 25),
    (2, 10, 30),
    (3, 40, 60),
    (4, 50, 70),
    (5, 20, 10),
    (6, 10, 40),
    (7, 50, 30),
]

for row in rows:
    ws.append(row)

chart1 = BarChart()
chart1.type = "col"
chart1.style = 10
chart1.title = "销量柱状图"
chart1.y_axis.title = '销量'
chart1.x_axis.title = '月份'

data = Reference(ws, min_col=2, min_row=1, max_row=8, max_col=3)
series = Reference(ws, min_col=1, min_row=2, max_row=8)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(series)
ws.add_chart(chart1, "A10")

wb.save('../file/excel3.xlsx')
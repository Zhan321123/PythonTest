"""
课程表表格图


"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib


matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 同样的数据
data = {'课程时段': ['第一节\n8:10-8:50', '第二节\n8:55-9:35', '第三节\n9:50-10:30', '第四节\n10:35-11:15', '第五节\n11:20-12:00',
                 '第六节\n13:30-14:10', '第七节\n14:15-14:55', '第八节\n15:05-15:45', '第九节\n15:50-16:30', '第十节\n18:00-∞'],
        '周一': ["", "", "材料力学\n求实南305", "材料力学\n求实南305", "",
               "工程水文学\n求实南205", "工程水文学\n求实南205", "", "", ""],
        '周二': ["毛概\n求实南214", "毛概\n求实南214", "体育\n体育馆", "体育\n体育馆", "",
               "工程测量\n求实南206", "工程测量\n求实南206", "形策\n求实北109", "形策\n求实北109", "电工学\n求实南201"],
        '周三': ["", "", "水力学\n求实北306", "水力学\n求实北306", "水力学\n求实北306",
               "", "", "", "", ""],
        '周四': ["工程测量\n求实南206", "工程测量\n求实南206", "", "", "",
               "习思想\n求实南311", "习思想\n求实南311", "习思想\n求实南311", "", "绿色建筑\n求实北312"],
        '周五': ["工程水文学\n求实南205", "工程水文学\n求实南205", "水力学\n求实北306", "水力学\n求实北306", "水力学\n求实北306",
               "电工学\n求实南201", "电工学\n求实南201", "材料力学\n求实南305", "材料力学\n求实南305", ""],
        }

# 将字典转换为DataFrame
df = pd.DataFrame(data)

# 初始化figure和axes
fig, ax = plt.subplots(figsize=(10, 6))

# 创建一个table
table = ax.table(cellText=df.values, colLabels=df.columns,
                 loc='center', cellLoc='center', bbox=[0, 0, 1, 1])

# 更改表格样式


# 隐藏坐标轴
ax.axis('off')
# 显示表格
plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import skill_metrics as sm

matplotlib.use('TkAgg')
# 以下操作可以当作固定步骤
taylor_stats1 = sm.taylor_statistics(np.random.rand(100), np.random.rand(100))
taylor_stats2 = sm.taylor_statistics(np.random.rand(100), np.random.rand(100))
taylor_stats3 = sm.taylor_statistics(np.random.rand(100), np.random.rand(100))
sdev = np.array([taylor_stats1['sdev'][0], taylor_stats1['sdev'][1],
                 taylor_stats2['sdev'][1], taylor_stats3['sdev'][1]])
crmsd = np.array([taylor_stats1['crmsd'][0], taylor_stats1['crmsd'][1],
                  taylor_stats2['crmsd'][1], taylor_stats3['crmsd'][1]])
ccoef = np.array([taylor_stats1['ccoef'][0], taylor_stats1['ccoef'][1],
                  taylor_stats2['ccoef'][1], taylor_stats3['ccoef'][1]])

# 开始绘图
sm.taylor_diagram(sdev, crmsd, ccoef)
plt.show()

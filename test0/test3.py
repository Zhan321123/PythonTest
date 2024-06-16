"""

"""

import math

import numpy as np
import matplotlib.pyplot as plt
from pandas import Timestamp
from scipy.stats import norm
import matplotlib

matplotlib.use('TkAgg')
from scipy import stats
import pandas as pd
from scipy.integrate import quad

StandardNormalDistribution_24 = [[0.9973002039367399, ],
                                 [0.49865010196836995, 0.49865010196836995, ],
                                 [0.15730535589982697, 0.682689492137086, 0.15730535589982697, ],
                                 [0.06545730323722798, 0.4331927987311419, 0.4331927987311419, 0.06545730323722798, ],
                                 [0.03458042108129572, 0.23832279863714778, 0.45149376449985285, 0.2383227986371479,
                                  0.034580421081295734, ],
                                 [0.02140023391654912, 0.13590512198327787, 0.341344746068543, 0.341344746068543,
                                  0.13590512198327787, 0.02140023391654912, ],
                                 [0.014712387572198234, 0.08320911123950271, 0.23484617405429375, 0.33176485820475066,
                                  0.23484617405429367, 0.08320911123950271, 0.014712387572198234, ],
                                 [0.010874574623414613, 0.054582728613813386, 0.15982015110801015, 0.27337264762313185,
                                  0.27337264762313185, 0.15982015110801015, 0.054582728613813386,
                                  0.010874574623414613, ],
                                 [0.00846543059701524, 0.03797502364416936, 0.11086490165864228, 0.21078608625030654,
                                  0.2611173196364727, 0.2107860862503067, 0.11086490165864245, 0.037975023644169416,
                                  0.00846543059701526, 0.0012270316416649475, ],
                                 [0.0068476378929660355, 0.02773278318832971, 0.07913935110878251, 0.15918344752836536,
                                  0.22574688224992645, 0.22574688224992642, 0.15918344752836533, 0.07913935110878247,
                                  0.027732783188329658, 0.0068476378929660355, ],
                                 [0.005703243442059675, 0.021072041167293668, 0.05821583806839076, 0.12028566703744598,
                                  0.1859047465269595, 0.2149371314524406, 0.18590474652695954, 0.12028566703744606,
                                  0.05821583806839081, 0.021072041167293668, 0.0057032434420596885,
                                  0.0011539297423802113, ],
                                 [0.004859767294146042, 0.016540466622403077, 0.04405706932067886, 0.091848052662599,
                                  0.14988228479452986, 0.19146246127401312, 0.19146246127401312, 0.14988228479452986,
                                  0.091848052662599, 0.04405706932067886, 0.016540466622403077, 0.004859767294146042, ],
                                 [0.004217153991234831, 0.013337277712325814, 0.03420938515481136, 0.07116790921858912,
                                  0.12009043608466262, 0.1643749829884368, 0.18250591363661936, 0.16437498298843667,
                                  0.1200904360846625, 0.07116790921858898, 0.03420938515481127, 0.013337277712325776,
                                  0.004217153991234815, ],
                                 [0.0037140972430652393, 0.010998290329132967, 0.027175847143004497,
                                  0.056033264096498156, 0.09641157231044499, 0.1384346017438487, 0.1658824291023753,
                                  0.16588242910237533, 0.13843460174384875, 0.09641157231044505, 0.05603326409649824,
                                  0.027175847143004517, 0.010998290329132989, 0.003714097243065248,
                                  0.0010465146088120651, ],
                                 [0.0033112899920886576, 0.009242259489779851, 0.02202687159942719, 0.04482634012084521,
                                  0.07789859469768597, 0.1155978638186165, 0.1464871728108234, 0.1585194188782061,
                                  0.14648717281082343, 0.11559786381861661, 0.07789859469768605, 0.044826340120845284,
                                  0.022026871599427202, 0.009242259489779872, 0.0033112899920886576,
                                  0.0010129687659532162, ],
                                 [0.0029825503313824645, 0.007892024292032146, 0.018171889110216676,
                                  0.03641083950359669, 0.0634873158679508, 0.09633283524005935, 0.127202880950408,
                                  0.1461697666727238, 0.1461697666727238, 0.127202880950408, 0.09633283524005935,
                                  0.0634873158679508, 0.03641083950359669, 0.018171889110216676, 0.007892024292032146,
                                  0.0029825503313824645, ],
                                 [0.0027098633637454798, 0.006832109590477856, 0.015226567055886663,
                                  0.02999813344240783, 0.05224395960537823, 0.08043245664759831, 0.10946693162618465,
                                  0.13170220725579798, 0.1400757467617864, 0.13170220725579793, 0.10946693162618455,
                                  0.08043245664759822, 0.05224395960537816, 0.029998133442407773, 0.015226567055886611,
                                  0.006832109590477841, 0.0027098633637454733, ],
                                 [0.0024804825359596447, 0.005984948061055609, 0.01293480331953387,
                                  0.025040220324635515, 0.04342086745305316, 0.06744403420558918, 0.09383728361546585,
                                  0.11694880263484071, 0.1305586598182364, 0.1305586598182364, 0.11694880263484073,
                                  0.09383728361546587, 0.06744403420558918, 0.04342086745305319, 0.025040220324635515,
                                  0.01293480331953389, 0.005984948061055609, 0.0024804825359596447, ],
                                 [0.0022851674880348576, 0.005297030736407192, 0.011122064968608512,
                                  0.021153361147721123, 0.03644320724115976, 0.056872058879529445, 0.08039481381818167,
                                  0.10294495494358666, 0.11940731546154386, 0.12546025456719423, 0.11940731546154382,
                                  0.10294495494358658, 0.08039481381818156, 0.05687205887952939, 0.0364432072411597,
                                  0.021153361147721088, 0.011122064968608486, 0.005297030736407178,
                                  0.002285167488034852, ],
                                 [0.002117075771410573, 0.004730562121555456, 0.009666884638220413, 0.01806589855010923,
                                  0.03087688215593225, 0.04826246895285018, 0.06899045512505123, 0.09019299240331409,
                                  0.10783546006097379, 0.11791142218895265, 0.11791142218895265, 0.10783546006097382,
                                  0.09019299240331415, 0.06899045512505125, 0.04826246895285024, 0.03087688215593228,
                                  0.01806589855010925, 0.009666884638220432, 0.004730562121555468, 0.002117075771410578,
                                  0.0008664738892463196, ],
                                 [0.001971044706583221, 0.004258276700506408, 0.00848306616510858, 0.015583130512844313,
                                  0.026396150752654838, 0.04122982997400343, 0.05938385708812597, 0.0788700080955194,
                                  0.09659230887064814, 0.10908393228590708, 0.1135969936329364, 0.10908393228590714,
                                  0.09659230887064825, 0.07887000809551951, 0.05938385708812612, 0.04122982997400355,
                                  0.02639615075265491, 0.01558313051284437, 0.008483066165108615, 0.004258276700506427,
                                  0.0019710447065832306, 0.000841277356465773, ],
                                 [0.0018431136097234308, 0.0038601298323362393, 0.007508335602502734,
                                  0.013563705564790885, 0.022756569834645378, 0.03545926823374533, 0.051315422551607016,
                                  0.06897024448583888, 0.08609377953764331, 0.09981096698931612, 0.1074685657262203,
                                  0.10746856572622031, 0.09981096698931621, 0.0860937795376434, 0.068970244485839,
                                  0.05131542255160713, 0.03545926823374542, 0.02275656983464545, 0.013563705564790937,
                                  0.007508335602502763, 0.003860129832336257, 0.00184311360972344,
                                  0.0008173220303439348, ],
                                 [0.0017301983876525737, 0.003521132435882664, 0.006696952852515702,
                                  0.011903680350964448, 0.019774023352157652, 0.030698642213391077, 0.04454040107435316,
                                  0.06039490890849455, 0.07653465575100395, 0.09064164938098279, 0.10032508181119382,
                                  0.10377755089955494, 0.10032508181119384, 0.09064164938098282, 0.07653465575100402,
                                  0.06039490890849456, 0.044540401074353184, 0.030698642213391105, 0.019774023352157662,
                                  0.011903680350964459, 0.006696952852515716, 0.003521132435882664,
                                  0.0017301983876525779, 0.0007945424272987822, ],
                                 [0.001629865203424463, 0.0032299020907215798, 0.006014807329268569,
                                  0.010525659293134506, 0.017309024915637884, 0.02674804440504098, 0.038842572397997197,
                                  0.053005480264601806, 0.06797209844541116, 0.08191018634911873, 0.09275613559108939,
                                  0.09870632568292374, 0.09870632568292374, 0.09275613559108939, 0.08191018634911873,
                                  0.06797209844541116, 0.053005480264601806, 0.038842572397997197, 0.02674804440504098,
                                  0.017309024915637884, 0.010525659293134506, 0.006014807329268569,
                                  0.0032299020907215798, 0.001629865203424463, ],
                                 ]


def d(t: Timestamp, h: float, duration: float):
    values = {}
    if duration == 0 or h == 0:
        return values
    timeStart = t.ceil('h')
    timeEnd = (t + pd.Timedelta(hours=duration)).ceil('h') - pd.Timedelta(hours=1)
    timeSeries = pd.date_range(start=timeStart, end=timeEnd, freq='h')

    d = len(timeSeries)
    for index, i in enumerate(timeSeries):
        values[i] = h * StandardNormalDistribution_24[d - 1][index]
        if index==0:
            values[i]+=h*0.0027
    return values


d = d(Timestamp(2007, 1, 1, 0, 0, 0), 100, 2)
for i in d:
    print(i, d[i])

# def integrand(x):
#     return math.e**(-(x**2)/2)/math.sqrt(2*math.pi)
# for i in range(1,25):
#     step = -3
#     print("[",end="")
#     while step<3:
#         print(quad(integrand, step, step+6/i)[0],end=',')
#         step += 6/i
#     print("],")

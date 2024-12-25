"""
运筹学-线型规划
"""
import itertools

from scipy import optimize

# 目标函数系数
# 如果是max，系数就要取反！！！
cos = [-3, 4, -2, 5]
# 等式约束
# ([[等式1系数],[...]], [等式1结果,...])
# 没有等式约束就写成 equal = ([[0,...]],[0])
eqs = ([[4, -1, 2, -1]],
      [-2])
# 不等式约束
# ([[不等式1系数],[...]], [不等式1结果,...])
# 如果是>=，系数和结果都取反！！！
ineqs = ([[1, 1, 3, -1],
          [2, -3, 1, -2]],
         [14, -2])
# 变量范围
# [[下限,上限],[...]]，None表示infinity
# 注意变量的数量！！！
xrs = [[0, None], [0, None], [0, None], [0, None]]


def linProgDetection(coefficient: list, inequality, equation, xRange: list[list]):
    """
    线型规划问题的变量输入检测
    :param coefficient: 目标函数系数
    :param inequality: 不等式约束
    :param equation: 等式约束
    :param xRange: 变量范围
    """
    ineqCo, ineqVa = inequality
    eqCo, eqVa = equation
    # 变量输入监测
    if len(ineqCo) != len(ineqVa): print("(等式约束的个数)与(结果个数)不一致");return
    if len(eqCo) != len(eqVa): print("(不等式约束的个数)与(结果个数)不一致");return
    if len(xRange) != len(coefficient): print("(目标函数系数)与(变量范围个数)不一致");return
    # 问题描述
    print("根据你所填的变量，该线型规划问题条件是：{")
    minZ = " +".join(list(f"{i}x{index}" for index, i in enumerate(coefficient)))
    maxZ = " +".join(f"{-i}x{index}" for index, i in enumerate(coefficient))
    print(f"\tmin(z) = {minZ} 或 max(z) = {maxZ} ;")
    for l, r in zip(eqCo, eqVa):
        l1 = " +".join(list(f"{i}x{index}" for index, i in enumerate(l)))
        print(f"\t{l1} = {r} ;")
    for l, r in zip(ineqCo, ineqVa):
        l1 = " +".join(f"{i}x{index}" for index, i in enumerate(l))
        l2 = " +".join(f"{-i}x{index}" for index, i in enumerate(l))
        print(f"\t{l1} <= {r} 或 {l2} >= {-r} ;")
    xR = list(
        f"{i[0] if i[0] is not None else '-无穷'} <x{index}< {i[1] if i[1] is not None else '+无穷'}" for index, i in
        enumerate(xRange))
    print(f"""\t{", ".join(xR)}""")
    print("}")


def linProg(coefficient: list, inequality, equation, xRange: list[list], method='highs'):
    """
    线性规划问题求最优解
    :param method: optimize的求解方法
    """
    ineqCo, ineqVa = inequality
    eqCo, eqVa = equation
    # 输出结果
    result = optimize.linprog(coefficient, ineqCo, ineqVa, eqCo, eqVa, xRange, method=method)
    print("结果{")
    print(f"\t目标函数值：{result.fun if result.success else '无解'}")
    if result.success:
        resultX = ", ".join(list(f"x{index}={i}" for index, i in enumerate(result.x)))
        print(f"\t最优解：{resultX}")
    print("}")
    return result.fun, result.x


def linProgInInt(coefficient: list, inequality, equation, xRange: list[list]):
    """
    线性规划问题求整数解
    :param coefficient: 目标函数系数
    :param inequality: 不等式约束
    :param equation: 等式约束
    :param xRange: 变量范围
    """
    ineqCo, ineqVa = inequality
    eqCo, eqVa = equation
    intRange = list(range(0, 30))
    # 取得所有可行解
    canCo = []
    iss = itertools.product(*([intRange] * len(xRange)))
    for i in iss:
        # 不等式约束
        for l, r in zip(ineqCo, ineqVa):
            if sum(i[index] * l[index] for index in range(len(i))) > r:
                break
        # 等式约束
        for l, r in zip(eqCo, eqVa):
            if sum(i[index] * l[index] for index in range(len(i))) != r:
                break
        else:
            canCo.append(i)
    # 确定最小值
    minValues = []
    for can in canCo:
        minValues.append(sum(ca * co for ca, co in zip(can, coefficient)))
    result = min(minValues)
    print("整数结果：{")
    print(f"\t函数值：{result}")
    print(f"\t最优解：{', '.join(list(f'x{index}={i}' for index, i in enumerate(canCo[minValues.index(result)])))}")
    print("}")

linProgDetection(cos, ineqs, eqs, xrs)
linProg(cos, ineqs, eqs, xrs, )
linProgInInt(cos, ineqs, eqs, xrs)

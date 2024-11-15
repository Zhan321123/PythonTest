"""
运筹学-线型规划
"""
from scipy import optimize

# 目标函数系数
# 如果是max，系数就要取反！！！
cs = [-3, 4, -2, 5]
# 等式约束
# ([[等式1系数],[...]], [等式1结果,...])
equal = ([[4, -1, 2, -1]],
         [-2])
# 不等式约束
# ([[不等式1系数],[...]], [不等式1结果,...])
# 如果是>=，系数和结果都取反！！！
As = ([[1, 1, 3, -1],
      [2, -3, 1, -2]],
     [14, -2])
# 变量范围
# [[下限,上限],[...]]，None表示infinity
# 注意变量的数量！！！
xr = [[0, None], [0, None], [0, None], [0, None]]


def linProg(c:list, A:list[list], B:list, e:list[list], E:list, xRange:list[list], method='highs'):
    """线性规划问题求最优解"""
    # 变量输入监测
    if len(A) != len(B): print("(等式约束的个数)与(结果个数)不一致");return
    if len(e) != len(E): print("(不等式约束的个数)与(结果个数)不一致");return
    if len(xRange) != len(c): print("(目标函数系数)与(变量范围个数)不一致");return
    # 问题描述
    print("根据你所填的变量，该问题条件是：{")
    minZ = " + ".join(list(f"{i}x{index}" for index, i in enumerate(c)))
    maxZ = " + ".join(f"{-i}x{index}" for index, i in enumerate(c))
    print(f"    min(z) = {minZ} 或 max(z) = {maxZ} ;")
    for l, r in zip(e, E):
        l1 = " + ".join(list(f"{i}x{index}" for index, i in enumerate(l)))
        print(f"    {l1} = {r} ;")
    for l, r in zip(A, B):
        l1 = " + ".join(f"{i}x{index}" for index, i in enumerate(l))
        l2 = " + ".join(f"{-i}x{index}" for index, i in enumerate(l))
        print(f"    {l1} <= {r} 或 {l2} >= {-r} ;")
    xR = list(
        f"{i[0] if i[0] is not None else '-无穷'} <x{index}< {i[1] if i[1] is not None else '+无穷'}" for index, i in
        enumerate(xRange))
    print(f"""    {", ".join(xR)}""")
    print("}")
    # 输出结果
    result = optimize.linprog(c, A, B, e, E, xRange, method=method)
    print("规划结果为{")
    print(f"    目标函数值：{result.fun if result.success else '无解'}")
    if result.success:
        resultX = ", ".join(list(f"x{index}={i}" for index, i in enumerate(result.x)))
        print(f"    最优解：{resultX}")
    print("}")
    return result.fun, result.x


res = linProg(cs, As[0], As[1], equal[0], equal[1], xr, )

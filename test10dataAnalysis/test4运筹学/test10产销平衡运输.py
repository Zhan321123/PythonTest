"""
运筹学-产销平衡或不平衡下的运输问题（指派问题）
"""
from scipy import optimize

# 运费
f = [[13.1, 11.8, 19.5, 9],
     [7.6, 6.6, 11.4, 7.2],
     [10.2, 9.7, 12.2, 11.1]]
# 产量
p = [60, 100, 120]
# 销量
s = [30, 20, 80, 90]


def ProductionSalesTransport(freight: list[list], product: list, sales: list):
    """产销平衡或不平衡下的运输问题"""
    # 检查数据
    if (len(freight) != len(product)) or (len(freight[0]) != len(sales)): print("长度不一致错误");return
    # 将数据转化为问题，用于手动检查
    print("问题描述-表格{")
    print(rf"""    产地\销地 | {"  ".join(f"销地{i}" for i in range(len(product)))} | 产量""")
    for i in range(len(product)):
        print(f"""     产地{i} | {"  ".join(f"{freight[i][j]}" for j in range(len(product)))} | {product[i]}""")
    print(rf"""     销量 | {"  ".join(f"{i}" for i in sales)} |""", )
    print("}")
    # 构造模型
    c = list(i for row in freight for i in row)
    xr = list([0, None] for _ in c)
    pb = list([0] * len(sales) * i + [1] * len(sales) + ([0] * len(sales)) * (len(product) - 1 - i) for i in
              range(len(product)))
    sb = list(([0] * i + [1] + [0] * (len(product) - i)) * (len(sales) - 1) for i in range(len(sales)))
    if sum(product) == sum(sales):
        status = "产 = 销，启动-产销平衡"
        A, B = [], []
        e = pb + sb
        E = product + sales
    elif sum(product) >= sum(sales):
        status = "产 > 销，启动-确保满足销售地"
        A, B = pb, product
        e, E = sb, sales
    else:
        status = "销 > 产，启动-尽量满足销售地"
        A, B = sb, sales
        e, E = pb, product
    result = optimize.linprog(c, A, B, e, E, xr, method='highs')
    # 输出结果
    print("运输规划结果为{")
    print(f"    产销状态：{status}")
    print(f"    总运费：{result.fun if result.success else '无解'}")
    x = None
    if result.success:
        x = list(map(float, result.x))
        x = list(list(x[i + j * len(product)] for i in range(len(sales))) for j in range(len(product)))
        print("    运输规划-表格{")
        print(fr"""        产地\销地 | {"  ".join(f"销地{i}" for i in range(len(product)))}""")
        for i in range(len(product)):
            print(f"""        产地{i} | {"  ".join(map(str, x[i]))}""")
        print("    }")
    print("}")
    return result.fun, x


res = ProductionSalesTransport(f, p, s)

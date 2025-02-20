"""
SL191-2008规范
"""
import math


def shouwanpeijin(K, M, b, h, fc, fy, fy_, cs, rho_min, xi_b, alpha_sb):
    if M > 200:
        a_s = cs + 35
    else:
        a_s = cs + 10
    as_ = cs + 10
    h0 = h - a_s
    alpha_s = K * M / fc / b / h0
    if alpha_s <= alpha_sb:
        print("满足不发生超筋要求，配置单筋")
        xi = 1 - math.sqrt(1 - 2 * xi_b)
        As = fc * b * xi * h0 / fy
        rho = As / b / h0
        if rho >= rho_min:
            print("满足不少筋要求，纵向受拉钢筋截面积", As)
        else:
            print("不满足不少筋要求，按最小配筋率rho_min纵向受拉钢筋截面积", As)
        return As
    else:
        print("不满足不发生超筋要求，配置双筋")
        alpha_s = alpha_sb
        As_ = (K * M - alpha_s * fc * b * h0 ** 2) / fy_ / (h0 - as_)
        As = (fc * b * xi_b * h0 + fy_ * As_) / fy
        print("纵向受拉钢筋截面积", As)
        print("纵向受压钢筋截面积", As_)
        return As, As_

def shouwanpeijinas_(K, M, b, h, fc, fy, fy_, cs, rho_min, xi_b, alpha_sb,as_):
    if M > 200:
        a_s = cs + 35
    else:
        a_s = cs + 10
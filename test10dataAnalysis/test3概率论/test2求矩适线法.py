import numpy as np

d = np.array((18500, 17700, 13900, 13300, 12800, 12100, 12000, 11500, 11200, 10800, 10800, 10700,
              10600, 10500, 9690, 8500, 8220, 8150, 8020, 8000, 7850, 7450, 7290, 6160, 5960,
              5950, 5590, 5490, 5340, 5220, 5100, 4520, 4240, 3650, 3220))

mean = d.mean()
cv = np.std(d, ddof=1) / mean
cs = skew(d)
alpha = 4 / cs ** 2
beta = 2 / mean / cv / cs
a0 = mean * (1 - 2 * cv / cs)

pdf = lambda x: gamma.pdf(x - a0, alpha, beta)
cdf = lambda x: 1 - gamma.cdf(x - a0, alpha, beta)
ppf = lambda p: gamma.ppf(p, alpha, beta)

print('数据长度:', len(d))
print('平均数:', mean)
print("cs:", cs)
print("cv", cv)
print('cs=n cv, n =', cs / cv)
print('gamma参数为：', alpha, beta, a0)

for p in ps:
    if 0 < p < 1:
        print(f'概率为{p * 100}%时的值:', (cdf(p) * cv + 1) * mean)
        print(f'概率为{(1 - p) * 100}%时的值:', (cdf(1 - p) * cv + 1) * mean)

plt.hist(d, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
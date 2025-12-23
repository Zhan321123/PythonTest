from math import factorial

import matplotlib
import numpy as np
import scipy
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

fig, axs = plt.subplots(3, 2)
axs = axs.flatten()

# poisson
poisson = lambda x, lamb: np.exp(-lamb) * lamb ** x / factorial(x)
xs = np.arange(0, 10)
axs[0].plot(xs, [poisson(x, 0) for x in xs], label='$\lambda=0$')
axs[0].plot(xs, [poisson(x, 0.1) for x in xs], label='$\lambda=0.1$')
axs[0].plot(xs, [poisson(x, 0.5) for x in xs], label='$\lambda=0.5$')
axs[0].plot(xs, [poisson(x, 1) for x in xs], label='$\lambda=1$')
axs[0].plot(xs, [poisson(x, 2) for x in xs], label='$\lambda=2$')
axs[0].set_title('Poisson')
axs[0].legend()
axs[0].set_ylim(0, 1)

# exponential
exponential = lambda x, lamb: lamb * np.exp(-lamb * x)
x = np.linspace(0, 6, 300)
axs[1].plot(x, [exponential(x, 0.1) for x in x], label='$\lambda=0.1$')
axs[1].plot(x, [exponential(x, 0.5) for x in x], label='$\lambda=0.5$')
axs[1].plot(x, [exponential(x, 1) for x in x], label='$\lambda=1$')
axs[1].plot(x, [exponential(x, 2) for x in x], label='$\lambda=2$')
axs[1].set_title('Exponential')
axs[1].legend()
axs[1].set_ylim(0)

# binomial
binomial = lambda x, n, p: factorial(n) / (factorial(x) * factorial(n - x)) * p ** x * (1 - p) ** (n - x)
xs = np.arange(0, 11)
axs[2].plot(xs, [binomial(x, 10, 0.5) for x in xs], label='$n=10, p=0.5$')
axs[2].plot(xs, [binomial(x, 10, 0.2) for x in xs], label='$n=10, p=0.2$')
axs[2].plot(xs, [binomial(x, 10, 0.8) for x in xs], label='$n=10, p=0.8$')
xs = np.arange(0, 6)
axs[2].plot(xs, [binomial(x, 5, 0.5) for x in xs], label='$n=5, p=0.5$')
axs[2].plot(xs, [binomial(x, 5, 0.8) for x in xs], label='$n=5, p=0.8$')
axs[2].set_title('Binomial')
axs[2].legend(framealpha=0.5)
axs[2].set_ylim(0, 1)

# geometric
geometric = lambda x, p: p * (1 - p) ** (x - 1)
xs = np.arange(1, 11)
axs[3].plot(xs, [geometric(x, 0.5) for x in xs], label='$p=0.5$')
axs[3].plot(xs, [geometric(x, 0.2) for x in xs], label='$p=0.2$')
axs[3].plot(xs, [geometric(x, 0.8) for x in xs], label='$p=0.8$')
axs[3].set_title('Geometric')
axs[3].legend(framealpha=0.5)
axs[3].set_ylim(0, 1)

# normal
normal = lambda x, mu, sigma: 1 / np.sqrt(2 * np.pi * sigma ** 2) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
x = np.linspace(-5, 5, 300)
axs[4].plot(x, [normal(x, 0, 1) for x in x], label='$\mu=0, \sigma=1$')
axs[4].plot(x, [normal(x, 0, 0.5) for x in x], label='$\mu=0, \sigma=0.5$')
axs[4].plot(x, [normal(x, 0, 2) for x in x], label='$\mu=0, \sigma=2$')
axs[4].plot(x, [normal(x, 1, 1) for x in x], label='$\mu=1, \sigma=1$')
axs[4].plot(x, [normal(x, -1, 1) for x in x], label='$\mu=-1, \sigma=1$')
axs[4].set_title('Normal')
axs[4].legend(framealpha=0.5)
axs[4].set_ylim(0)

# gamma
gamma = lambda x, alpha, beta: beta ** alpha / scipy.special.gamma(alpha) * x ** (alpha - 1) * np.exp(-beta * x)
x = np.linspace(0.001, 5, 300)
axs[5].plot(x, [gamma(x, 1, 1) for x in x], label=r'$\alpha=1, \beta=1$')
axs[5].plot(x, [gamma(x, 1, 2) for x in x], label=r'$\alpha=1, \beta=2$')
axs[5].plot(x, [gamma(x, 2, 1) for x in x], label=r'$\alpha=2, \beta=1$')
axs[5].plot(x, [gamma(x, 2, 2) for x in x], label=r'$\alpha=2, \beta=2$')
axs[5].set_title('Gamma')
axs[5].legend(framealpha=0.5)
axs[5].set_ylim(0)

plt.tight_layout()
plt.show()

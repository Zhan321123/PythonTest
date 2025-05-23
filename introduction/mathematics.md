<h1 style='text-align: center;'>Mathematics</h1>

<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M12 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h8zM4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4z"/><path d="M4 2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5v-2zm0 4a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-4z"/></svg>
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M5.68 5.792 7.345 7.75 5.681 9.708a2.75 2.75 0 1 1 0-3.916ZM8 6.978 6.416 5.113l-.014-.015a3.75 3.75 0 1 0 0 5.304l.014-.015L8 8.522l1.584 1.865.014.015a3.75 3.75 0 1 0 0-5.304l-.014.015L8 6.978Zm.656.772 1.663-1.958a2.75 2.75 0 1 1 0 3.916L8.656 7.75Z"/></svg>

## 平均数比较

均方根平均数 >= 算数平均数 >= 几何平均数 >= 调和平均数，
$$
\sqrt{\frac{x^2+y^2}{2}} \ge \frac{x+y}{2} \ge \sqrt{xy} \ge \frac{2}{\frac{1}{x}+\frac{1}{y}}
$$
都由证明，可拓展为
$$
\sqrt{\sum_{i=1}^n\frac{x_i^2}{n}} \ge \frac{\sum^n_{i=1}x_i}{n} \ge \sqrt[n]{\prod _{i=1}^{n}x_i } \ge \frac{n}{\sum^n_{i=1}\frac{1}{x_i}}
$$

## 数列

### 等差数列

$$
A_{n+1} = A_n + r = A_1 + rn
$$
$$
S_n = n \frac{A_1+A_n}{2} = n\frac{2A_1+nr-r}{2}
$$

### 等比数列

$$
A_{n+1} = A_n d = A_1 d^n
$$
$$
S_n = A_1 \frac{1-d^n}{1-d}
$$

### 斐波那契数列 (兔子繁殖数列)

$$
A_n = A_{n-1} + A_{n-2} = (((1 + \sqrt(5)) / 2)^n - ((1 - \sqrt(5)) / 2)^n) / \sqrt(5)
$$
$$
S_n = 2 * A_n + A_{n-1} - 1
$$

### 幂数列

$$
A_n = A_{n-1} a = A_1 n^a
$$
$$
S_n = 
$$

### 调和数列

$$
A_n=\frac{1}{n}
$$
$$
S_n=\ln n+C
$$
该式当n很大时成立，式中，$C=0.57722...$，称作欧拉常数，专为调和级数所用，至今未证明是有理数还是无理数
$$
\lim_{x \to \infty} S_n = \infty
$$

## 曲线

### n阶贝塞尔曲线

$$
B(t) = \sum_{i=0}^n C_n^i (1-t)^{n-i} t^i P_i
$$
其中
$C_n^i = \frac{n!}{i! (n-i)!}$
P为点集，t范围为$[0,1]$，该式适用于任何维度。

### 一般曲线

- 直线 $y = kx$
- 圆 $x^2 + y^2 = r^2$
- 抛物线 $y = ax^2 + bx + c$
- 反比例函数 $y = \frac{a}{x}$
- 椭圆 $x^2 + \frac{y^2}{a^2} = 1$
- 拱形 $a \cosh\frac{x}{a}$
- 双曲线
- 爱心 $x^2 + y^2 - 1)^3 - x^2 y^3$
- 三叶草 $(x^2 + y^2)^2 + ax^3 - 3axy^2$
- 山谷 $y = frac{1}{x^2 + 1}$

## 曲面

- 球体
- 椭球体
- 圆环体 
- 圆锥
- 圆柱体
- 双曲面
- 抛物面

## 概率分布函数

### 正态分布

### 伽马分布

### $t$ 分布

### $X^2$ 分布

### 泊松分布

### 二项式分布

## 回归模型

### 一元线性回归

- 线性回归模型 $y = \beta_0 + \beta_1 x + \epsilon$
- 回归方程 $\hat y = b_0 + b_1 x$
  - $\bar x = \frac{\sum x_i}{n}$
  - $\bar y = \frac{\sum y_i}{n}$
  - $b_1 = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2}$
  - $b_0 = \bar y - b_1 \bar x$
- 相关系数 $r = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sqrt{\sum (x_i - \bar x)^2 \sum (y_i - \bar y)^2}}$
- 决定系数 $r^2$

### 多元线性回归

### 一元非线性回归

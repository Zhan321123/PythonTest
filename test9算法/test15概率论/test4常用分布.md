<h1 style="text-align:center;">Distribution</h1>

## Concept

- 互不相容（互斥）
  $P(AB)=0$
- 相互独立
  $P(AB)=P(A)\cdot P(B)$

- f(x) 概率密度函数
  $\int^{+\infty}_{-\infty}f(x)=1 $
- F(x) 累积分布函数
  $F(x)=\int^{x}_{-\infty}f(x)dx$,
  $ F(+\infty)=1,F(-\infty)=0 $
- EX 均值
  $ EX = \int^{+\infty}_{-\infty}xf(x)dx $
- DX 方差
  $$
  \begin{align*}
    DX&=E(X-EX)^2 \\
    &=E(X^2-2XEX+E^2X) \\
    &=EX^2-2EXEX+E^2X \\
    &=EX^2-E^2X
  \end{align*}
  $$
- 标准差 $\sqrt{DX}$
- cov 协方差 🚀
  $$
  \begin{align*}
    cov(X,Y)&=E(X-EX)(Y-EY) \\
    &=E(XY-YEX-XEY+EXEY) \\
    &=EXY-EXEY-EXEY+EXEY \\
    &=EXY-EXEY
  \end{align*}
  $$
- 相关系数 🚀
  $\rho=\frac{cov(X,Y)}{\sqrt{DX\cdot DY}}$

## Transform
- X
  - $E(nX)=nEX$
  - $E(X+n)=n+EX$
  - $D(nX)=n^2DX$
  - $D(X+n)=DX$
  - $E(X^2)=DX+E^2X$ 🚀
- X、Y独立
  - $cov(X,Y)=0 $
  - $E(XY)=EXEY$
  - $E(X+Y)=EX+EY$
  - $D(X+Y)$
    $$
    \begin{align*}
      D(X+Y)&=E(X+Y)^2-E^2(X+Y) \\
      &=E(X^2+Y^2+2XY)-(EX+EY)^2 \\
      &=EX^2+EY^2+2EXEY-(E^2X+E^2Y+2EXEY) \\
      &=E^2X+DX+E^2Y+DY+2EXEY-(E^2X+E^2Y+2EXEY) \\
      &=DX+DY
    \end{align*}
    $$
  - $D(XY)=(DX+E^2X)(DY+E^2Y)-E^2XE^2Y$
- X、Y不独立
  - $D(X+Y)=DX+DY+2cov(X,Y)$ 🚀
  - $cov(aX,Y)=a\cdot cov(X,Y)$


## Common Distribution

- **Standard Uniform** $X \sim U(0, 1)$
  $$ x\in(0,1) $$
  $$ f(x)=1 $$
  $$ F(x)=x $$
  $$ EX=\frac{1}{2} , DX=\frac{1}{12} $$
- **Uniform** $X \sim U(a, b)$
  $$ x\in(a,b) $$
  $$ f(x)=\frac{1}{b-a} $$
  $$ F(x)=\frac{1}{(b-a)^2}x+\frac{a}{(b-a)^2} $$
  $$ EX=\frac{a+b}{2}, DX=\frac{(b-a)^2}{12} $$
- **01分布/两点分布**
  $$ X=[0,1] $$
  $$ P\{X=0\}=1-p, P\{X=1\}=p $$
  $$ EX=p, DX=p-p^2 $$
- **Poisson Distribution** $X\sim P(\lambda)/E(\frac{1}{\theta})$
  $$ X\in N_0 $$
  $$ P\{X=k\}=\frac{\lambda^k}{k!}e^{-\lambda} $$
  $$ EX=\lambda, DX=\lambda $$
- **指数分布** $X\sim E(\lambda)/E(\frac{1}{\theta})$
  $$ x\in(0,+\infty) $$
  $$ f(x)=\lambda e^{-\lambda x}=\frac{1}{\theta}e^{-\frac{1}{\theta}x} $$
  $$ F(x)=1-e^{-\lambda x}=1-e^{-\frac{1}{\theta}x} $$
  $$ EX=\frac{1}{\lambda}=\theta, DX=\frac{1}{\lambda^2}=\theta^2 $$
- **Binomial Distribution** $X\sim B(n,p)$
  $$ X\in N_0 $$
  $$ P\{X=k\}=C^k_n p^k(1-p)^{n-k} $$
  $$ EX=np, DX=np(1-p) $$
- **Geometric distribution** $X\sim GE(p)$
  $$ X\in N^+ $$
  $$ P\{X=k\}=(1-p)^{k-1}p $$
  $$ EX=\frac{1}{p},DX=\frac{1-p}{p^2} $$
- **Normal** $X\sim N(\mu, \sigma^2)$
  $$X\in R$$
  $$f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp(-\frac{(x-\mu)^2}{2\sigma^2})$$
  $$EX=\mu,DX=\sigma^2$$
- **Standard Normal** $X\sim N(0,1)$
  $$ X\in R $$
  $$ f(x)=\frac{1}{\sqrt{2\pi}}\exp (-\frac{x^2}{2}) $$

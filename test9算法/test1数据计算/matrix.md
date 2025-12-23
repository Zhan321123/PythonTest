<h1 style="text-align:center">Matrix</h1>

## Abstract

- 矩阵 Matrix
  $\begin{bmatrix}
    3&1 \\
    4&2
  \end{bmatrix},
  \begin{pmatrix}
    3&1 \\
    4&2
  \end{pmatrix}$
- 行列式 Determinant
  $\begin{vmatrix}
    2&1 \\
    3&4
  \end{vmatrix}$
- 向量 vector
  $[1,2,...],[1,2,...]^T$

## Type

- **单位矩阵 E**

  $\begin{bmatrix}
    1&& \\
    &1& \\
    &&...
  \end{bmatrix}$
  - EAE=A
- **零矩阵 O**

  $\begin{bmatrix}
    0&0& \\
    0&0&... \\
    &\vdots&
  \end{bmatrix}$
- **对角矩阵 $diag(\lambda_1,\lambda_2,...)$**

  $\begin{bmatrix}
    \lambda_1&& \\
    &\lambda_2& \\
    &&...
  \end{bmatrix}$
- **数量矩阵 A=k diag()**

## Properties

- **对称**
- **反对称**
- **可交换**
- **正交矩阵**
- **相似**
  
  n阶矩阵A、B相似的判定方法：
  - 若存在可逆矩阵P，使得$P^{-1}AP=B$
  - A、B的特征值完全相同，包括重数，且均可对角化（充要条件）
  - A、B的秩、迹相等（必要条件）

  性质：
  - 反身性 $A\sim A$
  - 对称性 $\because A\sim B,\therefore B\sim A$
  - 传递性 $\because A\sim B,A\sim C,\therefore B\sim C$
  - $A\sim B,\exists A^{-1},\exists B^{-1},\therefore A^{-1}\sim B^{-1}$
  - 如果$A\sim B$，则有
    - rank(A)=rank(B)
    - |A|=|B|
- **相加 A+B**
- **数乘矩阵 kA**
  - $|kA|=k^{n}|A|$
- **行列式的值 |A|**
- **矩阵相乘 AB**
- **余子式**
- **转置矩阵 $A^T$**
- **伴随矩阵 $A^*$**
- **上三角行列式**
- **下三角行列式**
- **逆 $A^{-1}$**

  求法：
  - $A^{-1}=\frac{A^*}{|A|}$
  - $(A|E)\to (E|A^{-1})$

  如果A可逆，则有：
  - $A^{-1}A=E$
  - $|A|\ne 0$
  - $r(A)=n_A$
- **秩 rank(A) r(A)**
- **范数**
- **特征值 $\lambda$**

  $Ax=\lambda x$，x为n维非零向量，$|\lambda E-A|=0$，解得λ

- **特征向量**
- **迹 tr(A)**

  矩阵的迹=矩阵主对角线元素之和
- **旋转**
  - rotato 90
  - rotato 180
  - rotato 270
- **镜像**
  - vertical
  - horizontal

## Artificial Intelligence

- **卷积**
- **扩边**
- **池化**
  - 最大
  - 平均
- **转置卷积**

## Application

- **多元线性方程组求解 Ax=y**

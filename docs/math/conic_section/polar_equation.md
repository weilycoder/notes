## 椭圆

以 $F_1$ 为极点，$x$ 轴为极轴，建立极坐标系，考虑椭圆上一点 $P\left(\rho,\theta\right)$ 满足的条件．

在原直角坐标系下考虑，作准线 $l_1:x=-\dfrac{a^2}{c}$．过 $P$ 作 $PG$ 垂直于 $x$ 轴，垂足为 $G$；作 $PH$ 垂直于 $l_1$，垂足为 $H$．过 $F_1$ 作 $F_1E$ 垂直于 $l_1$，垂足为 $E$．

根据[焦半径公式（第二定义）](./second_definition.md)推得的结论，有

$$
\begin{aligned}
    \left\vert GF_1\right\vert
    &= \left\vert GE\right\vert - \left\vert F_1E\right\vert \\
    &= \left\vert PH\right\vert - \left\vert F_1E\right\vert \\
    &= \dfrac{\rho}{e} - p. \\
\end{aligned}
$$

因此

$$
\begin{aligned}
    \cos\theta 
    &= \dfrac{\left\vert GF_1\right\vert}{\left\vert PF_1\right\vert} \\
    &= \dfrac{\dfrac{\rho}{e} - p}{\rho}.
\end{aligned}
$$

整理得

$$
\tag{5} \rho = \dfrac{ep}{1 - e\cos\theta} = \dfrac{b^2}{a - c\cos\theta}.
$$

若取 $F_2$ 作为极点，考虑椭圆的对称性，有

$$
\tag{6} \rho^{\prime} = \dfrac{ep}{1 + e\cos\theta} = \dfrac{b^2}{a + c\cos\theta}.
$$

另外，如果求焦点弦长度，立刻得到

$$
\tag{7} d = \rho+\rho^{\prime}=\dfrac{2ep}{1 - e^2\cos^2\theta}.
$$

## 双曲线

先说明结论，双曲线中，极坐标方程形式与椭圆的形式完全一致，但极点选取了 $F_2$：

$$
\rho = \dfrac{ep}{1 - e\cos\theta} = \dfrac{b^2}{a - c\cos\theta}.
$$

如果沿用椭圆的几何法证明，则具体推导过程由于双曲线两支曲线和方程中经常出现的绝对值符号而需要一些分类讨论，因此这里暂不讨论．

此外，需要注意公式中 $\rho$ 可以取负数，这时应理解为反向进行延长，即 $\left(-\rho,\theta\right)=\left(\rho,\theta+\pi\right)$．

$\rho$ 取负数时 $P$ 点在左支上；$\rho$ 取正数时 $P$ 点在右支上．

*[信息不足]* 似乎也可以移轴后将 $\left(r\cos\theta,r\sin\theta\right)$ 代入双曲线方程．

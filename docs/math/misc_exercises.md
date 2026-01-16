## 数列

### Problem 1

???+ note "Problem"

    有正项数列 $\left\{a_n\right\}$，$S_n$ 是其前 $n$ 项和，满足

    $$
    S_n=\dfrac{1}{2}\left(a_n+\dfrac{1}{a_n}\right),
    $$

    求数列通项．

#### 方法 1

注意到

$$
a_n=\sqrt{n}-\sqrt{n-1},
$$

数学归纳易证．

#### 方法 2

由 $S_n,a_n$ 关系，

$$
S_{n+1}=\dfrac{1}{2}\left(S_{n+1}-S_{n}+\dfrac{1}{S_{n+1}-S_{n}}\right);
$$

整理得

$$
S_{n+1}^2-S_{n}^2=1;
$$

又

$$
S_1=a_1=\dfrac{1}{2}\left(a_1+\dfrac{1}{a_1}\right);
$$

解得 $S_1=a_1=1$，则 $S_1^2=1$．

因此，

$$
S_n^2=n;
$$

由于数列各项为正，

$$
S_n=\sqrt{n};
$$

所以（$n\geqslant 2$ 时）

$$
a_{n}=\sqrt{n}-\sqrt{n-1}.
$$

检验发现 $n=1$ 时式子仍成立．

## 高等数学

### Problem 1

其实是物理题。

> 空间中一小球质量为 $m$，电荷量为 $q(q\gt 0)$，受重力影响下落，重力加速度为 $g$。
>
> 空间中还有磁场方向沿水平方向（垂直纸面向里）的匀强磁场，磁感应强度为 $B$，求小球运动方式。

不熟悉物理的求导符号，使用数学符号代替。

首先建立右手直角坐标系，令 $y$ 轴正方向沿重力方向，$z$ 轴正方向沿磁场方向。

则有

$$
\left\{
\begin{aligned}
    a_x = \dfrac{\mathrm{d}}{\mathrm{d}t}v_{x} &= \dfrac{qv_{y}B}{m}, \\
    a_y = \dfrac{\mathrm{d}}{\mathrm{d}t}v_{y} &= g - \dfrac{qv_{x}B}{m};
\end{aligned}
\right.
$$

对第二个式子求导，将 $g$ 消去，

$$
\dfrac{\mathrm{d}^2}{\mathrm{d}t^2}v_{y} = -\dfrac{qB}{m}\cdot\dfrac{\mathrm{d}}{\mathrm{d}t}v_{x} = -\dfrac{q^2B^2}{m^2}v_{y}.
$$

熟知

$$
\dfrac{\mathrm{d}^2}{\mathrm{d}x^2}y=Ay
$$

时，有

$$
y = C_{1}e^{\sqrt{A}x} + C_{2}e^{-\sqrt{A}x}.
$$

因此

$$
v_y = v_{1}e^{\frac{iqBt}{m}} + v_{2}e^{\frac{-iqBt}{m}},
$$

这里 $i$ 是虚数单位。

由于 $t=0$ 时 $v_y=0$，因此 $v_1=v_2$，进一步，由欧拉公式，可以将 $v_y$ 表示为

$$
v_y = v_0\sin\left(\dfrac{qBt}{m}\right).
$$

代入 $a_y$ 的表达式，得

$$
\begin{aligned}
    \dfrac{\mathrm{d}}{\mathrm{d}t}\left(v_0\sin\left(\dfrac{qBt}{m}\right)\right) &= g - \dfrac{qv_{x}B}{m}, \\
    \dfrac{qBv_0}{m}\cdot\cos\left(\dfrac{qBt}{m}\right) &= g - \dfrac{qv_{x}B}{m}, \\
    \dfrac{qv_{x}B}{m} &= g - \dfrac{qBv_0}{m}\cdot\cos\left(\dfrac{qBt}{m}\right), \\
    v_{x} &= \dfrac{mg}{qB} - v_0\cdot\cos\left(\dfrac{qBt}{m}\right).
\end{aligned}
$$

又 $t=0$ 时 $v_x=0$，因此 $v_0=\dfrac{mg}{qB}$，总之，

$$
\left\{
\begin{aligned}
    v_{x} &= \dfrac{mg}{qB}\left(1-\cos\left(\dfrac{qBt}{m}\right)\right), \\
    v_y &= \dfrac{mg}{qB}\sin\left(\dfrac{qBt}{m}\right).
\end{aligned}
\right.
$$

取小球初始位置为原点，积分得

$$
\left\{
\begin{aligned}
    x &= \dfrac{mgt}{qB} - \dfrac{m^2g}{q^2B^2}\sin\left(\dfrac{qBt}{m}\right), \\
    y &= \dfrac{m^2g}{q^2B^2}\left(1-\cos\dfrac{qBt}{m}\right).
\end{aligned}
\right.
$$

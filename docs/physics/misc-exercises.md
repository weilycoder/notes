## 积分练习

### Problem 1

> 空间中一小球质量为 $m$，电荷量为 $q(q\gt 0)$，受重力影响下落，重力加速度为 $g$．
>
> 空间中还有磁场方向沿水平方向（垂直纸面向里）的匀强磁场，磁感应强度为 $B$，求小球运动方式．

!!! note "高中常规做法"

    将速度进行矢量分解，分出一个速度提供与重力等大反向的洛伦兹力，则另一个速度符合匀速圆周运动规律．

!!! note "积分做法"

    不熟悉物理的求导符号，使用数学符号代替．

    首先建立右手直角坐标系，令 $y$ 轴正方向沿重力方向，$z$ 轴正方向沿磁场方向．

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

    这里 $i$ 是虚数单位．

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

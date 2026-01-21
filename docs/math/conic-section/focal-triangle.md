在椭圆或双曲线中，由焦点 $F_1,F_2$ 和曲线上一点 $P$ 作为顶点构成的三角形，叫做**焦点三角形**，并记 $\theta=\angle F_1PF_2$，$I$ 为三角形内心，$r=\left\vert y_{I}\right\vert$ 为三角形内接圆半径．

## 周长

在椭圆中，明显有

$$
\tag{26} C_{\triangle F_1F_2P} = 2a + 2c.
$$

## 面积

椭圆中有常用的几种表示方法：

$$
\tag{27} S_{\triangle F_1F_2P} = c\left\vert y_{P}\right\vert = b^2\tan\dfrac{\theta}{2} = \left(a+c\right)r = \left(a+c\right)\left\vert y_{I}\right\vert;
$$

双曲线中由于周长不定，没有后两种形式：

$$
\tag{28} S_{\triangle F_1F_2P} = c\left\vert y_{P}\right\vert = b^2\cot\dfrac{\theta}{2}.
$$

## 内心和旁心运动轨迹

<figure markdown="span">
    ![ellipse-focal-triangle](./image/ellipse-focal-triangle-incentre.png)
    <figcaption><i>椭圆中的焦点三角形以及内心和旁心</i></figcaption>
</figure>

<figure markdown="span">
    ![hyperbola-focal-triangle](./image/hyperbola-focal-triangle-incentre.png)
    <figcaption><i>双曲线中的焦点三角形以及内心和旁心</i></figcaption>
</figure>

结论是，对于椭圆，内心和 $F_1F_2$ 对应的旁心的轨迹是椭圆；其余两个旁心的轨迹是直线．

对于双曲线（假设 $P$ 只在一支上运动），内心和 $F_1F_2$ 对应的旁心轨迹是直线的一部分；其余两个旁心的轨迹是两个离心率不等的双曲线的一支．

同时可以从图中看到，上述轨迹中的直线均与曲线的左顶点或右顶点相切．

这些结论可以使用三角形的内心坐标公式验证．

---

下面以椭圆内心为例展示推导过程．

设椭圆方程为 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a\gt b\gt 0\right)$，则 $F_1\left(-c,0\right),F_2\left(c,0\right),P\left(x_0,y_0\right)$，并且记 $d_1=\left\vert PF_1\right\vert,d_2=\left\vert PF_2\right\vert$．

根据内心坐标公式，有

$$
\begin{aligned}
    x_I &= \dfrac{-cd_2+cd_1+2cx_0}{d_1+d_2+2c}, \\
    y_I &= \dfrac{2cy_0}{d_1+d_2+2c}.
\end{aligned}
$$

其中 $d_1+d_2$ 根据椭圆定义为 $2a$，又

$$
\begin{aligned}
    \left(d_1-d_2\right)\left(d_1+d_2\right)
    &= d_1^2-d_2^2 \\
    &= \left(x_0+c\right)^2-\left(x_0-c\right)^2 \\
    &= 4cx_0,
\end{aligned}
$$

因此 $d_1-d_2=\dfrac{2cx_0}{a}$，代入内心坐标，有

$$
\begin{aligned}
    x_I &= \dfrac{-cd_2+cd_1+2cx_0}{d_1+d_2+2c} \\
    &= \dfrac{\frac{2c^2x_0}{a}+2cx_0}{2\left(a+c\right)} \\
    &= \dfrac{2c^2x_0+2acx_0}{2a\left(a+c\right)} \\
    &= \dfrac{2cx_0\left(c+a\right)}{2a\left(a+c\right)} \\
    &= \dfrac{cx_0}{a}, \\
    y_I &= \dfrac{2cy_0}{d_1+d_2+2c} \\
    &= \dfrac{2cy_0}{2a+2c} \\
    &= \dfrac{cy_0}{a+c}. \\
\end{aligned}
$$

即 $I\left(\dfrac{cx_0}{a},\dfrac{cy_0}{a+c}\right)$，故其轨迹方程为 $\dfrac{x^2}{c^2}+\dfrac{y^2}{\left(\dfrac{bc}{a+c}\right)^2}=1$．

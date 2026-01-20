## 椭圆

<figure markdown="span">
    ![x^2/3+y^2=1](./image/ellipse_0.png)
    <figcaption>\(\small x^2/3+y^2=1\)</figcaption>
</figure>

平面内与两个定点 $F_1,F_2$ 距离之和等于常数 $2a\left(2a\gt\left\vert F_1 F_2 \right\vert\right)$ 的点的轨迹称为**椭圆**．

即，椭圆上一点 $P$ 满足

$$
\left\vert PF_1\right\vert + \left\vert PF_2\right\vert = 2a.
$$

其中 $F_1,F_2$ 为椭圆的**焦点**，$2c=\left\vert F_1 F_2\right\vert$ 为椭圆的**焦距**．并且可以证明，$2a$ 为椭圆的长轴．

!!! question "为什么要有系数 2？"

    这是为了简化标准方程的形式．

---

以过椭圆两焦点 $F_1 F_2$ 的直线为 $x$ 轴，线段 $F_1 F_2$ 的垂直平分线为 $y$ 轴，建立平面直角坐标系．

设椭圆上任意一点为 $P\left(x,y\right)$，$F_1\left(-c,0\right)$ 为椭圆的左焦点，$F_2\left(c,0\right)$ 为椭圆的右焦点，根据椭圆定义，有

$$
\tag{1} \sqrt{\left(x+c\right)^2+y^2} + \sqrt{\left(x-c\right)^2+y^2} = 2a.
$$

课本上的化简方法是两次移项后平方，这里给出一个更巧妙的做法．

由于

$$
\tag{2} \left[\left(x+c\right)^2+y^2\right]-\left[\left(x-c\right)^2+y^2\right]=4cx,
$$

有

$$
\tag{3} \sqrt{\left(x+c\right)^2+y^2} - \sqrt{\left(x-c\right)^2+y^2} = \dfrac{4cx}{2a} = \dfrac{2cx}{a}.
$$

$\mathrm{(1)}+\mathrm{(3)}$ 得

$$
\begin{align*}
    \tag{4} \sqrt{\left(x+c\right)^2+y^2} &= a+\dfrac{cx}{a}, \\
    x^2+2cx+c^2+y^2 &= a^2+2cx+\dfrac{c^2x^2}{a^2}, \\
    \tag{5} \dfrac{\left(a^2-c^2\right)x^2}{a^2}+y^2 &= a^2-c^2.
\end{align*}
$$

令 $b^2=a^2-c^2$ 并代入 $\mathrm{(5)}$ 式，得

$$
\begin{align*}
    \dfrac{b^2x^2}{a^2}+y^2 &= b^2, \\
    \tag{6} \dfrac{x^2}{a^2}+\dfrac{y^2}{b^2} &= 1.
\end{align*}
$$

请注意 $a\gt b\gt 0$．

---

!!! note

    当长轴在 $y$ 轴上时，椭圆的方程变为

    $$
    \tag{7} \dfrac{y^2}{a^2}+\dfrac{x^2}{b^2} = 1.
    $$

---

这时，容易得到（长轴在 $x$ 轴上的）椭圆的一些几何性质：

+ 椭圆上任意一点 $\left(x,y\right)$ 满足 $x\in\left[-a,a\right]$，$y\in\left[-b,b\right]$；
+ $A_1\left(-a,0\right),A_2\left(a,0\right)$ 分别为椭圆的左顶点和右顶点；
+ $B_1\left(0,-b\right),B_2\left(0,b\right)$ 分别为椭圆的上顶点和下顶点；
+ $A_1A_2$ 和 $B_1B_2$ 分别被称作椭圆的长轴和短轴，它们的长分别为 $2a$ 和 $2b$；
+ $x$ 轴和 $y$ 轴是椭圆的对称轴；
+ 原点是椭圆的对称中心．

---

如果固定半长轴 $a$，改变半焦距 $c(0\lt c\lt a)$ 的长度，可以发现，$c$ 越接近 $a$，椭圆越“扁平”；$c$ 越接近 $0$，椭圆越接近正圆．当然，如果同时将 $a,c$ 放大或缩小相同倍数，作出的椭圆是相似图形．

因此，可以使用比值 $\dfrac{c}{a}$ 衡量椭圆的“扁平程度”，并记 $e=\dfrac{c}{a}$ 为椭圆的**离心率**．

对于椭圆，$e\in\left(0,1\right)$（一般不认为圆是椭圆）．

!!! question "为什么使用 $c/a$ 而非 $b/a$ 或其他比值？"

    这与圆锥曲线的统一定义（第二定义）有关，后文将提到．

## 双曲线

<figure markdown="span">
    ![x^2-y^2/3=1](./image/hyperbola_0.png)
    <figcaption>\(\small x^2-y^2/3=1\)</figcaption>
</figure>

平面内与两个定点 $F_1,F_2$ 的距离之差的绝对值等于常数 $2a(0\lt 2a\lt \left\vert F_1 F_2\right\vert)$ 的点的轨迹称为**双曲线**．

即，双曲线上一点 $P$ 满足

$$
\left\vert\left\vert PF_1\right\vert-\left\vert PF_2\right\vert\right\vert = 2a.
$$

其中 $F_1,F_2$ 为双曲线的**焦点**，$2c=\left\vert F_1 F_2\right\vert$ 为双曲线的**焦距**．

---

使用与椭圆类似的建系方法，令左焦点为 $F_1\left(-c,0\right)$，右焦点为 $F_2\left(c,0\right)$，$P\left(x,y\right)$ 为椭圆上任意一点，根据双曲线的定义，有

$$
\tag{8} \sqrt{\left(x+c\right)^2+y^2} - \sqrt{\left(x-c\right)^2+y^2} = \pm 2a.
$$

类似椭圆的推导过程，有

$$
\tag{9} \sqrt{\left(x+c\right)^2+y^2} + \sqrt{\left(x-c\right)^2+y^2} = \pm\dfrac{2cx}{a}.
$$

两式相加

$$
\sqrt{\left(x+c\right)^2+y^2} = \pm\left(a+\dfrac{cx}{a}\right),
$$

即

$$
\tag{10} \sqrt{\left(x+c\right)^2+y^2} = \left\vert a+\dfrac{cx}{a}\right\vert.
$$

两侧平方，得

$$
\begin{align*}
    x^2+2cx+c^2+y^2 &= a^2+2cx+\dfrac{c^2x^2}{a^2}, \\
    \tag{11} \dfrac{\left(c^2-a^2\right)x^2}{a^2}-y^2 &= c^2-a^2. \\
\end{align*}
$$

令 $b^2=c^2-a^2$ 并代入 $\mathrm{(11)}$，得

$$
\begin{align*}
    \dfrac{b^2x^2}{a^2}-y^2 &= b^2, \\
    \tag{12} \dfrac{x^2}{a^2}-\dfrac{y^2}{b^2} &= 1.
\end{align*}
$$

与椭圆不同，这里 $a,b$ 没有大小关系，但仍注明 $a\gt 0,b\gt 0$．

!!! note

    假如将 $\mathrm{(5)}$ 式与 $\mathrm{(11)}$ 对比，可以发现它们实际上是相同的，但是 $a,c$ 的大小关系改变了．

!!! note

    当实轴在 $y$ 轴上时，椭圆的方程变为

    $$
    \tag{13} \dfrac{y^2}{a^2}-\dfrac{x^2}{b^2} = 1.
    $$

---

这时，容易得到（实轴在 $x$ 轴上的）双曲线的一些几何性质：

+ 双曲线上任意一点 $\left(x,y\right)$ 满足 $x\in\left(-\infty,-a\right]\cup\left[a,+\infty\right)$，$y\in\mathbb{R}$；
+ $A_1\left(-a,0\right),A_2\left(a,0\right)$ 分别为双曲线的左顶点和右顶点；
+ 与椭圆不同，双曲线没有上顶点或下顶点，但仍然记 $B_1\left(0,-b\right),B_2\left(0,b\right)$；
+ $A_1A_2$ 和 $B_1B_2$ 分别被称作双曲线的实轴和虚轴，它们的长分别为 $2a$ 和 $2b$；
+ $x$ 轴和 $y$ 轴是双曲线的对称轴；
+ 原点是双曲线的对称中心；
+ $\dfrac{x}{a}\pm\dfrac{y}{b} = 0$ 是双曲线的两条渐近线．

!!! note

    渐近线在某些时候可以看作退化的双曲线，这是因为其方程

    $$
    \tag{14} \dfrac{x^2}{a^2}-\dfrac{y^2}{b^2} = 0
    $$

    可以使用与双曲线类似的方法处理．

仍然记 $e=\dfrac{c}{a}$ 为双曲线的**离心率**，这里 $e\in\left(1,+\infty\right)$，刻画双曲线的张口大小，离心率越大，张口越大．

---

若双曲线的离心率为 $\sqrt{2}$，则其实轴与虚轴等长，称这种双曲线为**等轴双曲线**．

假设两双曲线的实轴与虚轴是对换的，称这它们为**共轭双曲线**．

共轭双曲线的渐近线相同；$4$ 个焦点共圆；离心率的平方倒数和为 $1$．

## 椭圆

### 焦半径公式

[标准方程（第一定义）](./first_definition.md)中 $\mathrm{(4)}$ 式指出，

$$
\left\vert PF_1\right\vert=\sqrt{\left(x+c\right)^2+y^2} = a+\dfrac{cx}{a}.
$$

同理可得 $\left\vert PF_2\right\vert$ 的表达式，即

$$
\tag{1} \begin{cases}
    \left\vert PF_1\right\vert=\sqrt{\left(x+c\right)^2+y^2} = a+\dfrac{cx}{a}=a+ex; \\
    \left\vert PF_2\right\vert=\sqrt{\left(x-c\right)^2+y^2} = a-\dfrac{cx}{a}=a-ex.
\end{cases}
$$

$\mathrm{(1)}$ 式即为椭圆的**焦半径公式**．

### 第二定义

以 $\left\vert PF_1\right\vert=a+ex$ 为例，可以注意到这是一个仅与 $x$ 有关的函数，我们考虑在等式两侧同时除以 $e$，把等式右侧做成点到直线距离的形式，即

$$
\begin{align*}
    \left\vert PF_1\right\vert &= a+ex, \\
    \dfrac{\left\vert PF_1\right\vert}{e} &= \dfrac{a^2}{c}+x, \\
    \tag{2} e &= \dfrac{\left\vert PF_1\right\vert}{x-\left(-\dfrac{a^2}{c}\right)}. \\
\end{align*}
$$

同理有

$$
\tag{3} e = \dfrac{\left\vert PF_2\right\vert}{x-\dfrac{a^2}{c}}.
$$

$\mathrm{(2)},\mathrm{(3)}$ 构成了椭圆的第二定义，即，平面内到定点距离与到定直线距离之比为定值 $e(0\lt e\lt 1)$ 的点的轨迹叫做椭圆．

这个定值 $e$ 叫做椭圆的**离心率**，定点与定直线是椭圆对应的**焦点**和**准线**．

左焦点对应的准线叫做左准线，右焦点对应的准线叫做右准线．

焦点到对应准线的距离叫做**焦准距**，一般记作 $p$，在椭圆中，准线在焦点外侧，因此

$$
\tag{4} p = \dfrac{a^2}{c}-c = \dfrac{b^2}{c}.
$$

## 双曲线

### 焦半径公式

根据[标准方程（第一定义）](./first_definition.md)中 $\mathrm{(10)}$ 式，与椭圆类似，可得

$$
\tag{8} \begin{cases}
    \left\vert PF_1\right\vert=\sqrt{\left(x+c\right)^2+y^2} = \left\vert a+\dfrac{cx}{a}\right\vert=\left\vert a+ex\right\vert; \\
    \left\vert PF_2\right\vert=\sqrt{\left(x-c\right)^2+y^2} = \left\vert a-\dfrac{cx}{a}\right\vert=\left\vert a-ex\right\vert.
\end{cases}
$$

### 第二定义

与椭圆类似，故不重复推导过程．

$$
\tag{9}\begin{cases}
    \dfrac{\left\vert PF_1\right\vert}{\left\vert x+\dfrac{a^2}{c}\right\vert} &= e,\\
    \dfrac{\left\vert PF_2\right\vert}{\left\vert x-\dfrac{a^2}{c}\right\vert} &= e.
\end{cases}
$$

因此双曲线的第二定义为，平面内到定点距离与到定直线距离之比为定值 $e(e\gt 1)$ 的点的轨迹叫做双曲线．

这个定值 $e$ 叫做椭圆的**离心率**，定点与定直线是双曲线对应的**焦点**和**准线**．

双曲线的准线在焦点内侧．

双曲线中仍然有

$$
p = \dfrac{b^2}{c}.
$$

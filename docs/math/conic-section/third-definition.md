在圆中，熟知垂径定理．

!!! note "垂径定理"

    垂直于弦的直径平分这条弦，且平分弦所对的两条弧．

    常用的两条推论是：

    + 平分弦（不是直径）的直径垂直于弦，且平分弦所对的两条弧．
    + 弦的垂直平分线是直径，且平分弦所对的两条弧．
    + 直径所对的圆周角是直角．

    第三条可以利用三角形中位线的性质证明．

在椭圆和双曲线中，存在类似的结论．

!!! note "广义垂径定理"

    对于标准方程

    $$
    \dfrac{x^2}{a^2}\pm\dfrac{y^2}{b^2}=1
    $$

    描述的圆锥曲线 $\Gamma$ 中，设不经过原点的直线与 $\Gamma$ 交于 $A,B$ 两点，$M$ 为 $AB$ 中点，且 $AB,OM$ 斜率存在，则

    $$
    \tag{1} k_{AB}\cdot k_{OM} = \mp\dfrac{b^2}{a^2} = e^2-1.
    $$

下面证明该定理．

设 $A\left(x_1,y_1\right),B\left(x_2,y_2\right)$ 是 $\Gamma$ 上不同的两点，即

$$
\begin{cases}
    \dfrac{x_1^2}{a^2}\pm\dfrac{y_1^2}{b^2}=1, \\
    \dfrac{x_2^2}{a^2}\pm\dfrac{y_2^2}{b^2}=1.
\end{cases}
$$

两式作差，有

$$
\begin{align*}
    \dfrac{x_1^2-x_2^2}{a^2}\pm\dfrac{y_1^2-y^2}{b^2} &= 0, \\
    \dfrac{x_1^2-x_2^2}{a^2} &= \mp\dfrac{y_1^2-y^2}{b^2}, \\
    \dfrac{\left(x_1-x_2\right)\left(x_1+x_2\right)}{a^2} &= \mp\dfrac{\left(y_1-y_2\right)\left(y_1+y_2\right)}{b^2}, \\
    \dfrac{\left(y_1-y_2\right)}{\left(x_1-x_2\right)}\cdot\dfrac{\left(y_1+y_2\right)}{\left(x_1+x_2\right)} &= \mp\dfrac{b^2}{a^2}, \\
    k_{AB}\cdot k_{OM} &= \mp\dfrac{b^2}{a^2} = e^2-1.
\end{align*}
$$

需要指出，上述推导对双曲线的渐近线方程仍然成立．

这引出的一条推论是，设直线 $\alpha$ 与双曲线交于 $P,Q$ 两点，与两条渐近线交于 $S,T$ 两点，则线段 $PQ,ST$ 共中点，或 $PS=QT$．

应用三角形的中位线性质，广义垂径定理的另一条推论是：设过原点的直线交 $\Gamma$ 于 $A,B$ 两点，$P$ 为 $\Gamma$ 上与 $A,B$ 不同的一点，若 $AP,BP$ 斜率均存在，则

$$
\tag{2} k_{AP}\cdot k_{BP} = e^2-1.
$$

因此，部分人将这一性质作为圆锥曲线的第三定义，即在**平面直角坐标系中**，与两定点斜率之积为定值的点的轨迹是圆锥曲线的**一部分**．

加粗的部分是这一定义的两个缺陷，另两个缺陷是这一定义只能作出对称轴平行于坐标轴的圆锥曲线，以及对于抛物线没有良好描述．

<figure markdown="span">
    ![x^2+xy+y^2=36](./image/ellipse-1.png)
    <figcaption>\(\small x^2+xy+y^2=36\)</figcaption>
</figure>

<figure markdown="span">
    ![x^2-xy-y^2=4](./image/hyperbola-1.png)
    <figcaption>\(\small x^2-xy-y^2=4\)</figcaption>
</figure>

广义垂径定理常被用于转化题中斜率相关定值．

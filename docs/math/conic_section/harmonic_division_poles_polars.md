## 调和点列

若直线上**不同**的 $A,B,C,D$ 四点满足

$$
\tag{1} \dfrac{AC}{CB} = \dfrac{AD}{DB},
$$

则称 $A,B,C,D$ 为**调和点列**，或说 $C,D$ **调和分割**线段 $AB$．

由于 $C,D$ 一点在线段 $AB$ 上，一点在线段 $AB$ 外（否则重合），称在 $AB$ 上的为**内分点**，在 $AB$ 外的为**外分点**．

注意此时亦有

$$
\tag{2} \dfrac{CB}{BD} = \dfrac{CA}{AD},
$$

因此也说 $A,B$ 调和分割线段 $CD$．

## 无穷远点

对于线段 $AB$ 及其中点 $C$，若希望在直线 $AB$ 上选取一点 $C$ 使得 $A,B,C,D$ 构成调和点列，则有

$$
\dfrac{x_{D}-x_{B}}{x_{D}-x_{A}} = 1.
$$

这在普通的欧式几何中是不可能的，但在射影几何中，我们取 $D$ 在这条直线的无穷远处，有

$$
\lim_{x_{D}\to\infty}\dfrac{x_{D}-x_{B}}{x_{D}-x_{A}} = 1.
$$

请注意这里写 $x_{D}\to\infty$，而不在 $\infty$ 前加正号或符号，因为无穷原点不在 $AB$ 的左侧或右侧，它只是在这条线的无穷远处．

在射影几何中，两条平行线交于无穷远处，因此也可以将无穷远点理解为直线的“方向”．

全体无穷远点构成无穷远直线．

## 调和线束

若 $A,B,C,D$ 成调和点列，$O$ 为 $ABCD$ 外一点，则称 $OA,OB,OC,OD$ 为**调和线束**．

任取直线 $l$ 分别交 $OA,OB,OC,OD$ 于 $A^{\prime},B^{\prime},C^{\prime},D^{\prime}$，则 $A^{\prime},B^{\prime},C^{\prime},D^{\prime}$ 也构成调和点列．

一个比较简洁的方法是通过三角形面积公式将 $\mathrm{(1)}$ 转化为

$$
\tag{3} \dfrac{\sin\angle AOC}{\sin\angle COB} = \dfrac{\sin\angle AOD}{\sin\angle DOB},
$$

两个常用推论：

+ 定理在 $A^{\prime},B^{\prime},C^{\prime},D^{\prime}$ 有无穷远点时也成立，此时另外三个点中有一个点时另两个的中点；
+ 若 $OA,OB,OC,OD$ 中有一条射线平分了另外三条射线中其中两条构成的角，则这条平分线与剩下的一条射线构成直角（阿氏圆）．

## 完全四边形

<figure markdown="span">
    ![complete_quadrangle](../../image/complete_quadrangle.png)
    <figcaption>*完全四边形*</figcaption>
</figure>

两两相交且任意三线不共点的四条直线构成完全四边形．

如上图，$ABC,BDE,CDF,AFE$ 四条直线两两交于 $A,B,C,D,E,F$ 六点，故 $ABCDEF$ 构成完全四边形．

完全四边形有三条对角线，如上图，$AD,BF,CE$ 为三条对角线．

完全四边形的任意两条对角线所在直线调和分割另外一条．

下证 $I,H$ 调和分割 $CE$．

在 $\triangle ACE$ 中，由梅涅劳斯定理，

$$
\tag{4} \dfrac{AB}{BC}\cdot\dfrac{CI}{IE}\cdot\dfrac{EF}{FA} = 1;
$$

由塞瓦定理，

$$
\tag{5} \dfrac{AB}{BC}\cdot\dfrac{CH}{HE}\cdot\dfrac{EF}{FA} = 1;
$$

两式对比，得

$$
\tag{6} \dfrac{CI}{IE} = \dfrac{CH}{HE}.
$$

剩余两对调和点列同理得证．

另外，由于调和线束的性质，如果再连一些边，可以形成更多调和点列．

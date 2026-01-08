欧拉第二积分定义为

$$
\begin{aligned}
\Gamma\left(a\right) 
&= \int_{0}^{\infty}x^{a-1}\mathrm{e}^{-x}\mathrm{d}x \\
&= \int_{0}^{\infty}x^{a-1}\mathrm{d}\left(-\mathrm{e}^{-x}\right) \\
&= \left.-x^{a-1}\mathrm{e}^{-x}\right|_{0}^{\infty}+\int_{0}^{\infty}\mathrm{e}^{-x}\mathrm{d}x^{a-1} \\
&= \left[a=1\right] + \int_{0}^{\infty}\mathrm{e}^{-x}\dfrac{\mathrm{d}x^{a-1}}{\mathrm{d}x}\mathrm{d}x \\
&= \left[a=1\right] + \left(a-1\right)\cdot\int_{0}^{\infty}x^{a-2}\mathrm{e}^{-x}\mathrm{d}x \\
&= \left[a=1\right] + \left(a-1\right)\cdot\Gamma\left(a-1\right) \\
\end{aligned}
$$

取 $a=1$，有 $\Gamma\left(1\right)=1$，则对于正整数 $n$ 有 $\Gamma\left(n\right)=\left(n-1\right)!$

因此 $n! = \Gamma\left(n+1\right)$ 是阶乘的一种解析延拓方式，此时阶乘的定义域为除负整数以外的全体复数。

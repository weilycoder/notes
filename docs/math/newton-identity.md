设

$$
P\left(x\right)=\sum_{k=0}^{n}a_{k}x^{k}
$$

记 $P\left(x\right)$ 的根为 $\alpha_{k},k=1,2,\ldots,n$，定义 $S_{i}=\sum \alpha_{k}^{i}$，并且令

$$
\begin{aligned}
  \sigma_1 &= \sum\alpha_{i} = -\dfrac{a_{n-1}}{a_{n}} \\
  \sigma_2 &= \sum\alpha_{i}\alpha_{j} = \dfrac{a_{n-2}}{a_{n}} \\
  \sigma_3 &= \sum\alpha_{i}\alpha_{j}\alpha_{k} = -\dfrac{a_{n-3}}{a_{n}} \\
  &\vdots \\
  \sigma_n &= \alpha_{1}\alpha_{2}\cdots\alpha_{n} = \left(-1\right)^{n}\dfrac{a_0}{a_{n}}
\end{aligned}
$$

则有

$$
\begin{aligned}
  S_{0} &= n \\
  S_{1} &= 1\cdot\sigma_{1} \\
  S_{2} &= \sigma_{1}S_{1}-2\cdot\sigma_{2} \\
  S_{3} &= \sigma_{1}S_{2}-\sigma_{2}S_{1}+3\cdot\sigma_{3} \\
  &\vdots \\
  S_{n-1} &= \sigma_{1}S_{n-2}-\sigma_{2}S_{n-3}+\cdots+(-1)^{n-3}\sigma_{n-2}S_{1}+(-1)^{n-2}\cdot(n-1)\cdot\sigma_{n-1} \\
  &\vdots \\
  S_{m} &= \sum_{k=1}^{n}(-1)^{k+1}\sigma_{k}S_{m-k}
\end{aligned}
$$

*这里 $m\geqslant n$。*

更简洁地

$$
\boxed{
  S_{m} =
  \begin{cases}
    n, & m=0
    \\
    \begin{aligned}
    (-1)^{m+1}\cdot\sigma_{m}\cdot m+\sum_{k=1}^{m-1}(-1)^{m-1}\sigma_{k}S_{m-k}
    \end{aligned}, & 1\leqslant m\lt n
    \\
    \begin{aligned}
      \sum_{k=1}^{n}(-1)^{k+1}\sigma_{k}S_{m-k}
    \end{aligned}, & m\geqslant n
  \end{cases}
}
$$

***当 $n$ 为正无穷时，公式的第二行仍有意义。***

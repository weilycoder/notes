## 数列

### Problem 1

???+ note "Problem"

    有正项数列 $\left\{a_n\right\}$，$S_n$ 是其前 $n$ 项和，满足

    $$
    S_n=\dfrac{1}{2}\left(a_n+\dfrac{1}{a_n}\right)
    $$

    求数列通项．

#### 方法 1

注意到

$$
a_n=\sqrt{n}-\sqrt{n-1}
$$

数学归纳易证．

#### 方法 2

由 $S_n,a_n$ 关系，

$$
S_{n+1}=\dfrac{1}{2}\left(S_{n+1}-S_{n}+\dfrac{1}{S_{n+1}-S_{n}}\right)
$$

整理得

$$
S_{n+1}^2-S_{n}^2=1
$$

又

$$
S_1=a_1=\dfrac{1}{2}\left(a_1+\dfrac{1}{a_1}\right)
$$

解得 $S_1=a_1=1$，则 $S_1^2=1$．

因此，

$$
S_n^2=n
$$

由于数列各项为正，

$$
S_n=\sqrt{n}
$$

所以（$n\geqslant 2$ 时）

$$
a_{n}=\sqrt{n}-\sqrt{n-1}
$$

检验发现 $n=1$ 时式子仍成立．

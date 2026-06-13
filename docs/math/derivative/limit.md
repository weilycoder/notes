考虑到高中对导数的知识架构一塌糊涂，在这里引入极限的概念以便严格化导数的定义．

!!! note "数列极限的定义"

    数列 $\{a_n\}$ 的极限是 $L$，记作 $\lim\limits_{n \to \infty} a_n = L$，如果对于任意 $\varepsilon > 0$，存在一个正整数 $N$，使得当 $n > N$ 时，恒有 $|a_n - L| < \varepsilon$．

    特别地，如果数列 $\{a_n\}$ 的极限是正无穷，记作 $\lim\limits_{n \to \infty} a_n = +\infty$，如果对于任意 $M > 0$，存在一个正整数 $N$，使得当 $n > N$ 时，恒有 $a_n > M$；如果数列 $\{a_n\}$ 的极限是负无穷，记作 $\lim\limits_{n \to \infty} a_n = -\infty$，如果对于任意 $M < 0$，存在一个正整数 $N$，使得当 $n > N$ 时，恒有 $a_n < M$．

数学上，先定义数列极限，再定义函数极限．由于前者是离散的，因此相关定理证明较简单，从而可以为后者的相关定理证明做辅助．

!!! note "函数极限的定义"

    函数 $f(x)$ 在点 $x_0$ 的极限是 $L$，记作 $\lim\limits_{x \to x_0} f(x) = L$，如果对于任意 $\varepsilon > 0$，存在一个 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，恒有 $|f(x) - L| < \varepsilon$．

    特别地，如果函数 $f(x)$ 在点 $x_0$ 的极限是 $+\infty$，记作 $\lim\limits_{x \to x_0} f(x) = +\infty$，如果对于任意 $M > 0$，存在一个 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，恒有 $f(x) > M$；如果函数 $f(x)$ 在点 $x_0$ 的极限是 $-\infty$，记作 $\lim\limits_{x \to x_0} f(x) = -\infty$，如果对于任意 $M < 0$，存在一个 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时，恒有 $f(x) < M$．

    ---

    特别地，函数 $f(x)$ 在 $+\infty$ 处的极限是 $L$，记作 $\lim\limits_{x \to +\infty} f(x) = L$，如果对于任意 $\varepsilon > 0$，存在一个 $M > 0$，使得当 $x > M$ 时，恒有 $|f(x) - L| < \varepsilon$．
    
    特别地，如果函数 $f(x)$ 在 $+\infty$ 处的极限是 $+\infty$，记作 $\lim\limits_{x \to +\infty} f(x) = +\infty$，如果对于任意 $M > 0$，存在一个 $N > 0$，使得当 $x > N$ 时，恒有 $f(x) > M$；如果函数 $f(x)$ 在 $+\infty$ 处的极限是 $-\infty$，记作 $\lim\limits_{x \to +\infty} f(x) = -\infty$，如果对于任意 $M < 0$，存在一个 $N > 0$，使得当 $x > N$ 时，恒有 $f(x) < M$．

    ---

    特别地，函数 $f(x)$ 在 $-\infty$ 处的极限是 $L$，记作 $\lim\limits_{x \to -\infty} f(x) = L$，如果对于任意 $\varepsilon > 0$，存在一个 $M < 0$，使得当 $x < M$ 时，恒有 $|f(x) - L| < \varepsilon$．

    特别地，如果函数 $f(x)$ 在 $-\infty$ 处的极限是 $+\infty$，记作 $\lim\limits_{x \to -\infty} f(x) = +\infty$，如果对于任意 $M > 0$，存在一个 $N < 0$，使得当 $x < N$ 时，恒有 $f(x) > M$；如果函数 $f(x)$ 在 $-\infty$ 处的极限是 $-\infty$，记作 $\lim\limits_{x \to -\infty} f(x) = -\infty$，如果对于任意 $M < 0$，存在一个 $N < 0$，使得当 $x < N$ 时，恒有 $f(x) < M$．

对于函数极限的定义，有些版本会强调在 $x_0$ 附近有定义，或者说在 $x_0$ 的去心邻域 $\mathring U(x_0)$ 中有定义，但个人认为是不必要的，因为 $\lvert x-x_0\rvert < \delta$ 事实上暗示了函数在该点附近有定义（这里隐含了一个全称量词）．
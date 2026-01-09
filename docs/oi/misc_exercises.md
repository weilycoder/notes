存档一份 [QOJ 难度评级说明](https://qoj.ac/blog/qingyu/blog/1280)，方便估计难度．

但是好像极限在难度 4 ~ 5 了．

??? note "QOJ 难度"

    + 难度 0 ：最简单的竞技题目，即使是没有任何算法竞赛经历的人士，在具备使用任意一种编程语言编写程序的能力下便可轻松通过，大致可对应 Codeforces 难度 800 ~ 1000 的题目，TopCoder SRM Div. 2 的 250 分题目，或是 AtCoder Beginner Contest 的第一道题目．
    + 难度 1：需要选手具有一定时间的程序设计经验，或者需要使用初步的数学与简单的算法设计能力．不具备算法竞赛经历的选手仍可解决这些题目，但可能需要消耗一定的时间．大致可对应 Codeforces 难度 1000 ~ 1600 的题目，亚洲区域赛或 NERC 区域赛的签到题的难度，以及 AtCoder Beginner Contest 的前四道题目．
    + 难度 2：具有一定竞技门槛的题目．题目考查了一些算法竞赛中常用的 trick，或者具备一定的思维难度．这一类题目可被定义为最低一档的「竞赛题」，未经训练的程序设计者在解决时会遇到许多困难．大致可对应 Codeforces 难度 1500 ~ 1900 的题目，亚洲区域赛或 NERC 区域赛区分铜牌队伍的题目的难度，以及 USACO Silver 难度的题目．
    + 难度 3：大致可对应 Codeforces 难度 1800 ~ 2400 的题目，ICPC 亚洲区域赛中区分铜牌 ～ 银牌队伍的题目的难度，以及通常 USACO 中 Gold 难度的题目．
    + 难度 4：大致可对应 Codeforces 难度 2300 ~ 2800 的题目，USACO Gold ~ Platinum 题目，ICPC 亚洲区域赛中区分银牌 ～ 金牌队伍的题目，以及国际信息学奥林匹克竞赛（IOI）大多数年份中难度最低一档的题目．在国际信息学奥林匹克竞赛（IOI）中通过的选手数大约在 100，而在 Universal Cup 中出现时通常的 AC 数为 70 ~ 100+．
    + 难度 5：大致可对应 Codeforces 难度 2600 ~ 3200 的题目，USACO Platinum 题目的难度，ICPC 亚洲区域赛中区分靠前金牌队伍甚至出线队伍区分度题目．在国际信息学奥林匹克竞赛（IOI）中通过的选手数通常在 50，在 ICPC World Finals 中出现时通常的 AC 数为 10 ~ 30，在 Universal Cup 中出现时通常的 AC 数为 20 ~ 50．
    + 难度 6：大致可对应 Codeforces 难度 3000 ~ 3500 的题目，ICPC 区域赛中针对前若干名队伍所区分的题目，ICPC 全球总决赛（World Finals）针对奖牌区队伍所区分的题目，以及国际信息学奥林匹克竞赛（IOI）中取得金牌的区分度所对应的题目．在国际信息学奥林匹克竞赛（IOI）中通过的选手数通常在 10 ～ 20，在 ICPC World Finals 中出现时通常的 AC 数为 3 ~ 10，在 Universal Cup 中出现时通常的 AC 数为 10 ~ 30．
    + 难度 7：大致可对应 Codeforces 难度 3500+ 的题目，ICPC 比赛中针对冠军队伍所区分的题目，以及国际信息学奥林匹克竞赛（IOI）中区分最顶尖的选手所对应的题目．在国际信息学奥林匹克竞赛（IOI）中通过的选手数通常在 0 ～ 5，在 ICPC World Finals 中出现时通常的 AC 数为 0 ~ 3，在 Universal Cup 中出现时通常的 AC 数为 1 ~ 10．
    + 难度 8：国际信息学奥林匹克竞赛（IOI）中难度最高的一档题目，不太可能在 Codeforces 或 AtCoder 等短时间多题数的比赛中有选手解出．即使在大多数比赛，也几乎没有队伍或选手通过的题目．只有最强的选手有机会在赛时通过这些题目，且需要消耗可观的时间．在国际信息学奥林匹克竞赛（IOI）中通过的选手数通常在 0 ～ 1，在 ICPC World Finals 中出现时通常的 AC 数为 0，在 Universal Cup 中出现时通常的 AC 数为 0 ~ 2．
    + 难度 9：难度极高的题目，在 IOI 或 ICPC 中不可能会被任何选手解出．即便在 AtCoder World Tour Finals、Meta Hacker Cup、Universal Cup 等时间较长且具有许多高水平算法竞赛选手的赛场上，有经验的选手经过长时间也可能会遇到很多阻碍，几乎不具有通过的可能性．在 Universal Cup 中出现时通常的 AC 数为 0．
    + 难度 10：没有任何机会的题目．题目的难度极高，在任何比赛中都不会有选手能够在数小时内解出此题．在 Universal Cup 中出现时通常的 AC 数为 0．

## *[2]* P-smooth number (ABC 300 G) 

> 若一个数的质因数均不超过 $k$，称其为 $k$-smooth number．
>
> 给定 $N,p$ 求 $N$ 以内 $p$-smooth number 的个数．
>
> + $1\leqslant N\leqslant 10^{16}$；
> + $2\leqslant p\leqslant 100$，且 $p$ 为质数．

样例 2 极具提示性．

注意到输入为 $N=10^{16},p=97$ 时，输出 $2\ 345\ 134\ 674$，大约只有 $2\times 10^{9}$．

考虑暴搜．

但是 2e9 就算是 AT 神机估计也得跑个 6s 左右．

考虑 meet-in-middle，把 $p$ 以内的质数分成 2 组，分别暴搜．

可以按质数从小到大交替分到两组中，平衡效率：

$$
\begin{aligned}
  P_{0} &= \left\{2, 5, 11, 17, 23, 31, 41, 47, 59, 67, 73, 83, 97 \right\} \\
  P_{1} &= \left\{3, 7, 13, 19, 29, 37, 43, 53, 61, 71, 79, 89 \right\}
\end{aligned}
$$

这样在 $P_{0}$ 中暴搜时枚举量为 $6\ 269\ 654$，在 $P_{1}$ 中暴搜时枚举量为 $1\ 913\ 116$；

也可以把 $97$ 放到 $P_{1}$ 中，这样枚举量分别为 $4\ 221\ 248$ 和 $2\ 864\ 380$．

统计答案时可以排序后双指针．

??? note "Code"

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;

    array<uint32_t, 12> prime0{2, 5, 11, 17, 23, 31, 41, 47, 59, 67, 73, 83};
    array<uint32_t, 13> prime1{3, 7, 13, 19, 29, 37, 43, 53, 61, 71, 79, 89, 97};

    template <size_t Len>
    void dfs(size_t cur, uint64_t val, uint64_t limit, uint32_t p,
            const array<uint32_t, Len> &prime, vector<uint64_t> &res) {
    if (cur == Len || prime[cur] > p)
        res.push_back(val);
    else
        for (; val <= limit; val *= prime[cur])
        dfs<Len>(cur + 1, val, limit, p, prime, res);
    }

    template <size_t Len>
    vector<uint64_t> get_smooth(uint64_t limit, uint32_t p,
                                const array<uint32_t, Len> &prime) {
    vector<uint64_t> res;
    dfs<Len>(0, 1, limit, p, prime, res);
    sort(res.begin(), res.end());
    return res;
    }

    int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    uint64_t N;
    uint32_t p;
    cin >> N >> p;
    auto r1 = get_smooth(N, p, prime0);
    auto r2 = get_smooth(N, p, prime1);
    uint64_t cnt = 0;
    size_t pt = r2.size();
    for (uint64_t x : r1) {
        while (pt == 0 || r2[pt - 1] * x > N)
        --pt;
        cnt += pt;
    }
    cout << cnt << '\n';
    return 0;
    }
    ```

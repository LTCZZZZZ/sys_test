# 计算布洛妮娅1星魂的实际收益
# 问题抽象：考虑离散的无穷序列，从1开始往后，1，2，3，...，在每个点，事件A发生的概率遵从如下规则：
# 如果在前一点事件A发生，则在当前点事件A发生的概率为p，否则为q，
# 对此问题，p=0，q=0.5，求在此无穷序列中事件A发生的综合概率
# 上述综合概率的严格定义如下：N为正整数，m为从1到N，A发生的次数，综合概率P定义为lim(N->inf) m/N
import random
import matplotlib.pyplot as plt


def simulate(p, q, n):
    """
    计算机随机数模拟
    :param p: 在前一点事件A发生，则在当前点事件A发生的概率为p
    :param q: 在前一点事件A不发生，则在当前点事件A发生的概率为q
    :param n: 从1到n
    :return: 事件A发生的综合概率
    """
    # 事件A发生的次数
    m = 0
    # 概率P的序列
    PList = []
    # 前一点事件A是否发生
    pre = False
    for i in range(1, n + 1):
        if pre:
            if random.random() < p:
                m += 1
                pre = True
            else:
                pre = False
        else:
            if random.random() < q:
                m += 1
                pre = True
            else:
                pre = False
        PList.append(m / i)

    draw(PList)
    return m / n, PList


def draw(PList):
    plt.plot(PList)
    plt.show()


def probability(p, q, n):
    """
    实际计算概率
    """
    # a为当前点事件A发生的概率，b为当前点事件A不发生的概率
    a = q
    b = 1 - q
    a_list = [a]
    b_list = [b]
    for i in range(1, n):
        # 注意：a, b不能分开写，要同时写在一个式子中
        a, b = a * p + b * q, a * (1 - p) + b * (1 - q)
        a_list.append(a)
        b_list.append(b)
    print(a_list)
    print(sum(a_list) / n)
    print(b_list)
    print(sum(b_list) / n)
    plt.plot(a_list, label='a')
    plt.plot(b_list, label='b')
    plt.legend()  # 显示图例
    plt.show()

    # 化简完之后递推公式为：a[n+1] = q + (p-q)a[n]，这是高中学过的常规型，
    # 将a[n]+x构造成等比数列，即(a[n+1]+x)/(a[n]+x) = p-q，解得x = q/(p-q-1)，
    # 于是求得通项公式为a[n] = (p-q)^(n-1) * (a[1]+x) - x
    # 前n项和S[n] = (a[1]+x) * (1-(p-q)^n) / (1-(p-q)) - x * n
    # 下面验证计算结果和for循环计算的结果一致
    a1 = q
    x = q / (p - q - 1)
    an_list = [(p - q) ** (i - 1) * (a1 + x) - x for i in range(1, n + 1)]
    print(an_list)

    # 由于浮点数的精度问题，这里不能直接比较，需要设置误差
    for i in range(n):
        assert an_list[i] - a_list[i] < 1e-10
    S_list = [(a1 + x) * (1 - (p - q) ** i) / (1 - (p - q)) - x * i for i in range(1, n + 1)]
    for i in range(n):
        assert S_list[i] - sum(a_list[:i + 1]) < 1e-10

    # 此数列还有一个性质，lim(N->inf) S[n]/n - a[n] = 0，即S[n]/n逼近a[n]，其实a[n]的极限存在，就等于-x，即q/(1-p+q)
    # 这和大数定律的表现形式很像


if __name__ == '__main__':
    P, PList = simulate(0, 0.5, 10000)  # 确实是逼近1/3，但如何证明？
    print(P)
    # P, PList = simulate(0.5, 0.5, 100000)
    # print(P)
    # P, PList = simulate(0.2, 0.8, 100000)
    # print(P)
    # P, PList = simulate(0.8, 0.2, 100000)
    # print(P)

    probability(0, 0.5, 100)

    # 测试发现，如果p+q=1，那么P趋近于0.5

# 如果不用期望累加的方法，而是考虑马尔科夫链的稳态，设稳态存在，为[P, 1-P]，状态转移矩阵为[[p, 1-p], [q, 1-q]]，
# 则有[P, 1-P] = [P, 1-P] * [[p, 1-p], [q, 1-q]]，即P=Pp+(1-P)q，1-P=P(1-p)+(1-P)(1-q)，化简后，这两个式子是等价的，
# 解得P = q/(1-p+q)，
# 带入p=0，q=0.5，得P=1/3，与上面的结果一致，
# 带入p+q=1，得P=0.5，与上面的结果一致，

# 但这个方法有一个问题，就是要先证明对这个链，稳态存在
# 在不可约、非周期、正常返的条件下，马尔科夫链拥有唯一稳态分布，且每个状态的概率都大于0。
# 此外，期望累计法似乎更符合上述综合概率的定义，马尔科夫链求出的结果更像是，事件还未实际发生，然后去估算，在无穷远的单个点处，A发生的概率
# 不知道这两种方法是否在某种程度上可以等价

# 答：已经发生的东西，用其分布来描述概率是自然的

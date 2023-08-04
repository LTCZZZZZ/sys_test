# 计算日麻天和的概率
# 参考：https://www.zhihu.com/question/27549138/answer/37131792

from functools import partial
from scipy.special import comb, perm

comb = partial(comb, exact=True)


def main():
    # 任意数牌组成【m的面子+n个雀头】的组合数，m<=4, n<=1
    # 先考虑最简单的m=1，n=0，即36张1-9m中任取3张组成面子的组合数
    # 牌型有123，234，345，456，567，678，789，再加上9种暗刻型
    count = comb(4, 1) ** 3 * 7 + comb(4, 3) * 9  # 484
    print(count)







if __name__ == '__main__':
    # print(perm(136, 14, True))  # 370534329521651228232499200000
    # print(comb(136, 14, True))  # 4250305029168216000
    main()

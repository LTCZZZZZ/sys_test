# 计算日麻天和的概率
# 参考：https://www.zhihu.com/question/27549138/answer/37131792

from functools import partial
from scipy.special import comb, perm
import pandas as pd

from fishing import get_cards2, is_complete

comb = partial(comb, exact=True)

# 一般型
# 成型后含对子时牌的张数：2，2+3，2+3+3，2+3+3+3，2+3+3+3+3
pair_num = [2, 5, 8, 11, 14]
# 成型后不含对子时牌的张数：3，3+3，3+3+3，3+3+3+3
no_pair_num = [3, 6, 9, 12]


def trivial():
    """
    思考过程记录，非正式运行的程序
    :return:
    """
    # 任意数牌组成【m的面子+n个雀头】的组合数，m<=4, n<=1
    # 先考虑最简单的m=1，n=0，即36张1-9m中任取3张组成面子的组合数
    # 牌型有123，234，345，456，567，678，789，再加上9种暗刻型
    count = comb(4, 1) ** 3 * 7 + comb(4, 3) * 9  # 484
    print(count)

    # 再考虑m=1, n=1，分3种情况：12311这种，12344这种，11122这种
    count = comb(4, 3) * comb(4, 1) * comb(4, 1) * 3 * 7 + \
            comb(4, 1) ** 3 * comb(4, 2) * 6 * 7 + \
            comb(4, 3) * comb(4, 2) * 9 * 8  # 19200
    print(count)

    # 考虑最复杂的m=4, n=1，此时人脑列举感觉复杂度已经超了，得想别的办法


def num_combs():
    """
    从pair_num中取一个，然后从no_pair_num中取若干(小于等于3个)，满足加和等于14，即一般型的组合
    :return:
    """



def cards_comb(cards: str):
    """
    计算cards的组合数，cards为单种牌，m,p,s,z中的一种
    :param cards: 示例值：11123
    :return:
    """
    res = 1
    for i in range(1, 10):
        count = cards.count(str(i))
        res *= comb(4, count)
    return res


def compute_combs(type='a'):
    """
    一般型，成型时数牌、字牌的组合数计算
    :return: DataFrame
    """

    if type == 'z':
        base = range(1, 8)
    else:
        base = range(1, 10)

    # 索引列表示张数，接下来依次是 牌型数、有效牌型数、有效组合数
    df = pd.DataFrame(columns=['patterns', 'valid_patterns', 'valid_combs'])
    for i in pair_num + no_pair_num:
        # 这里在计算get_cards2时，其实有很多重复计算，但耗时不长，暂时忽略
        cards_list = get_cards2(i, base=base)
        patterns = len(cards_list)
        valid_patterns = 0
        valid_combs = 0
        for cards in cards_list:
            if is_complete(cards, type=type):
                valid_patterns += 1
                valid_combs += cards_comb(cards)
        df.loc[i] = [patterns, valid_patterns, valid_combs]

    # 排序
    df.sort_index(inplace=True)
    return df


def main():
    number = compute_combs(type='a')
    print(number)
    word = compute_combs(type='z')
    print(word)
    # numbers最后一行有效牌型13259，对应有效组合440593684，
    # word   最后一行有效牌型  105，对应有效组合   161280，
    # 两相对比，可以看出字一色的难度要比清一色高很多，有效组合数足足差了约2732倍

    # 下面可以计算天和的概率了
    # 从pair_num中取一个，然后从no_pair_num中取若干(小于等于3个)，满足加和等于14，即一般型的组合
    num_combs = []
    for i in pair_num:
        while 14 - i > 0:
            pass






if __name__ == '__main__':
    # print(perm(136, 14, True))  # 370534329521651228232499200000
    # print(comb(136, 14, True))  # 4250305029168216000

    print(cards_comb('11123'))  # 64

    # trivial()

    # number()
    main()

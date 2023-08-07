# 此文件包罗万象：类的使用(加法、iter、repr等)，递归、生成器、深拷贝等等
# 麻将计算器，m表示万，p表示饼，s表示索，z1-7表示东南西北中发白
import time
import re
from copy import deepcopy

from scipy.special import comb, perm

# 一般型
# 成型后含对子时牌的张数：2，2+3，2+3+3，2+3+3+3，2+3+3+3+3
pair_num = [2, 5, 8, 11, 14]
# 成型后不含对子时牌的张数：3，3+3，3+3+3，3+3+3+3
no_pair_num = [3, 6, 9, 12]


class Cards:

    def __init__(self, cards=None):
        self.m = []
        self.p = []
        self.s = []
        self.z = []
        if cards is None:
            return

        match = re.findall(r'(\d+)([mpsz])', cards)
        for i, t in match:
            # print(i, t)
            setattr(self, t, [int(k) for k in i])

    def __len__(self):
        return len(self.m) + len(self.p) + len(self.s) + len(self.z)

    def __add__(self, other):
        # 定义加法
        res = Cards()
        for i in ['m', 'p', 's', 'z']:
            setattr(res, i, sorted(getattr(self, i) + getattr(other, i)))
        return res

    def __iter__(self):
        for i in ['m', 'p', 's', 'z']:
            for j in getattr(self, i):
                yield Cards(f'{j}{i}')

    def __str__(self):
        return f'm:{self.m}\np:{self.p}\ns:{self.s}\nz:{self.z}'

    def __repr__(self):
        """
        当不直接print该对象，而是比如print([Cards('123m'), Cards('123p')])时，会调用该方法
        """
        res = ''
        for i in ['m', 'p', 's', 'z']:
            if temp := getattr(self, i):
                res += ''.join([str(j) for j in temp]) + i
        return res

    def suits(self):
        res = []
        for i in ['m', 'p', 's', 'z']:
            if getattr(self, i):
                res.append(i)
        return res


def get_match(i, type='a'):
    """
    获取i的匹配列表
    :param i:
    :param type: 默认参数a表示数牌所有类型，z表示字牌，逻辑是只要传参不是z则都使用数牌的算法
    :return:
    """
    res = []
    i = int(i)
    res.append([i, i, i])

    if type != 'z':
        # 这个思路有点意思
        if i <= 7:
            res.append([i, i + 1, i + 2])
        if 2 <= i <= 8:
            res.append([i - 1, i, i + 1])
        if i >= 3:
            res.append([i - 2, i - 1, i])

    return res


def cards_pop(cards: list[int], c_match: list[int]):
    """
    如果c_match中的元素全部在cards中，则从cards中剔除c_match，否则返回0，cards
    :param cards:
    :param c_match:
    :return:
    """

    # 不要修改原来的cards
    cards = deepcopy(cards)
    # print(cards, c_match)

    signal = 1
    for c in c_match:
        # 这代码行不通，反例：cards=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5]，c_match=[1, 1, 1]
        # if c not in cards:
        #     signal = 0
        #     break
        if c_match.count(c) > cards.count(c):
            signal = 0
            break

    if signal:
        for c in c_match:
            cards.remove(c)
        return 1, cards
    else:
        return 0, cards


def eliminate_pair_generator(cards: Cards):
    """
    将对子剔除的生成器，返回所有可能的列表(生成器)，如22335会返回[335, 225]，2345会返回[]
    :param cards:
    :return:
    """

    def onefold(cards: list[int]):
        """
        处理单一花色
        """
        # print(cards)
        if len(cards) in pair_num:
            # 使用set去重
            for c in sorted(set(cards)):
                # print(cards, c)
                if cards.count(c) >= 2:

                    # 不要修改原来的cards
                    cards_copy = deepcopy(cards)

                    cards_copy.remove(c)
                    cards_copy.remove(c)
                    # print(cards_copy)
                    yield cards_copy

    # 这个写法还行，但不算特别优雅
    for s in cards.suits():
        # 因为onefold不会修改传入的变量，所以这里deepcopy可以放在下面的循环外
        cards_copy = deepcopy(cards)
        for c in onefold(getattr(cards, s)):
            setattr(cards_copy, s, c)
            yield cards_copy


def no_pair(cards: Cards):
    """
    判断cards是否组成了不含对子的一般型（有几种组法-兼顾性能时不考虑组法）
    """

    def onefold(cards: list[int]):
        """
        处理单一花色
        """
        # print(cards)
        complete = 0
        if len(cards) == 0:
            return 1  # 处理边界条件，cards为空时，说明前面的已经全部匹配，返回1
        if len(cards) not in no_pair_num:
            return complete

        for c_match in get_match(cards[0]):
            # c_match是一种含c的面子，如[1, 2, 3]
            # print(cards, cards[0], c_match)
            signal, sub_cards = cards_pop(cards, c_match)
            # print(signal, sub_cards)
            if signal:
                complete += onefold(sub_cards)
                # print(f'complete: {complete}')

            # 如果要追求速度，加上以下代码，即只要匹配到就返回，不再继续匹配
            if complete:
                return complete  # 此时onefold返回的complete最多为1，因为只要匹配到就返回了

        # print(cards, complete)
        return complete

    complete = True
    for s in cards.suits():
        # 即只要有一种花色不满足，就返回False
        if not onefold(getattr(cards, s)):
            complete = False
            break

    return complete


def is_complete(cards: Cards):
    """
    判断cards是否和牌
    :param cards:
    :return:
    """
    if len(cards) in pair_num:
        for cs in eliminate_pair_generator(cards):
            if no_pair(cs):
                return True
    else:
        if no_pair(cards):
            return True
    return False


def fishing(cards: Cards):
    """
    判断牌型组合所听的牌
    :param cards:
    :return:
    """
    time0 = time.time()

    listen_cards = Cards()
    all_cards = Cards('123456789m123456789p123456789s1234567z')
    for c in all_cards:
        cards_copy = cards + c
        if is_complete(cards_copy):
            listen_cards += c

    time_cost = time.time() - time0
    return listen_cards, f'{time_cost:.3f} s'


if __name__ == '__main__':
    # cards = Cards('123456789m123456789p123456789s1234567z')
    # print(cards)
    # c1 = Cards('123m123p123s2z')
    # for c in c1:
    #     print(c)
    # c2 = Cards('123m456p789s1z')
    # c3 = c1 + c2
    # print(c3)

    print(perm(136, 14, True))
    print(comb(136, 14, True))

    # c = Cards('123m123p123s2z')
    # print(fishing(c))

    for t in ('1112345678999m', '222m4445p666s777z', '345m11234p23456s'):
        c = Cards(t)
        print(fishing(c))


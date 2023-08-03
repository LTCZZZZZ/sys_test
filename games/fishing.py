# 特别注意：set函数得到的结果是没排序的，在需要的场景下要使用sorted函数进行排序

# 问：麻将只听2478的牌型存在吗？2678呢？
# 先考虑听2478而不考虑只听
import time
# 获取一副牌的听牌（如果没听返回None）：
# 思路1：从现有牌开始组合，看缺的一张
# 思路2：遍历加入所有单张牌，判断是否胡牌

from copy import deepcopy
from itertools import combinations, permutations


def get_match(i):
    """
    获取i的匹配列表
    :param i:
    :return:
    """
    res = []
    i = int(i)
    res.append([i, i, i])

    # 这个思路有点意思
    if i <= 7:
        res.append([i, i + 1, i + 2])
    if 2 <= i <= 8:
        res.append([i - 1, i, i + 1])
    if i >= 3:
        res.append([i - 2, i - 1, i])

    return res


def cards_pop(cards, c_match):
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


def is_complete(cards):
    """
    判断cards是否组成了一般型
    :param cards:
    :return:
    """
    # 成型后含对子时牌的张数：2，2+3，2+3+3，2+3+3+3，2+3+3+3+3
    pair_num = [2, 5, 8, 11, 14]
    # 成型后不含对子时牌的张数：3，3+3，3+3+3，3+3+3+3
    no_pair_num = [3, 6, 9, 12]

    cards = [int(i) for i in cards]

    # 统计递推次数
    recursion = 0

    def no_pair(cards):
        """
        判断cards是否组成了不含对子的一般型，有几种组法
        :param cards:
        :return:
        """
        nonlocal recursion
        recursion += 1
        # print(cards)

        complete = 0
        if len(cards) == 0:
            return 1  # 处理边界条件，cards为空时，说明前面的已经全部匹配，返回1
        if len(cards) not in no_pair_num:
            return complete

        # # 这里使用set(cards)，因为如果整体匹配到了，直接返回成功，而匹配失败的话，也不需要用同样的数字再来一次
        # for c in sorted(set(cards)):
        #     for c_match in get_match(c):
        #         # c_match是一种含c的面子，如[1, 2, 3]
        #         # print(cards, c, c_match)
        #         signal, sub_cards = cards_pop(cards, c_match)
        #         # print(signal, sub_cards)
        #         if signal:
        #             complete += no_pair(sub_cards)
        #             # print(f'complete: {complete}')
        #
        #         # 如果要追求速度，加上以下代码，即只要匹配到就返回，不再继续匹配
        #         if complete:
        #             return complete  # 此时no_pair返回的complete最多为1，因为只要匹配到就返回了

        # 思考后发现这个外层for循环完全没有必要，因为get_match函数已经包含了匹配成功时所有可能的情况
        # 直接去掉外层for循环后代码如下：将cards[0]作为参数传入get_match函数
        for c_match in get_match(cards[0]):
            # c_match是一种含c的面子，如[1, 2, 3]
            # print(cards, cards[0], c_match)
            signal, sub_cards = cards_pop(cards, c_match)
            # print(signal, sub_cards)
            if signal:
                complete += no_pair(sub_cards)
                # print(f'complete: {complete}')

            # 如果要追求速度，加上以下代码，即只要匹配到就返回，不再继续匹配
            if complete:
                return complete  # 此时no_pair返回的complete最多为1，因为只要匹配到就返回了

        # print(cards, complete)
        return complete

    def eliminate_pair_generator(cards):
        """
        将对子剔除的生成器
        :param cards:
        :return:
        """

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

    # 找出所有成型的牌，并计数
    complete = 0
    if len(cards) in pair_num:
        for cs in eliminate_pair_generator(cards):
            complete += no_pair(cs)

            # 如果要追求速度，加上以下代码，即只要匹配到就返回，不再继续匹配
            # 九莲宝灯速度从1.3s左右下降到0.4s左右，但感觉还是不够快，这个算法似乎已经很难优化了
            # 错，再次找问题并细致优化过后，九莲宝灯速度从0.4s左右下降到0.001s，性能巨幅提升，达到实际可用的程度了
            if complete:
                break
    else:
        complete += no_pair(cards)

    # 打印递归次数
    # print(f'{cards}: {recursion}')
    return complete


def fishing(cards):
    """
    只考虑单种数牌、一般型(即清一色不含七对)，计算听牌面数，能向上加1张组成一种型即可，称为成型
    默认cards是已排序过的
    如3-3，34-25，3334-245，3334567-24578，3456667-2578
    :param cards:
    :return:
    """
    # 成型后含对子时成型前牌的张数：1，1+3，1+3+3，1+3+3+3，1+3+3+3+3
    # pair_num = [1, 4, 7, 10, 13]
    # 成型后不含对子时成型前牌的张数：2，2+3，2+3+3，2+3+3+3
    # no_pair_num = [2, 5, 8, 11]

    time0 = time.time()
    cards = [int(i) for i in cards]

    listen = []
    for i in range(1, 10):
        cards_copy = cards + [i]
        cards_copy.sort()
        if is_complete(cards_copy):
            listen.append(i)

    time_cost = time.time() - time0
    return listen, f'{time_cost:.3f} s'


def get_cards(num):
    """
    num张牌所有可能的组合
    :param num:
    :return:
    """
    s = '123456789' * 4
    res = []
    for i in combinations(s, num):
        # 注意这里i要先排序，否则13和31会被认为是不同的组合
        res.append(''.join(sorted(i)))
    print(len(res))
    res = sorted(set(res))
    print(len(res))
    return res


def from_listen_to_cards(listen, num=7, cards_list=None):
    """
    清一色不含七对，计算听指定牌的所有可能牌型，牌张数为num，这个结果print就行
    此函数同时返回num张牌可听的最多张数及对应的牌型
    :param listen:
    :param num:
    :param cards_list: 如果有cards_list，则不使用num，优先使用cards_list
    :return: 返回num张牌可听的最多张数
    """
    listen = [int(i) for i in listen]
    if not cards_list:
        cards_list = get_cards(num)

    max_listen = 0
    specified_listen = []
    for cards in cards_list:
        listen_, _ = fishing(cards)
        if len(listen_) > max_listen:
            max_listen = len(listen_)
            specified_listen = [(cards, listen_)]
        elif len(listen_) == max_listen:
            specified_listen.append((cards, listen_))
        if listen_ == listen:
            print(cards, listen)

    return max_listen, specified_listen


if __name__ == '__main__':
    # cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(cards_pop(cards, [1, 2, 3]))
    # print(cards)

    # print(is_complete([1, 2, 3]))
    # print(is_complete([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 优化前：162  # 后，递归次数4

    # print(is_complete('124567'))
    print(is_complete('11112345678999'))  # 递归次数7
    print(is_complete('11123345678999'))  # 递归次数5

    # for v in ['33', '234', '33344', '33345', '33345567']:
    #     print(v, is_complete(v))

    for v in ['3', '34', '3334', '3334567', '3456667', '1113455678999', '1112345678999']:
        print(v, fishing(v))

    # 在单一数牌中任选2张牌，有多少种组合方式？
    # 9*8/2 + 9 = 45种
    # print(get_cards(2))

    # 但是如果任选7张，问题就复杂了，因为每种数牌最多只有4张，所以任意单张不能超过4
    # cards_list = get_cards(6)  # 1947792 2992
    # cards_list = get_cards(7)  # 8347680 6030，这是暴力算出来的，6030种组合

    # 现在可以考虑听2478的问题了
    # 先考虑7张牌的情况
    cards_list = get_cards(7)
    from_listen_to_cards('2578', cards_list=cards_list)  # 3456667
    from_listen_to_cards('24578', cards_list=cards_list)  # 3334567
    res = from_listen_to_cards('2478', cards_list=cards_list)  # 7张组合中，只听2478的牌型不存在
    # 7张组合和5面的总共只有11种，如下
    print(res)  # 2223444, 2223456, 2345666, 3334555, 3334567, 3456777, 4445666, 4445678, 4567888, 5556777, 6667888




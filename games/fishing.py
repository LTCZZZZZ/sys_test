# 问：麻将只听2478的牌型存在吗？2678呢？
# 先考虑听2478而不考虑只听

# 获取一副牌的听牌（如果没听返回None）：
# 思路1：从现有牌开始组合，看缺的一张
# 思路2：遍历加入所有单张牌，判断是否胡牌

from copy import deepcopy


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

    def no_pair(cards):
        """
        判断cards是否组成了不含对子的一般型，有几种组法
        :param cards:
        :return:
        """
        complete = 0
        if len(cards) == 0:
            return 1  # 处理边界条件，cards为空时，说明前面的已经全部匹配，返回1
        if len(cards) not in no_pair_num:
            return complete
        for c in cards:
            for c_match in get_match(c):
                # c_match是一种含c的面子，如[1, 2, 3]
                # print(cards, c, c_match)
                signal, sub_cards = cards_pop(cards, c_match)
                # print(signal, sub_cards)
                if signal:
                    complete += no_pair(sub_cards)
                    # print(f'complete: {complete}')
        # print(cards, complete)
        return complete

    def eliminate_pair_generator(cards):
        """
        将对子剔除的生成器
        :param cards:
        :return:
        """
        # 不要修改原来的cards
        cards = deepcopy(cards)

        if len(cards) in pair_num:
            # 使用set去重
            for c in set(cards):
                # print(cards, c)
                if cards.count(c) >= 2:
                    cards.remove(c)
                    cards.remove(c)
                    yield cards

    # 找出所有成型的牌，并计数
    complete = 0
    if len(cards) in pair_num:
        for cs in eliminate_pair_generator(cards):
            complete += no_pair(cs)
    else:
        complete += no_pair(cards)

    return complete


def fishing(cards):
    """
    只考虑单种数牌、一般型，计算听牌面数，能向上加1张组成一种型即可，称为成型
    默认cards是已排序过的
    如3-3，34-25，3334-245，3334567-24578
    :param cards:
    :return:
    """
    # 成型后含对子时成型前牌的张数：1，1+3，1+3+3，1+3+3+3，1+3+3+3+3
    # pair_num = [1, 4, 7, 10, 13]
    # 成型后不含对子时成型前牌的张数：2，2+3，2+3+3，2+3+3+3
    # no_pair_num = [2, 5, 8, 11]

    cards = [int(i) for i in cards]

    listen = []
    for i in range(1, 10):
        cards_copy = cards + [i]
        cards_copy.sort()
        if is_complete(cards_copy):
            listen.append(i)
    return listen


if __name__ == '__main__':
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(cards_pop(cards, [1, 2, 3]))
    # print(cards)

    # print(is_complete([1, 2, 3]))
    print(is_complete([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 162

    for v in ['33', '234', '33344', '33345', '33345567']:
        print(v, is_complete(v))

    for v in ['3', '34', '3334', '3334567']:
        print(v, fishing(v))




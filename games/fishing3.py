# 计算日麻天和的概率
# 参考：https://www.zhihu.com/question/27549138/answer/37131792
import time
from functools import partial
from itertools import combinations, permutations, product

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
    :return: [2, 3, 3, 6], [2, 3, 9], [2, 6, 6], [2, 12], [5, 3, 3, 3], [5, 3, 6], [5, 9], [8, 3, 3], [8, 6], [11, 3], [14]
    """

    # 下面尝试各种方法

    # 方法一：因为列表长度不超过4，最简单的方法是遍历C(5,1)与5**3(因为no_pair_num可重复，且需加上0元素)的笛卡尔积，取和为14的组合即可
    # temp = [pair_num]
    # for i in range(3):
    #     temp.append(no_pair_num + [0])
    # temp = product(*temp)
    # temp = [tuple(sorted(i)) for i in temp if sum(i) == 14]  # 筛选过滤并排序后设为元组，便于下一步去重
    # temp = set(temp)  # 去重
    # temp = [[i for i in x if i != 0] for x in temp]  # 去除0元素
    # print(len(temp))
    # print(temp)
    # return temp

    # 方法二：其实根本思想和product差不多，只是，需要兼容考虑如果不存在位置上限，而是存在和上限14时，代码要怎么写
    # 即先假设pair_num中取一个，但no_pair_num中可无限取值(可取重复元素)，只要总和不超过14
    # 因为no_pair_num中可无限重复取值，故这里用了一个默认条件，即no_pair_num中的元素各不相同，且从小到大排列
    # res = []
    # for i in pair_num:
    #     temp = [i]
    #     start = 0
    #     while True:
    #         # time.sleep(0.5)
    #         print(temp, start)
    #
    #         if sum(temp) == 14:
    #             res.append(temp.copy())
    #             # 其实因为是从小到大排列的，这里匹配到之后，可以双退向，然后适当设置start，再continue，可减少循环次数
    #             # 但考虑过后为了让逻辑更清晰（即确定大于时再双退向），决定不这么写，相关操作放到sum(temp) > 14的部分
    #             temp.pop()
    #             start += 1
    #         elif sum(temp) > 14:
    #             # 注意这里的操作，先退一个元素，再退一个元素并获取其索引index，然后设置start设置为index+1
    #             temp.pop()
    #             # 边界条件
    #             if len(temp) == 1:
    #                 break
    #             index = no_pair_num.index(temp.pop())
    #             start = index + 1
    #         else:
    #             pass
    #
    #         # 这部分放到最后，兼容[14]的情况
    #         if start == len(no_pair_num):
    #             break
    #         temp.append(no_pair_num[start])
    #
    # res = [x for x in res if len(x) <= 4]
    # print(len(res))
    # print(res)
    # return res

    # 方法二优化版，可兼容no_pair_num有重复元素，且无序的情况
    # res = []
    # for i in pair_num:
    #     temp = [i]
    #     # 用于记录迭代到temp中指定位置对应的no_pair_num中的元素的索引
    #     indexes = [0]
    #     while True:
    #         print(temp, indexes)
    #
    #         if sum(temp) == 14:
    #             res.append(temp.copy())
    #             temp.pop()
    #             indexes[-1] += 1
    #         elif sum(temp) > 14:
    #             temp.pop()
    #             indexes[-1] += 1
    #         else:
    #             indexes.append(0)
    #             pass
    #
    #         while indexes[-1] == len(no_pair_num):
    #             if len(temp) == 1:
    #                 break
    #             temp.pop()
    #             indexes.pop()
    #             indexes[-1] += 1
    #
    #         if len(temp) == 1 and indexes[-1] == len(no_pair_num):
    #             break
    #
    #         temp.append(no_pair_num[indexes[-1]])
    #
    # res = [sorted(x) for x in res if len(x) <= 4]
    # res = [tuple(x) for x in res]
    # res = set(res)
    # print(len(res))
    # print(res)
    # return res

    # 方法三：思考：方法二的代码执行效率可能是最高的，但是代码逻辑不够清晰，能否用递归的思想来写呢？
    def func(no_pair_num, res, temp):
        """
        这个函数的思想是，如果sum(temp) > 14，则pop，如果sum(temp) == 14，则append后pop
        它相当于一个检验程序，检验temp是否满足条件，小于14则append后再次调用自身，调用完成后pop，因为调用方执行完后，sum(temp)必然>=14

        这个函数完美实现了我想要的效果，即在每一层开始时从no_pair_num中取元素，验证和，根据结果决定下一步
        且，对no_pair_num没有任何要求，可以有重复元素，也可以是无序的
        且，再递归过程中还可根据需要在特定层中传入不同的no_pair_num，可扩展性强

        这个函数另一个奇特之处在于，它没有返回值，一般常规的递归函数都会有返回值，而这个函数是通过在递归过程中不断修改temp来达成目的，
        且，一般常见的递归是将复杂的过程简单化，层层向下直至最简形式，而这个函数的操作，真的很6，有点难以系统性地描述

        这个函数的整体结构设计真的太巧妙了，值得认真学习

        要思考得出这样的结构有2点，首先递归就是干重复的（不便于用for循环来干的）事情，而在这个场景中，重复的事情有哪些呢？
        有判断sum(temp)和14的大小关系，这是最先想到的，其次，从no_pair_num中取元素，要想办法在一次递归中取到所有元素，
        那递归的过程对应的是什么呢？对应的是temp的变化，即一次递归过程对应于temp中指定位置对no_pair_num元素的遍历，
        这个指定位置很容易局限我们的思想，因为总是下意识的想要拿到这个索引，但其实这个索引我们并不需要，
        如下面的程序所示，把它交给程序自然处理就好

        这个函数我虽然完全看懂了，但假如在不知道的情况下，让我来写，感觉我还是很难写出，所以是我还没完全通透？？

        :return:
        """
        if sum(temp) > 14:
            return
        if sum(temp) == 14:
            res.append(temp.copy())
            return
        for i in no_pair_num:
            temp.append(i)
            # print(temp)
            func(no_pair_num, res, temp)
            temp.pop()
        return

    res = []
    for i in pair_num:
        temp = [i]
        func(no_pair_num, res, temp)
    res = [sorted(x) for x in res if len(x) <= 4]
    res = [tuple(x) for x in res]
    res = set(res)
    print(len(res))
    print(res)
    return res


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
    num_combs()

    # number()
    # main()

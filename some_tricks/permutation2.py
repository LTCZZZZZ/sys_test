# 密码排列，即允许重复
# from scipy.special import comb, perm
import timeit
import math
import itertools


def func1(string, r=None):
    # 重复计算了相同的结果多次，不好
    l = len(string)
    if r is None or r > l:
        r = l

    def permu(string, r):
        # print(string, r)
        l = len(string)

        if r == 1:
            # print(list(string))
            return list(string)
        else:
            res = []
            for i in range(l):
                # print(string, i)
                first = string[i]
                res.extend([first + item for item in permu(string, r - 1)])
            return res

    res = permu(string, r)
    print(len(res) == math.pow(l, r))  # 验证结果是否正确
    return res


# print(func1('ABCD', 3))
# print(func2('ABCD', 3))

# 在func本身需执行的排列较简单时，由于func1结构更简单，所以它更快，但复杂时，如下，则func2更快
# 且随着复杂程度的增加，func2的性能优势更能显现
# t1 = timeit.Timer("func1('ABCDEFGHIJKL', 8)", "from __main__ import func1")
# print(t1.timeit(1))
# t1 = timeit.Timer("func2('ABCDEFGHIJKL', 8)", "from __main__ import func2")
# print(t1.timeit(1))

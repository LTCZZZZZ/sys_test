# 排列组合算法
from scipy.special import comb, perm
import timeit


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
                other = string[:i] + string[i + 1:]
                res.extend([first + item for item in permu(other, r - 1)])
            return res

    res = permu(string, r)
    # print(len(res) == perm(l, r, True))  # 验证结果是否正确
    return res


def func2(string, r=None):
    # 将之前的结果记录下来
    l = len(string)
    if r is None or r > l:
        r = l
    res_dict = {}
    Δ = l - r
    # 显而易见的，在permu的各级递归中，Δ=l-r 均为定值，都等于最外层的Δ，
    # 所以res_dict中可以只记录string，而不记录r，
    # 也就是说如果string确定的情况下，其实r已经随之确定了
    # 下面这么写程序可能有些难以理解，但确实是最优的方式

    def permu(string):
        # 先查询结果字典
        if string in res_dict:
            return res_dict[string]

        l = len(string)
        r = l - Δ
        # print(string, r)

        if r == 1:
            # print(list(string))
            res = list(string)
        else:
            res = []
            for i in range(l):
                # print(string, i)
                first = string[i]
                other = string[:i] + string[i + 1:]
                res.extend([first + item for item in permu(other)])

        # 将结果存起来，因为外层是字典故而这里不需要使用nonlocal关键字
        res_dict[string] = res
        return res

    res = permu(string)
    # print(len(res) == perm(l, r, True))  # 验证结果是否正确
    return res



# print(func1('ABCD', 3))
# print(func2('ABCD', 3))

# 在func本身需执行的排列较简单时，由于func1结构更简单，所以它更快，但复杂时，如下，则func2更快
# 且随着复杂程度的增加，func2的性能优势更能显现
t1 = timeit.Timer("func1('ABCDEFGHIJKL', 8)", "from __main__ import func1")
print(t1.timeit(1))
t1 = timeit.Timer("func2('ABCDEFGHIJKL', 8)", "from __main__ import func2")
print(t1.timeit(1))

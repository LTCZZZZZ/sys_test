# 手动实现product函数
# 笛卡尔积，密码生成
from itertools import product

# rowlists = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# for combination in itertools.product(*rowlists):  # 注意这里的传参，是*传进去的
#     print(combination)


def prod(*args, repeat=1):
    """
    手动实现product函数
    :param args: 传入的列表
    :param repeat: 重复次数
    :return:
    """
    pools = [tuple(pool) for pool in args] * repeat
    # print(pools)
    result = [[]]
    for pool in pools:
        # 真的太简洁了，就一行代码
        result = [x + [y] for x in result for y in pool]
        # print(result)
    for v in result:
        yield tuple(v)


if __name__ == '__main__':
    row = [1, 2]
    # temp = product(row, row, row)
    temp = product(row, repeat=3)
    print(list(temp))
    temp = prod(row, repeat=3)
    print(list(temp))
    assert list(prod(row, repeat=3)) == list(prod(row, row, row)) == list(product(row, repeat=3))

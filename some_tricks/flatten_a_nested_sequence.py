# Example of flattening a nested sequence using subgenerators
# 生成器、迭代器、yield from 的进一步应用

from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    """
    递归展开嵌套的序列，这部分代码真的很优雅
    :param items:
    :param ignore_types: 不进一步展开的数据类型
    :return:
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


if __name__ == '__main__':

    items = [1, 2, [3, 4, [5, 6], 7], 8]

    # Produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)

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


def flatten2(items, ignore_types=(str, bytes)):
    """
    不用生成器，常规的版本
    :param items:
    :param ignore_types: 不进一步展开的数据类型
    :return:
    """
    l = []
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            l.extend(flatten2(x))
        else:
            l.append(x)
    return l


if __name__ == '__main__':
    """
    flatten和flatten2的差别：flatten有点像一个流水线机器，使用for循环迭代时，每次吐出一个元素，内存占用是很小的，
    与之相比，flatten2的递归，首先会有最外层的一个存储l，每次向下递归时，都会有一个新的l，要存储全部的元素，这样内存占用就会很大，
    在处理超大量数据时，生成器版本的flatten会有极大的优势
    """

    items = [1, 2, [3, 4, [5, 6], 7], 8]

    print(flatten2(items))
    # Produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    print(flatten2(items))
    for x in flatten(items):
        print(x)

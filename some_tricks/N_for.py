# python的N个嵌套for循环

# letters 是一个字符数组 ['a','b','c','d'] 并且 transitions 是一个字典 {'a':['b','c'],'b':['a'],'c':['d'],'d':['b' ,'c','d']
# 对于 n = 4，


def func1(letters, transitions, n):
    for x in letters:
        for k1 in transitions[x]:
            for k2 in transitions[k1]:
                for k3 in transitions[k2]:
                    word = ""
                    word = x + k1 + k2 + k3
                    print(word)


def generate_strings(letters, transitions, n):
    """
    生成器
    yield from iterable本质上等于 for item in iterable: yield item
    """
    def helper(s):
        if len(s) == n:
            yield s
        elif len(s) < n:
            for letter in transitions[s[-1]]:
                yield from helper(s + letter)

    for letter in letters:
        yield from helper(letter)


def func2(letters, transitions, n):
    for s in generate_strings(letters, transitions, n):
        print(s)


def recursion(strings, transitions, n):
    """
    （常见）递归法
    这里最初层是['a','b','c','d']，每一层递归相当于依次取出其中的元素，向后扩展字符串

    但这个方法是有明显劣势的，首先内存占用更大，然后，假如生成的结果是会被用于for循环遍历，且通过条件判断break退出时，
    因为在这种场景下，generate_strings生成器版本不用得出所有的结果，而recursion需要将所有的结果都先生成出来，
    假使break的位置是均匀分布的，那也直接节约了50%的时间以及大量内存，数据量越大内存节省越多
    """
    if n == 1:
        return strings

    res = []
    for s in strings:
        inner = recursion(transitions[s[-1]], transitions, n - 1)
        res.extend([s + v for v in inner])

    return res


if __name__ == '__main__':
    letters = 'abcd'
    transitions = {'a': 'bc', 'b': 'a', 'c': 'd', 'd': 'bcd'}
    # func1(letters, transitions, 4)
    # print('------------------')

    # func2(letters, transitions, 4)

    print(list(generate_strings(letters, transitions, 4)))
    print('------------------')

    print(recursion(letters, transitions, 4))

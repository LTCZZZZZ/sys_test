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


if __name__ == '__main__':
    letters = 'abcd'
    transitions = {'a': 'bc', 'b': 'a', 'c': 'd', 'd': 'bcd'}
    func1(letters, transitions, 4)
    print('------------------')

    func2(letters, transitions, 4)

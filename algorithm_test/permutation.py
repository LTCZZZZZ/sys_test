def permutations(chars: list, i: int = 0):
    """
    这个函数太妖了，真的，太妖了。我感觉它强行把简单的事情复杂化了。
    用递归的思路去想：每个permutations只负责打印满足要求的字符串，然后递归调用，会好理解一点。
    :param chars: characters to permute
    :param i: starting index of subarray of characters to permute. (default: (0))
    :return:
    """
    chars_len = len(chars)
    print(f"i: {i}")  # 这里面有个细节，当i >= chars_len时，下面的任何操作都不会执行，相当于递归会在此处终止。
    if i == chars_len - 1:
        print(f'result: {chars}')
    # 在每个for循环开始时，先交换位置，再执行递归，最后交换回来，每个完整的递归过程(无论深度)都不会改变chars。
    # 整个for循环的过程相当于，依次把chars[i]和从chars[i]往后的字符(包括它自己)交换位置，执行permutations。
    # 如果chars = ['a', 'b', 'c']，以i=0为例，每个for循环的过程就是：
    # 1. swap(chars, 0, 0)
    # 1. 此时chars = ['a', 'b', 'c']，permutations(chars, 1)打印abc，acb
    # 1. swap(chars, 0, 0)
    # 2. swap(chars, 0, 1)
    # 2. 此时chars = ['b', 'a', 'c']，permutations(chars, 1)打印bac，bca
    # 2. swap(chars, 0, 1)
    # 3. swap(chars, 0, 2)
    # 3. 此时chars = ['c', 'b', 'a']，permutations(chars, 1)打印cba，cab
    # 3. swap(chars, 0, 2)
    for j in range(i, chars_len):
        chars[i], chars[j] = chars[j], chars[i]
        print('pos1:', chars, i, j)
        # Missing Line Here
        permutations(chars, i + 1)
        print('pos2:', chars, i, j)
        chars[i], chars[j] = chars[j], chars[i]
        print('pos3:', chars)
    print(f"i: {i} end")


if __name__ == '__main__':
    permutations(['a', 'b', 'c'])
    # permutations(['a', 'b', 'c'], 1)

# 参考 https://haseebq.com/what-explains-the-rise-of-amms/
# uniswap交易方法


def get_input_price(output_amount, input_reserve, output_reserve):
    """
    输入币种A
    输出币种B
    即池内A币种数量增加，B币种数量减少，但需保持A币种数量* B币种数量不变，此时计算B以A计价的单价
    :param output_amount: 输出的币种数量
    :param input_reserve: 输入币种的储备量
    :param output_reserve: 输出币种的储备量
    :return: 输出币种B以输入币种A计价的单价
    """
    numerator = input_reserve * output_reserve
    input_amount = numerator / (output_reserve - output_amount) - input_reserve
    # -10表示在右边补空格，总宽10位，.10表示截取10位（是先截取，再执行补位操作，位数超过指定位数的，按超过显示）
    # 这打印的是对应于想购买B数量，池中当前A币种数量，池中当前B币种数量，此时B币种以A币种计价的单价
    print('%4s %-10.10s, %-10.10s, %-10.10s' % (output_amount, input_reserve, output_reserve, input_amount / output_amount))
    return input_amount / output_amount


def compare(n, input_reserve, output_reserve):
    """
    考虑买入n单位币种A时，一次性买入和连续单次买入是否有差别
    :param n: 买入币种A的数量
    :return:
    """
    # 一次性买入花费总价
    total1 = get_input_price(n, input_reserve, output_reserve) * n
    print(f'total1: {total1}')
    # 连续单次买入花费总价
    total2 = 0
    numerator = input_reserve * output_reserve
    for i in range(n):
        total2 += get_input_price(1, numerator / (output_reserve - i), output_reserve - i)
    print(f'total2: {total2}')

    # 结果表明，一次性买入和连续单次买入的成本是一样的，但一般来说一次性买入的手续费更低

    # 很显然，由于numerator是常数，所以思考可知：对只有双方的交易来说，只要结果固定，则交易成本也随之确定，和交易过程的次数无关
    # 现实世界中显然会有多方参与，所以此结论一般不适用


if __name__ == '__main__':
    # print(get_input_price(1, 50, 50))

    compare(2, 50, 50)
    compare(10, 50, 50)

    compare(2, 40, 60)
    compare(20, 40, 60)  # 交易完后池子变为 (60, 40)

    compare(2, 60, 40)
    compare(20, 60, 40)  # 交易完后池子变为 (120, 20)

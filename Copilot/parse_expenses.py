# Copilot中文测试
import datetime


def parse_expenses(expenses_string):
    """
    解析费用列表并返回元组 (date, value, currency)的列表
    忽略以#开头的行
    将date转为timestamp并取整
    Example expenses_string:
        2016-01-02 -34.01 USD
        2016-01-03 2.59 DKK
        2016-01-03 -2.72 EUR
    """
    expenses = []
    for line in expenses_string.splitlines():
        if line.startswith('#'):
            continue
        date, value, currency = line.split()
        date = int(datetime.datetime.strptime(date, '%Y-%m-%d').timestamp())
        expenses.append((date, float(value), currency))
    return expenses


if __name__ == '__main__':
    res = parse_expenses('''2016-01-02 -34.01 USD
        2016-01-03 2.59 DKK
        2016-01-03 -2.72 EUR''')
    print(res)

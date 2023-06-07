# 银狼2星魂等效提升，不考虑由于基础概率导致的实战溢出值，但要去掉提升溢出hit_rate的部分
import numpy as np
import matplotlib.pyplot as plt


def equivalent(hit_rate=1, resist_rate=0.3, reduce=0.2):
    """
    这是一个可用于np.ndarray的函数
    计算效果命中等效提升
    :param hit_rate: 效果命中
    :param resist_rate: 效果抵抗
    :param reduce: 效果抵抗降低
    :return:
    """
    actual_hit_rate = (1 + hit_rate) * (1 - resist_rate)
    arise = (1 + hit_rate) - actual_hit_rate / (1 - resist_rate + reduce)
    # print(type(arise))

    # 去掉提升溢出hit_rate的部分
    # if isinstance(arise, np.ndarray):
    #     res = np.minimum(arise, hit_rate)
    # else:
    #     res = min(arise, hit_rate)
    res = np.minimum(arise, hit_rate)

    print(arise, res)
    return res


def draw():
    x_list = np.arange(0, 1.1, 0.1)
    y_list_1 = equivalent(1, x_list)
    y_list_08 = equivalent(0.8, x_list)
    y_list_12 = equivalent(1.2, x_list)
    # 画图
    plt.plot(x_list, y_list_1, label='hit_rate=1')
    plt.plot(x_list, y_list_08, label='hit_rate=0.8')
    plt.plot(x_list, y_list_12, label='hit_rate=1.2')
    plt.legend()  # 显示图例
    plt.xlabel('resist_rate')
    plt.ylabel('arise')
    plt.show()

    # 从图中可以看出，原hit_rate越大，等效提升越大，从计算式可知，提升和(1+hit_rate)成正比；
    # 此外，resist_rate越大，等效提升越大，形状应是反比例函数的形状


if __name__ == '__main__':
    equivalent(1, 0.3)
    equivalent(1, 0.4)
    equivalent(1, 0.5)
    # equivalent(1, 0.9)
    print('------------------')

    equivalent(0.8, 0.3)
    equivalent(0.8, 0.4)
    equivalent(0.8, 0.5)
    print('------------------')
    equivalent(1.2, 0.3)
    equivalent(1.2, 0.4)
    equivalent(1.2, 0.5)
    print('------------------')
    equivalent(1.35, 0.3)
    equivalent(1.35, 0.4)
    equivalent(1.35, 0.5)

    draw()

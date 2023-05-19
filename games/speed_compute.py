# 配速计算

def func(c1, c2, v1=0, v2=0, p1=0.0, p2=0.0):
    """
    :param c1: 主C跑圈数
    :param c2: 辅助跑圈数
    :param v1: 主C速度
    :param v2: 辅助速度
    :param p1: 主C行动提前百分比（相对于跑道长度）
    :param p2: 辅助行动提前百分比（相对于跑道长度）
    v1 != 0则计算v2，v2应该小于计算出的阈值
    v2 != 0则计算v1，v1应该大于计算出的阈值
    """
    d0 = 10000  # 跑道长度，常数
    if v1 == 0:
        # 路程除以时间，常数d0可以约掉
        v1 = (c1 - p1) / ((c2 - p2) / v2)
        print(v1)
        return v1
    elif v2 == 0:
        v2 = (c2 - p2) / ((c1 - p1) / v1)
        print(v2)
        return v2


if __name__ == '__main__':
    func(3, 2, v1=180, p1=0, p2=0.15)
    func(3, 2, v1=180, p1=0, p2=0.3)  # 每2轮一次拉条，满级天赋
    func(3, 2, v2=110, p1=0, p2=0.3)

import time
# import numpy as np


class Timer:  # @save
    """记录多次运行时间。"""

    def __init__(self):
        self.times = []
        self.start()

    def start(self):
        """启动计时器。"""
        self.tik = time.time()

    def record(self):
        """打点记录时间。不停歇，self.times列表中记录每一段时间的时长。"""
        self.times.append(time.time() - self.tik)
        if len(self.times) == 1:
            return self.times[-1]
        else:
            return self.times[-1] - self.times[-2]

    def stop(self):
        """停止计时器并将时间记录在列表中。record记录分段时长，stop记录累计时长。"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    # 下面这三个函数和record冲突
    # def avg(self):
    #     """返回平均时间。"""
    #     return sum(self.times) / len(self.times)
    #
    # def sum(self):
    #     """返回时间总和。"""
    #     return sum(self.times)
    #
    # def cumsum(self):
    #     """返回累计时间。"""
    #     return np.array(self.times).cumsum().tolist()

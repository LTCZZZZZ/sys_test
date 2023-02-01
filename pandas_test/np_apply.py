# axis=m的意思是，在取元素时，每次固定非m轴，然后遍历第m轴得到的元素作为一个组，记为x(m轴除外后的shape相乘为组的数量)，
# 再将func(x)得到的结果放到原m轴的位置，拼起来，结果的shape是原shape将m轴替换为func(x)的shape后的shape
# 如果func(x)为标量，则shape为原shape去掉m轴
import numpy as np


def func(x):
    # 注意到，axis=0时，一共有3*4=12个x，每个x包含的数据是a的第0维依次取出来的
    print(x)
    # return x[0]      # 标量，即()，res的shape为(3,4)
    # return x         # (2, )，res的shape为(2,3,4)
    return [x, x + 1]  # (2,2)，res的shape为(2,2,3,4)


a = np.arange(24).reshape((2, 3, 4))
a[0,:2,:2] = np.zeros(shape=(2, 2))  # 区块赋值

print(a)
print('___________________')
res = np.apply_along_axis(func, axis=0, arr=a)
print('___________________')
print(res)
print(res.shape)

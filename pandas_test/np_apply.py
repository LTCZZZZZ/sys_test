import numpy as np


def func(x):
    # 注意到，axis=0时，一共有3*4=12个x，每个x包含的数据是a的第0维依次取出来的
    print(x)
    return x[0]


a = np.arange(24).reshape((2, 3, 4))

print(a)
print('___________________')
res = np.apply_along_axis(func, axis=0, arr=a)
print('___________________')
print(res)

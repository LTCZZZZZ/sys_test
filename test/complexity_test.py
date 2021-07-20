# 列表list和字典dict的(空间)时间复杂度测试

# 结论：list构建起来比dict快得多，并且，应该是数据量越大这个差别越大
# 而list的in操作比dict慢得多，同样的，数据量越大此差别越大
# 其次，python内部应该是对range的in操作做了优化，如果l不加list，则执行非常快

# 在Python中dict在发生哈希冲突时采用的开放寻址法，而java的HashMap采用的是链地址法。

# 另外，参见 https://zhuanlan.zhihu.com/p/273666774

import time

time0 = time.time()
# l = range(0, 10 ** 8, 2)
l = list(range(10 ** 8))
time1 = time.time()
print(99999999 in l)  # 大约需要1s
time2 = time.time()

print(time0)
print(time1)
print(time2)


time0 = time.time()
d = {i: i for i in range(10 ** 8)}
time1 = time.time()
print(99999999 in d)  # 只需要0.00002s
time2 = time.time()

print(time0)
print(time1)
print(time2)

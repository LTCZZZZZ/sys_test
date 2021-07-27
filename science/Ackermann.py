# Ackermann函数定义如下：　若m=0，返回n+1。
# 若m>0且n=0，返回Ackermann(m-1,1)。
# 若m>0且n>0，返回Ackermann(m-1,Ackermann(m,n-1))。
from functools import lru_cache
import sys

sys.setrecursionlimit(32780)
# 32779会挂，Ackermann(4, 1)递归深度为32780


@lru_cache(maxsize=10000)
def Ackermann(m, n):
    """m, n必须为自然数"""
    # print(m, n)
    if m == 0:
        return n + 1
    else:
        if n == 0:
            return Ackermann(m - 1, 1)
        else:
            return Ackermann(m - 1, Ackermann(m, n - 1))


print(Ackermann(4, 0))
print(Ackermann(4, 1))  # 不设置递归深度，就挂了，递归深度10000竟还不够，这里实际递归深度是32780
print(Ackermann(3, 3))

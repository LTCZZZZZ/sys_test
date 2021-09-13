import numpy as np
import os
import time

# a = 7
# b = a >> 2

def bit(a, b):
    '''显示a二进制表示从右往左起第b位的数字'''
    return (a >> (b - 1)) & 1

# print(bit(6, 1))

a = iter('1234')
for i in a:
    print(i)


# try:
#     1 / 0
# except:
#     # 会先执行finally，最后才raise
#     raise
# finally:
#     time.sleep(3)
#     print('end')


i = 5
for i in range(10):
    print(i)
print(i)

l = [1, 2]
l.extend()

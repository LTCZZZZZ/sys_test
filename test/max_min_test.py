from tools import Timer

timer = Timer()
timer.start()

# 2.650378 sec
a = range(1000000)
for k in range(100):
    print(max(a))

# 5.811684 sec，在Go那边运行，带上生成的代码，居然才要0.190279 sec，
# 不带生成的代码，只需要0.061451 sec，也就是说快了94倍左右
# Go数据类型改为int32还能更快，0.057557s
# a = range(1000000, 0, -1)
# for k in range(100):
#     big = 0
#     for i in a:
#         if i > big:
#             big = i
#     print(big)

print(f'{timer.stop():.6f} sec')

# 事实说明：max比自己的for循环快一倍左右

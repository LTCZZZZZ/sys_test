# 参见 https://blog.csdn.net/qq_27825451/article/details/82967904
from matplotlib import patches
import matplotlib.pyplot as plt

# 绘制一个椭圆需要制定椭圆的中心，椭圆的长和高
xcenter, ycenter = 1, 1
width, height = 0.8, 0.5
angle = -30  # 椭圆的旋转角度

# 第一步：创建绘图对象
fig = plt.figure()
ax = fig.add_subplot(211, aspect='auto')
ax.set_xbound(-1, 3)
ax.set_ybound(-1, 3)

# 第二步
e1 = patches.Ellipse((xcenter, ycenter), width, height,
                     angle=angle, linewidth=2, fill=False, zorder=2)

# 第三步
ax.add_patch(e1)

# 第一步
ax = fig.add_subplot(212, aspect='equal')
ax.set_xbound(-1, 3)
ax.set_ybound(-1, 3)

# 第二步
e2 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, fill=False, zorder=2)

# 第三步
ax.add_patch(e2)

plt.show()

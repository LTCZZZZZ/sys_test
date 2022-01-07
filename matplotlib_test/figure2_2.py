# 使用集合添加对象
from matplotlib import patches
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

# 绘制一个椭圆需要制定椭圆的中心，椭圆的长和高
xcenter, ycenter = 1, 1
width, height = 0.8, 0.5
angle = -30  # 椭圆的旋转角度

fig = plt.figure()
ax = fig.add_subplot(111, aspect='auto')
# ax.set_xbound(-1, 3)
# ax.set_ybound(-1, 3)
ax.axis([-1, 3.5, -1, 3.5])

e1 = patches.Ellipse((0, 0), width, height,
                     angle=angle, linewidth=2, fill=False, zorder=2)

e2 = patches.Arc((2, 2), width=3, height=2,
                 angle=angle, linewidth=2, fill=False, zorder=2)

patches = []
patches.append(e1)
patches.append(e2)
collection = PatchCollection(patches)
ax.add_collection(collection)

plt.show()

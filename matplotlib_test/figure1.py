# 参见 https://blog.csdn.net/qq_27825451/article/details/102457049
from matplotlib import gridspec, pyplot as plt
import numpy as np

plt.rcParams['font.family'] = ['STXingkai']  # 此字体显示负号不正常，需搭配下面的设置
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# plt.rcParams['font.family']=['STKaiti']  # 此字体能自动显示负号

f = plt.figure(num=2, figsize=(16, 12), dpi=80, facecolor="pink", edgecolor='green', frameon=True)
f.suptitle('总标题', fontsize=40, color='#0099ff')
# print(plt.setp(f))  # 使用该方法可以查看到底有多少参数可以设置，分别是哪一些

# 前两个参数表示图形的总行列数，第三个参数表示图形的位置
fig1 = plt.subplot(1, 2, 1)  # 借助plt创建
fig2 = f.add_subplot(3, 5, 9)  # 借助总图所返回的f对象

# # [x,y,width,height]，下面的四个值都是“相对取值”，在0~1之间，
# # 前面两个是以左下角作为基准的，后面两个数字指的是相对于整个figure对象的宽度和高度。
# fig3 = f.add_axes([0.1, 0.1, 0.5, 0.5], facecolor='grey')
# fig4 = plt.axes([0.2, 0.2, 0.4, 0.4], facecolor='green')

# 还可以借助gridspec()
# G = gridspec.GridSpec(3, 3)
# fig1 = f.add_subplot(G[0, :], facecolor='red')
# fig2 = f.add_subplot(G[1, 0:2], facecolor='pink')
# fig2 = f.add_subplot(G[1, 2], facecolor='blue')
# fig2 = f.add_subplot(G[2, 0], facecolor='grey')
# fig2 = f.add_subplot(G[2, 1:3], facecolor='green')

# （1）显示范围：
# fig1.axis([xmin, xmax, ymin, ymax])
# plt.axis([xmin, xmax, ymin, ymax])

# (2)分别设置x,y轴的显示范围：
fig1.set_xlim(2, 4)
fig1.set_ylim(2, 4)
plt.xlim(2, 4)
plt.ylim(2, 4)

# (3)设置刻度：
#  这两种方法只能设置数字刻度
fig1.set_yticks([-1, -1 / 2, 0, 1 / 2, 1])
fig1.xaxis.set_ticks([1, 2, 3, 4, 5, 6, 7, 8])  # 先获取x轴

# 这种方法可以将对应的数字用字符串替代出来，xx-large表示XXL，是一种字体相对大小
plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           ['aaa', 'bbb', 'ccc', 'ddd', 'eee'],
           fontsize='xx-large')

# 若要显示π、α等一些特殊的数学符号，则可以通过以下来完成
fig1.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                ['$0$', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'], fontsize='xx-large')
# ——该方法称之为LaTeX语法

# （4）坐标轴的显示和移动
# 默认坐标轴有四条，上下左右。
# （a）坐标轴不显示
zuobiao_zhou = plt.gca()  # 获得坐标轴句柄,这是一种方式
zuobiao_zhou.spines['top'].set_color('none')
zuobiao_zhou_01 = fig1.axes  # 获得坐标轴对象，这是另一种方式
zuobiao_zhou_01.spines['right'].set_color('none')
#
# （b）设置刻度是显示在哪一条坐标轴旁边
zuobiao_zhou_01.yaxis.set_ticks_position('right')
zuobiao_zhou.xaxis.set_ticks_position('top')

# (5)设置主要-次要坐标轴
fig1 = f.add_subplot(1, 2, 2)
# plot返回一个列表，通过line,获取其第一个元素
line1, = plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], marker='>', label='第一条直线')
# 主坐标系
plt.title('两条直线综合', size=30)  # 标题
fig1.legend(loc=9)  # 图例的位置，取值范围0-10
# loc: 表示图例显示的位置
'''===============   =============
    Location String   Location Code
   ===============   =============
    'best'            0
    'upper right'     1
    'upper left'      2
    'lower left'      3
    'lower right'     4
    'right'           5
    'center left'     6
    'center right'    7
    'lower center'    8
    'upper center'    9
    'center'          10
'''
fig1.set_xlabel('横坐标', size=30)  # 设置坐标
fig1.set_ylabel('纵坐标一', size=30)
# 次坐标系
fig2 = fig1.twinx()  # 双胞胎，就是设置次坐标轴
line2, = plt.plot([1, 2, 3, 4, 5], [6, 6.5, 7.5, 9, 10.5], label='第二条直线')
fig2.legend(loc=1)
fig2.set_ylabel('纵坐标二', size=30)
plt.grid()  # 网格

# 2.2.2 与图像线条相关的设置
# （1）关闭抗锯齿
line1.set_antialiased(False)

# （2）线条样式的各种设置——四种设置方法
x = range(1, 6)
y = range(3, 18, 3)
# 方法一：直接在画线的时候通过“字符串参数”加以指定
line1, = fig1.plot(x, y, 'r-')  # 简单设置可以这样使用

# 方法二：直接在划线的时候通过参数指定，如下：
line1, = fig1.plot(x, y, color='red', linewidth=3, linestyle='--')

# 方法三：通过line.set_xxxx()的方式加以设置，如下：
line1.set_color('black')
line1.set_linestyle('-')
line1.set_alpha(0.3)
line1.set_linewidth(8)

# 方法四：通过plt.setp(line,xxxxxxxxx)方法去设置
plt.setp(line1, color='black', linewidth=8, linestyle='-', alpha=0.3)

'''推荐使用二三四种方法。
注意，设置线条样式的属性非常的多，我们可以通过以下方式加以查看'''
print(plt.setp(line1))  # 会显示到底有哪些属性可以设置

# （3）下面是常见的属性设置：
# 参见官方文档 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html?#matplotlib.pyplot.plot
'''常见的颜色：——除了使用字母，还可以使用十六进制的字符串表示，比如“#008000”，这样任意一种颜色均可以使用了。
        ``'b'``          blue
        ``'g'``          green
        ``'r'``          red
        ``'c'``          cyan（青色）
        ``'m'``          magenta（品红）
        ``'y'``          yellow
        ``'k'``          black
        ``'w'``          white
常见的线型：
        ``'-'``          solid line style
        ``'--'``         dashed line style
        ``'-.'``         dash-dot line style
        ``':'``          dotted line style
常见的点标记marker：
 '.'       point marker
','       pixel marker
'o'       circle marker
'v'       triangle_down marker
'^'       triangle_up marker
'<'       triangle_leftmarker
'>'       triangle_rightmarker
'1'       tri_down marker
'2'       tri_up marker
'3'       tri_left marker
'4'       tri_right marker
's'       square marker
'p'       pentagon marker
'*'       star marker
'h'       hexagon1 marker
'H'       hexagon2 marker
'+'       plus marker
'x'       x marker
'D'       diamond marker
'd'       thin_diamond marker
'|'       vline marker
'_'      hline
'''

f.show()

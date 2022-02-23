import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

print(matplotlib.matplotlib_fname())
print(matplotlib.get_backend())    # 返回matplotlib的后端
print(matplotlib.get_cachedir())   # 缓存文件夹，添加新字体时需要手动清除缓存
print(matplotlib.get_configdir())  # 配置文件夹
print(matplotlib.get_data_path())  # 数据路径
# 查看全局可用字体
a = sorted([f.name for f in fm.fontManager.ttflist])
for i in a:
    print(i)

# 这是在需要多种字体混合使用时，各个单独设置的方法
# f = plt.figure(num=2, figsize=(16, 12), dpi=80, facecolor="pink", edgecolor='green', frameon=True)
# # font = fm.FontProperties(fname='/Library/Fonts/STXINGKA.TTF')
# # f.suptitle('总标题abcdef', fontproperties=font, fontsize=48, color='#0099FF')
# # 当字体列表更新后，可以直接设置字体，不用再通过font了
# f.suptitle('总标题abcdef', font='STXingkai', fontsize=48, color='#0099FF')
# f.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, hspace=0.2, wspace=0.2)
# f.show()

# 全局设置字体的方法，设置有中文的字体以正常显示中文
print(plt.rcParams['font.family'])
plt.rcParams['font.family'] = ['STXingkai']  # 此字体显示负号不正常，需搭配下面的设置
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# plt.rcParams['font.family']=['STKaiti']  # 此字体能自动显示负号
print(plt.rcParams['font.family'])
f = plt.figure()
f.suptitle('总标题abcdef', fontsize=48, color='#0099FF')
f.show()

# 另外可能的设置参考
# plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
# plt.rcParams['font.size'] = 12  # 字体大小
# plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 下面这一堆是github copilot生成的，未经过验证
# plt.rcParams['axes.facecolor'] = '#E6E6FA'  # 设置背景颜色
# plt.rcParams['axes.edgecolor'] = '#000000'  # 设置边框颜色
# plt.rcParams['axes.linewidth'] = 1.5  # 设置边框宽度
# plt.rcParams['axes.grid'] = True  # 设置网格
# plt.rcParams['axes.titlesize'] = 'large'  # 设置标题字体大小
# plt.rcParams['axes.titleweight'] = 'bold'  # 设置标题字体加粗
# plt.rcParams['axes.titlepad'] = 5  # 设置标题和坐标轴之间的距离
# plt.rcParams['axes.labelweight'] = 'bold'  # 设置坐标轴标签字体加粗
# plt.rcParams['axes.labelsize'] = 'large'  # 设置坐标轴标签字体大小
# plt.rcParams['axes.labelpad'] = 5  # 设置坐标轴标签和坐标轴之间的距离
# plt.rcParams['axes.linewidth'] = 1.5  # 设置坐标轴线宽

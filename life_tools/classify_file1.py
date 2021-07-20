import os
import shutil
# import re

dir_name1 = r'C:\Users\hht\Desktop\桌面文件'
dir_name2 = r'C:\Users\hht\Desktop\测试'
os.chdir(dir_name2)
jobs = ['IOS', 'WEB', '安卓', '产品设计', '运营', '教研', '职能', '其他']
channels = ['51JOB', 'BOSS', '猎聘', '智联', '拉勾', '其他']

for job in jobs:
    # 对于不存在的路径，isdir函数也会返回False
    if not os.path.isdir(job):
        os.mkdir(job)
    for channel in channels:
        channel_path = os.path.join(job, channel)
        if not os.path.isdir(channel_path):
            os.mkdir(channel_path)

# files = list(filter(os.path.isfile, os.listdir()))
file_list = []
for root, dirs, files in os.walk(dir_name1):
    # for name in files:
    #     print(os.path.join(root, name))
    # for name in dirs:
    #     print(os.path.join(root, name))
    # print(dirs)
    # print(files)
    for name in files:
        file_list.append((os.path.join(root, name), name))
# print(file_list)


for f_path, f in file_list:
    for job in jobs:
        f = f.upper()
        signal = 0
        if job in ['IOS', 'WEB']:
            if job in f:
                signal = 1
        elif job == '安卓':
            if 'ANDROID' in f:
                signal = 1
        elif job == '产品设计':
            if 'UI' in f or 'UE' in f or 'UX' in f or '交互' in f or '产品' in f or '视觉' in f:
                signal = 1
        elif job == '运营':
            if '运营' in f:
                signal = 1
        elif job == '教研':
            if '编辑' in f or '教研' in f or '课程' in f or '教师' in f or '主管' in f or '总监' in f or '经理' in f or '动画' in f:
                signal = 1
        elif job == '职能':
            if '人力' in f or '财务' in f or 'HR' in f or 'BP' in f or '薪酬' in f or '绩效' in f or '会计' in f:
                signal = 1
        else:
            # 此时job为'其他'
            signal = 1
        if signal:
            for channel in channels:
                if channel in f:
                    channel_path = os.path.join(job, channel)
                    try:
                        shutil.move(f_path, channel_path)
                    except shutil.Error:
                        pass
                    break
            # 注意，这个else子句从属于for
            else:
                channel_path = os.path.join(job, '其他')
                try:
                    shutil.move(f_path, channel_path)
                except shutil.Error:
                    pass
            break


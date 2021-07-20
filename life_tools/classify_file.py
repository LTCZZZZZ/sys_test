# 文件分类测试文件
import os
import shutil
import re

dir_name = '/Users/私有/Chinese/TestProject/FileTest'
os.chdir(dir_name)
names = ['AAA', 'BBB', 'CCC', 'DDD']
for name in names:
    # 对于不存在的路径，isdir函数也会返回False
    if not os.path.isdir(name):
        os.mkdir(name)

files = list(filter(os.path.isfile, os.listdir()))
print(files)
for f in files:
    for name in names:
        if re.search(name, f):
            try:
                shutil.move(f, name)
            except shutil.Error:
                i = 1
                while True:
                    new_f = os.path.join(name, f'{f}_{i}')
                    if not os.path.exists(new_f):
                        shutil.move(f, new_f)
                        break
                    i += 1
            break

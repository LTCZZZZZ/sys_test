import os
import random

dir_name = '/Users/私有/Chinese/TestProject/FileTest'
os.chdir(dir_name)

names = ['AAA', 'BBB', 'CCC', 'DDD']
for name in names:
    for i in range(random.randint(2, 4)):
        # print(os.path.join(dir_name, f'{name}{i}'))
        # 下面这一行解决了权限问题后仍然报错，原因未知，先换一种方法
        # os.mknod(os.path.join(dir_name, f'{name}{i}'))
        os.system(f'touch {name}{i}')


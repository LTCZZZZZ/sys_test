# 读取文件的时间相关信息
import os
import time

# print(os.listdir('./hierarchy'))

# 显示文件的 stat 信息
stinfo = os.stat('hierarchy')
print(stinfo)

# 另一种方法
ctime = os.path.getctime("hierarchy")
print(int(ctime))

# 文件的Change time，ctime 是在写入文件、更改所有者、权限或链接设置时随 Inode 的内容更改而更改的
# 比如chmod命令就会修改文件的ctime
# 修改文件名也会更新ctime
# 只有修改了文件的内容，才会更新mtime
print(f'Change time：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stinfo.st_ctime))}')
print(f'最后访问时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stinfo.st_atime))}')
print(f'最后修改时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stinfo.st_mtime))}')

# ls -lc filename 查看ctime
#
# ls -lu filename 查看atime
#
# ls -l filename 查看mtime

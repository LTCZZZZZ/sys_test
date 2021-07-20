import zipfile
import os
# import sys
import time
from itertools import product
# 获取迭代器长度的代码，但一般不要用。另外，用了之后迭代器里面就空了
# print(sum(1 for _ in product(chars, repeat=3)))

if __name__ == '__main__':
    print(time.time())
    # print(sys.getfilesystemencoding())
    root = '/root/test'
    zip_file_path = os.path.join(root, '测试.zip')
    with zipfile.ZipFile(zip_file_path) as zf:
        # zf.setpassword(b'123')
        chars = '0123456789abcdefghijklmnopqrstuvwxyz.@'
        k = 1
        # 上一轮循环所使用的全部密码（想了想这种方式可能太占内存了，先不用）
        # last_char_list = []
        signal = 0
        while k <= 10:
            print(f'k = {k}')
            # 注意下面的代码，迭代器(或生成器)列表要先建好
            for item in product(chars, repeat=k):
                pwd = ''.join(item).encode('utf8')
                # print(pwd)
                try:
                    zf.extractall(os.path.join(root, '测试3'), pwd=pwd)
                    print(f'password: {pwd}')
                    signal = 1
                    break
                except (RuntimeError, zipfile.BadZipFile):
                    pass
            if signal:
                break
            k += 1

    print(time.time())

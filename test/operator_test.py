# 此文件在Pycharm中运行会报错，可在Pycharm的Terminal中运行
# 后来发现是文件名operator.py和python的原始文件冲突导致的，修改文件名后运行无问题

class new_int(int):

    def __add__(self, other):
        return new_int(int.__add__(self, other) + 1)


a = new_int(1)
b = new_int(2)


c = a + b
print(c)
print(type(c))
print(type(1))

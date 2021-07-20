# 有些重要 > 比较重要
# 链式API，SDK，参见 https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    def __str__(self):
        return self._path

    def users(self, name):
        return Chain(f'{self._path}/users/{name}')

    __repr__ = __str__


print(Chain().status.user.timeline.list)

# 还有些REST API会把参数放到URL中，比如GitHub的API：
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
# Chain().users('michael').repos
# 就可以非常方便地调用API了

# 很简单，加一个users方法就可以了
print(Chain().users('michael').repos)

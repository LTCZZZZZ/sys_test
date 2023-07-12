# 定义一个

a = 0


def func():
    global a
    a += 1


func()
print(__name__, a)

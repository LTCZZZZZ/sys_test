def func1(a, b=0, *args):
    print(a, b, args)


func1(1, 2, 3)
# func1(1, b=2, args=[3])  # 失败的调用

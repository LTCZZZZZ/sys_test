a = b = 0


def func1():
    # global a
    a = 10
    print(a)


def func2():
    global b
    b = 10
    print(b)


func1()
print(a)

func2()
print(b)

import inspect


def func0():
    print(inspect.stack()[0][3])


func0()

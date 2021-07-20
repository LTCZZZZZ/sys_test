from thread_test import handle


def func():
    p = handle(1)
    return p


print(func().age)

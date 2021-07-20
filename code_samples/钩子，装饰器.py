import time
import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        print(func.__name__)
        res = func(*args, **kwargs)
        time.sleep(1)
        print('finished.')
        e = time.time()
        print(e - s)
        return res
    return wrapper


@decorator
def func1():
    for i in range(2):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    print(func1.__name__)
    func1()

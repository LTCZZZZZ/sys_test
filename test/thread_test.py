import threading
from time import sleep


class People(object):

    def __init__(self, age):
        self.age = age

    def age_add(self, n):
        t = threading.Thread(target=func1, args=(self, n))
        t.start()
        return t


def func1(p, n):
    sleep(1)
    p.age += n


# 修改全局变量没有问题
# p1 = People(10)
# # t = p1.age_add(5)
# # # t.join()
# print(p1.age)
# p1.age_add(5).join()
# print(p1.age)

def handle(age):
    p1 = People(age)
    # t = p1.age_add(5)
    # t.join()
    # print(p1.age)
    p1.age_add(6).join()
    # print(p1.age)
    return p1


if __name__ == '__main__':
    print(handle(10).age)
    print('fffffffff')

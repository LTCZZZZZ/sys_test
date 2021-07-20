from typing import List, Dict


class Test:
    def __init__(self, x):
        self.val = x

    def get_val(self):
        return self.val


l = []  # type: List[Test]
d = {}  # type: Dict[int, Test]
for i in range(5):
    l.append(Test(i))
for i in range(5):
    d[i] = Test(i)
for i in l:
    print(i.get_val())
for i in d.values():
    print(i.get_val())

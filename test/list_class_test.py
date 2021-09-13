# python和go相同，切片都是引用类型
s = [[1, 1], [2, 2]]
a = s[0]
a[0] = 5
print(s)

class User:

    def __init__(self, id, age):
        self.id = id
        self.age = age

    def __repr__(self):
        return str((self.id, self.age))


# python和go的不同之处，go的struct是值类型
s = [User(1, 1), User(2, 2)]
a = s[0]
a.id = 5
print(s, s[0])

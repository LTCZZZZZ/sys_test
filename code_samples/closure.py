def getSequenceFail():  # 失效的闭包
    i = 0
    return lambda: i + 1


def getSequence():  # 正确的闭包
    i = 0

    def add_one():
        nonlocal i  # 注意nonlocal关键字
        i += 1
        return i

    return add_one

nextNumber = getSequence()
print(nextNumber())
print(nextNumber())
print(nextNumber())
nextNumber2 = getSequence()
print(nextNumber2())
print(nextNumber())
print(nextNumber2())
print(nextNumber)
print(nextNumber2)

nextNumber = getSequenceFail()
print(nextNumber())
print(nextNumber())
print(nextNumber())
print(nextNumber)

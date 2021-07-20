

try:
    print(1)
    try:
        a = 1 / 0
    except:
        print(2)
        # 如果想继续触发外层的except子句，加一行raise即可
        # raise
except:
    print(3)

print(4)

with open('staging.env') as f:
    a = f.read()
    print(repr(a))


with open('staging_error.env') as f:
    b = f.read()
    print(repr(b))


print(a == b)


# 以 b 的形式读取，可以发现两者内容并不相同
with open('staging.env', 'rb') as f:
    a = f.read()
    print(repr(a))


with open('staging_error.env', 'rb') as f:
    b = f.read()
    print(repr(b))


print(a == b)

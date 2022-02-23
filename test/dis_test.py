# Disassembler of Python byte code into mnemonics
# 汇编码查看工具，以及在局部变量域中执行代码，参见
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p23_executing_code_with_local_side_effects.html

import dis


def a(s):
    loc = locals()
    exec("s = 0")
    print("s =", s)
    s = loc["s"]
    print("s =", s)
    return s + 1


def 这个函数的名字很长(参数的名字也非常长):
    return 参数的名字也非常长 + 1


dis.dis(a)
print(a(1))
dis.dis(这个函数的名字很长)

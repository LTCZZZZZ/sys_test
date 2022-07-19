# 十六进制表示的字符串和常规字符串的相互转换
from binascii import a2b_hex, b2a_hex

hex_s = '546f6e676a692046696e7465636820526573656172636820496e73746974757465'
print(a2b_hex(hex_s).decode())

s = '中文Aabc'
print(s.encode().hex())
print(b2a_hex(s.encode()))  # 这两个结果一样
hex_s = s.encode().hex()

print(a2b_hex(hex_s).decode())

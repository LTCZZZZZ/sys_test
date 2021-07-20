# 笛卡尔积，密码生成
import itertools

# rowlists = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# for combination in itertools.product(*rowlists):  # 注意这里的传参，是*传进去的
#     print(combination)

row = [1, 2]
print(itertools.product(row, repeat=3))

for comb in itertools.product(row, row, row):
    print(comb)

print()

for comb in itertools.product(row, repeat=3):
    print(comb)

# for comb in itertools.product(row):
#     print(comb)
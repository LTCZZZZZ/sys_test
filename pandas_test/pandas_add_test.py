import pandas as pd

df1 = pd.DataFrame([[1, 1, 1], [2, 1, 1], [3, 1, 1]], columns=['ID', 'A', 'B'])
df1.set_index('ID', inplace=True)
print(df1)

df2 = pd.DataFrame([[1, 2, 3], [4, 4, 4]], columns=['ID', 'A', 'B'])
df2.set_index('ID', inplace=True)
print(df2)

print(df1 + df2)
# 看起来下面两个结果相同
print(df1.add(df2, fill_value=0))
print(df2.add(df1, fill_value=0))

import pandas as pd

df = pd.DataFrame([range(6)], index=['a', 'b', 'c', 'd', 'e', 'a'], columns=[0, 1, 1, 2, 2, 2])
print(df)

print(df.index.duplicated())
print(df.index.drop_duplicates())
print(df.loc[df.index.drop_duplicates()])  # 有相同的索引都会取到，结果和df相同
print(df.columns.duplicated())
print(df.columns.drop_duplicates())
print(df[df.columns.drop_duplicates()])  # 有相同的列也都会取到，结果和df相同

# excel = 'test.xlsx'
# with pd.ExcelWriter(excel, mode='w') as writer:
#     df.to_excel(writer, columns=[0, 1, 2], index=True)  # 报错

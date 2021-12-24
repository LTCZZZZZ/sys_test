# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html?highlight=apply#pandas.DataFrame.apply

import numpy as np
import pandas as pd

df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])

print(df.apply(np.sqrt))
print(df.apply(np.sum, axis=0))
print(df.apply(np.sum, axis=1))

print(df.apply(lambda x: [1, 2], axis=1))
print(df.apply(lambda x: [1, 2], axis=1, result_type='expand'))
# print(df.apply(lambda x: 1, axis=1, result_type='expand'))
print(df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1))

print(df.apply(lambda x: [1, 2], axis=1, result_type='broadcast'))
print(df.apply(lambda x: 3, axis=1, result_type='broadcast'))  # 返回标量时，延axis广播

df[['C', 'D']] = df.apply(lambda x: 3, axis=1, result_type='broadcast')
print(df)

# apply的结果的列名被drop了，所以这里index参数可不传
df[['E', 'F']] = df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)
print(df)

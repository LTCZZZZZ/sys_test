import pandas as pd

dfmi = pd.DataFrame([list('abcd'),
                     list('efgh'),
                     list('ijkl'),
                     list('mnop')],
                    columns=pd.MultiIndex.from_product([['one', 'two'],
                                                        ['first', 'second']]))
print(dfmi)

print(dfmi['one']['second'])
print(dfmi.loc[:, ('one', 'second')])
# These both yield the same results, so which should you use? It is instructive to understand
# the order of operations on these and why method 2 (.loc) is much preferred over method 1 (chained []).
# 参考 https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

value = 30

dfmi.loc[:, ('one', 'second')] = value
# becomes
dfmi.loc.__setitem__((slice(None), ('one', 'second')), value)
print(dfmi)
#
dfmi['one']['second'] = value
# # becomes
# dfmi.__getitem__('one').__setitem__('second', value)
print(dfmi)

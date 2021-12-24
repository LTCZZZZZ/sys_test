import pandas as pd
import numpy as np

company = ["A", "B", "C"]

data = pd.DataFrame({
    "company": [company[x] for x in np.random.randint(0, len(company), 10)],
    "salary": np.random.randint(5, 50, 10),
    "age": np.random.randint(15, 50, 10)
})

print(data)
group = data.groupby("company")
print(group)
for i in group:
    print(type(i))
    print(len(i))
    print(type(i[0]), i[0])
    print(type(i[1]), i[1])  # DataFrame类型，还是有用的，，
    # print(i)

# list(group)
m = data.groupby("company").agg('mean')

avg_salary_dict = data.groupby('company')['salary'].mean().to_dict()
data['avg_salary'] = data['company'].map(avg_salary_dict)  # 注意这个map函数，可能会比较常用

data['avg_salary'] = data.groupby('company')['salary'].transform('mean')


# 获取各个公司年龄最大的员工的数据
def get_oldest_staff(x):
    df = x.sort_values(by='age', ascending=True)
    print(type(df.iloc[-1, :]))
    return df.iloc[-1, :]


# 区别在于，对于groupby后的apply，以分组后的子DataFrame作为参数传入指定函数的，基本操作单位是DataFrame，
# 而之前介绍的对dataframe的apply的基本操作单位是dataframe的(按axis取到的)Series
oldest_staff = data.groupby('company', as_index=False).apply(get_oldest_staff)
print(oldest_staff)

# 这样看起来最清晰明了，但会形成MultiIndex
oldest_staff2 = data.groupby('company').apply(lambda x: x.nlargest(1,'age'))
print(oldest_staff2)

# 最后，关于apply的使用，这里有个小建议，虽然说apply拥有更大的灵活性，但apply的运行效率会比agg和transform更慢。
# 所以，groupby之后能用agg和transform解决的问题还是优先使用这两个方法，实在解决不了了才考虑使用apply进行操作。


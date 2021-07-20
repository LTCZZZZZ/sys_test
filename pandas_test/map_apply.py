import pandas as pd
import numpy as np

boolean = [True, False]
gender = ["男", "女"]
color = ["white", "black", "yellow"]
number = 10
data = pd.DataFrame({
    "height": np.random.randint(150, 190, number),
    "weight": np.random.randint(40, 90, number),
    "smoker": [boolean[x] for x in np.random.randint(0, 2, number)],
    "gender": [gender[x] for x in np.random.randint(0, 2, number)],
    "age": np.random.randint(15, 90, number),
    "color": [color[x] for x in np.random.randint(0, len(color), number)]
})


# ①使用字典进行映射
# data["gender"] = data["gender"].map({"男":1, "女":0})

# ②使用函数，传入map的函数只能接收一个参数
def gender_map(x):
    gender = 1 if x == "男" else 0
    return gender


# 注意这里传入的是函数名，不带括号
data["gender"] = data["gender"].map(gender_map)


def apply_age(x, bias):
    return x + bias


# 以元组的方式传入额外的参数
data["age"] = data["age"].apply(apply_age, args=(-3,))

# 沿着0轴求和
data[["height", "weight", "age"]].apply(np.sum, axis=0)

# 沿着0轴取对数
data[["height", "weight", "age"]].apply(np.log, axis=0)


def BMI(series):
    print(type(series))
    weight = series["weight"]
    height = series["height"] / 100
    BMI = weight / height ** 2
    return BMI


data["BMI"] = data.apply(BMI, axis=1)
# 无论axis=0还是axis=1，其传入指定函数的默认形式均为Series，可以通过设置raw=True传入numpy数组
# 但当数据中有混合对象时，raw=True无效

df = pd.DataFrame(
    {
        "A":np.random.randn(5),
        "B":np.random.randn(5),
        "C":np.random.randn(5),
        "D":np.random.randn(5),
        "E":np.random.randn(5),
    })

df.applymap(lambda x:"%.2f" % x)  # applymap会对DataFrame中的每个单元格执行指定函数的操作

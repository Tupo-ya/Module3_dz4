import pandas as pd

obj = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5
}

series = pd.Series(obj, index=[1, 2, 3])
print(series)

#? Объект содержит в себе только эти 3 индекса из словаря


import pandas as pd

arr = [1, 2, 3, 6, 2]

series = pd.Series(arr, index=['a', 'b', 'a', 'c', 'd'])
print(series)


# В случае создания одинаковых индексов, объект нормально создастся
# А при обращении к этим индексам будет выводиться 2 числа

print('\nОдинаковый индекс:')
print(series['a'])

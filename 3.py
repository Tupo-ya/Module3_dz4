import pandas as pd

obj = [i**2 for i in range(1, 21)]

series = pd.Series(obj)
objs = series[series.index % 3 != 0]

objs_ser = pd.Series(objs)
print(objs_ser)
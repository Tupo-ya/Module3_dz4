import pandas as pd

data = pd.read_csv('students.csv')

print(data.head(3))

print()

print(data.tail(2))

print('\n- - - - INFO - - - -\n')

print(data.info())
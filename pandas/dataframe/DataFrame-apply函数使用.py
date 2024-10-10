import pandas as pd
import numpy as np

data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10],'col3': ['value1', 'value2', 'value3', 'value4', 'value5']}


df = pd.DataFrame(data)

#针对每一列进行操作
df['col1_squared'] = df['col1'].apply(lambda col1: col1**2 + 1)

print(df)


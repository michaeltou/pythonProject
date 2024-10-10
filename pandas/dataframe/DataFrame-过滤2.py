import pandas as pd
import numpy as np

# 字典数据
data = {
     'col1': [1, 2, 3, 4, 5],
        'col2': [6, 7, 8, 9, 10],
        'col3': ['value1 ', ' value2', ' value3 ', 'value4 ', 'value5']
      }

# 创建DataFrame
df = pd.DataFrame(data)

condition = (df['col1'] > 3) & (df['col2'] >= 8) & (df['col3'].str.startswith('value'))

condition = (df['col1'] > 3) & (df['col2'] >= 8) & (df['col3'].str.strip().str.startswith('value'))
# 多条件过滤
condition = (df['col1'] > 3) & (df['col3'].str.strip() == 'value4')

df = df[condition]

print(df)






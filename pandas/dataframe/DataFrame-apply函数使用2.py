import pandas as pd
import numpy as np

data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10],'col3': ['value1 ', ' value2', ' value3 ', 'value4', 'value5']}


df = pd.DataFrame(data)

# 去除字符串两端的空格
df['col3_trimed']  = df['col3'].apply(lambda col3: col3.strip())
# 字符串去除空格后，末尾添加'_append'
df['col3_append']  = df['col3'].apply(lambda col3: col3.strip() + '_append')

print(df)


import pandas as pd
import numpy as np

##教程：http://liao.cpython.org/pandas13.html
val = np.arange(10,60).reshape(10,5)

import pandas as pd
import numpy as np
val = np.arange(10, 40).reshape(10, 3)
column = ["column1", "column2", "column3"]
idx = list("ABCDEFGHIJ")
df = pd.DataFrame(val, columns = column, index = idx)
print(df)
print('--------------')
result1 = df["column1"]  # 访问指定列， 返回series
print(result1)

print('--------------')
result1 = df[["column1",'column2']]  # 访问指定多列，  返回dataframe
print(result1)


print('--------------')

result1 = df.loc["A":"C"]  # Q: 如何访问指定行？A: 行标签可以用切片的方式访问，如df.loc["A":"C"]，表示从A到C的行。
print(result1)
print('--------------')
result1 = df.loc["A":"C","column2":"column3"]  # 根据行标签和列标签访问指定多行和多列，  返回dataframe
print(result1)

print('--------------')
result1 = df.iloc[0:1, 0:2]  #
print(result1)


print('----end----------')
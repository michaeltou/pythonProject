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

result1 = df.loc["A"]  # 访问指定行， 返回series
print(result1)
print('--------------')
result1 = df.at["B","column2"]  # 访问指定单元格， 返回value
print(result1)
print('--------------')
result1 = df.iat[1,1]  # 访问指定 单元格， 返回value
print(result1)

print('----end----------')
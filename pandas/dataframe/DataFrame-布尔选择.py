import pandas as pd
import numpy as np

##教程：http://liao.cpython.org/pandas13.html
val = np.arange(10, 60).reshape(10, 5)
col = ["ax", "bx", "cx", "dx", "ex"]
idx = list("abcdefghij")
df1 = pd.DataFrame(val, columns = col, index = idx)
print("dataframe", "*" * 11)
print(df1)
print("*" * 21, "<- dataframe")
bs1 = (df1["bx"] > 30) & (df1["cx"] > 30)  # 数字过滤
#bs2 = (df1["bx"] == 'string-value') & (df1["cx"] > 30) # 字符串过滤

newDf1 = df1[bs1]

print(newDf1)
print("*" * 21, "<- dataframe1")


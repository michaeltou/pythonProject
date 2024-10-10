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

df1["ax"] = df1["ax"]

print('end')

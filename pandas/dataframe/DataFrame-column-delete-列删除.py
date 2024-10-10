import pandas as pd
import numpy as np

##教程：http://liao.cpython.org/pandas13.html
val1 = np.arange(10,40).reshape(10,3)
val2 = np.arange(40,70).reshape(10,3)

col1 = ["ax","bx","cx"]
col2 = ["ay","by","cy"]
idx = list("abcdefghij")

df1 = pd.DataFrame(val1,index=idx,columns=col1)
df2 = pd.DataFrame(val2,index=idx,columns=col2)

print(df1[:3])
print("*"*20, "<------DataFrame")
print(df2[:3])
print("*"*20, "<------DataFrame")

del df1['cx']
print(df1[:3])
print("*"*20, "<------DataFrame")
df3 = df2.pop('by')
print(df3[:3])



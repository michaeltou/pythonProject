import pandas as pd
import numpy as np

##教程：http://liao.cpython.org/pandas13.html
val = np.arange(10,60).reshape(10,5)

columns = ['ac','bc','cc','dc','ec']
index = list('ABCDEFGHIJ')
df1 = pd.DataFrame(val, columns=columns, index=index)
print(df1)

print("*"*21,"<- dataFrame")

val = np.arange(100,110).reshape(10,1)
df1['fix'] = val

print("*"*21,"<- dataFrame")
print(df1)
print("*"*21,"<- dataFrame")
df1.insert(1,'new',val)
print(df1)
print("*"*21,"<- dataFrame")

df1.loc[:,"column-add-by-loc"] = val

print(df1)
print("*"*21,"<- dataFrame")
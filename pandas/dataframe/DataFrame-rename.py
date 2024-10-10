import pandas as pd
import numpy as np
##教程：http://liao.cpython.org/pandas13.html
val = np.arange(10,60).reshape(10,5)

columns = ['ac','bc','cc','dc','ec']
index = list('ABCDEFGHIJ')
df1 = pd.DataFrame(val, columns=columns, index=index)
print(df1)

print("*"*21,"<- dataFrame")
df2 = df1.rename(columns={'ac':'A-column',"bc":'B-column'})
print(df2)
print("*"*21,"<- dataFrame")



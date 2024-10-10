import pandas as pd
import numpy as np
##教程：http://liao.cpython.org/pandas13.html
val1 = np.arange(10,40).reshape(10,3)
val2 = np.arange(50,80).reshape(10,3)

col1 = ["ax","bx","cx"]
col2 = ["ay","by","cy"]

idx = list("abcdefghij")

df1 = pd.DataFrame(val1,index=idx,columns=col1)
df2 = pd.DataFrame(val2,index=idx,columns=col2)

print(df1)
print("*"*20,"<-DataFrame")

print(df2)
print("*"*20,"<-DataFrame")

df3 = pd.concat([df1,df2[:5],df1[5:],df2],axis=1)

print(df3)

print("*"*20,"<-DataFrame")
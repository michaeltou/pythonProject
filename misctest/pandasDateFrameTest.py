
from pandas import Series,DataFrame

data = {
        "name":["John","Smith","Michael"],
        "age":[10,20,30],
        "price":[100,200,300]
        }

mydf = DataFrame(data,columns=["name","age","price","sex"],index=["a","b","c"])

mydf.loc['a','age'] = 18

print(mydf)

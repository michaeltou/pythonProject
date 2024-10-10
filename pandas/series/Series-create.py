import pandas as pd
s = pd.Series([1, 2, 3, 4, 5],index=['a', 'b', 'c', 'd', 'e'])
print(s)
a = s[:1]
b = s[1:3]
c = s[s > 3]


d = s.iloc[1]
print('test')
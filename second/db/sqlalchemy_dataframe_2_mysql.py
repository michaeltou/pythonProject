import pandas as pd
from sqlalchemy import create_engine

# create engine
engine = create_engine('mysql+pymysql://root:tm123456@localhost:3306/test')

sql='''
    SELECT * FROM students;
'''


# read data from database
df = pd.read_sql(sql, engine)

# print data
print(df)

mydf = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

# write data to database
mydf.to_sql('mydata', engine, if_exists='append', index=False)
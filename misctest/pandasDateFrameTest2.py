
from pandas import Series,DataFrame
import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                   columns=['max_speed', 'shield'])

row = df.loc['viper']
row['max_speed'] = 111
print(row)

newDf = df.loc[['viper', 'sidewinder']]
print(newDf)

df.loc['viper', 'max_speed'] = 88
cell = df.loc['viper', 'max_speed']
print(cell)


mulSliceDF = df.loc['cobra':'viper', 'max_speed':'shield']
print(mulSliceDF)


newDFFromBoolean  = df.loc[[False, True, True]]
print(newDFFromBoolean)


sliceMultiRow = df.loc['cobra':'viper']
print(sliceMultiRow)

print('============')
column = df['shield']
print(column)


print('============')
columnConditionSeria = df['shield'] > 4
print(columnConditionSeria)

print('============')
condition_DF = df.loc[columnConditionSeria]
print(condition_DF)

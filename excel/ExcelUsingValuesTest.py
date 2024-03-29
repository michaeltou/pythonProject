import pandas as pd

"""默认读数 sheet1 """
#myexcel = pd.read_excel('testSheet.xlsx')

"""默认读数 sheet1, 第一行为列名 """
#myexcel = pd.read_excel('testSheet.xlsx')

"""默认读数 sheet1, 第一行为数据取消header读取 使用header=None ， 指定sheet页签 sheet_name =xxx """
myexcel = pd.read_excel('testSheet.xlsx',
                        header=None,sheet_name='场外期权 Option')

myvalues = myexcel.values

myColumns = myexcel.columns.values

myIndexs = myexcel.index.values

aCellValue = myexcel.values[2,2]

aRowValue = myexcel.values[1]

multiRowValue1 = myexcel.values[1:3]

multiRowValue2 = myexcel.values[[1,3]]

aColumnValue = myexcel.values[:,1]

multiColumnValue = myexcel.values[:,[1,2]]

areaValue = myexcel.values[1:3,1:3]

print('end')
import pandas as pd

"""默认读数 sheet1 """
#myexcel = pd.read_excel('testSheet.xlsx')

"""默认读数 sheet1, 第一行为列名 """
#myexcel = pd.read_excel('testSheet.xlsx')

"""默认读数 sheet1, 第一行为数据取消header读取 使用header=None ， 指定sheet页签 sheet_name =xxx """
myexcel = pd.read_excel('testSheet.xlsx',
                        header=None,sheet_name='场外期权 Option')

myvalues = myexcel.loc[:,:].values

aCellValue = myexcel.loc[2,3]

aRowValue = myexcel.loc[2].values

aColumnValue = myexcel.loc[:,2].values


newData = myexcel.loc[2:].values
newColumns = myexcel.loc[1].values
''' 新构建一个DataFrame '''
newDF = pd.DataFrame(data=newData, columns=newColumns)

''' 保存到csv '''
newDF.to_csv('testSheetResult.csv')

''' 保存到excel '''
newDF.to_excel('testSheetResult.xlsx')


new_excel = pd.read_excel('testSheetResult.xlsx',sheet_name='Sheet1')

columNameNdArray = new_excel.columns.values

name =columNameNdArray[1];

oneCellValue = new_excel.loc[1,'期权费\nPremium']

twoRows = new_excel.loc[[0,1]]
twoRowsValues  = new_excel.loc[[0,1]].values

print('end')
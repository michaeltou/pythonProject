import time
from  dbfread import DBF
from pandas import DataFrame

#table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/SJSMX1.dbf')
table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/ZZGZ20180307.dbf',encoding='gbk')

frame = DataFrame(iter(table))
count = len(frame)
print("总行数：", count)
start = time.time()
print(frame)

end = time.time()
print("总耗时：", end-start)
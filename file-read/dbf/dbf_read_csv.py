import csv, sys,time
from dbfread import DBF



table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/SJSMX1.dbf')
#table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/ZZGZ20180307.dbf',encoding='gbk')

writer = csv.writer(sys.stdout)

writer.writerow(table.field_names)
start_time = time.time()
for row in table:
    writer.writerow(list(row.values()))

end_time = time.time()
print("Total time: ", end_time - start_time) ## 输出运行时间 17.864295959472656

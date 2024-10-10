import dbfread as df
import pandas as pd
import time

dbf_filename = r"/Users/douming/Documents/读数工具重构/dbf_files/ZZGZ20180307.dbf"  # dbf文件
xls_filename = r"test.xlsx"  # 输出路径

#data = df.DBF(dbf_filename, encoding='utf-8')  # dbf编码为utf-8，如果编码错误可能会乱码
table = df.DBF(dbf_filename, encoding='gbk') # dbf编码为GBK，如果编码错误可能会乱码
start_time = time.time()
df = pd.DataFrame(iter(table))
end_time = time.time()
print("读取完成，用时：", end_time - start_time, "秒") #读取完成，用时： 1.564056634902954 秒

start_time = time.time()
df.to_excel(xls_filename, index=False)  # 写入表格中
end_time = time.time()
print("写入完成，用时：", end_time - start_time, "秒")#写入完成，用时： 11.144834041595459 秒
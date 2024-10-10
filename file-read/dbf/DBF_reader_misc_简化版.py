from dbfread import DBF
import pandas as pd
import time
from sqlalchemy import create_engine
 
#table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/SJSMX1.dbf')
# table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/ZZGZ20180307.dbf',encoding='gbk')
table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/债券估值2023082917542120972.dbf',encoding='gbk')


##1 获取记录数量
print("总记录数：", len(table))

##3 打印记录
print('--------------打印10条记录------------------start--------------------------')
count = 0
print_total_cnt = 10
for record in table:
    if count < print_total_cnt:
        # 打印每一条记录，记录是以字典的形式呈现的，字段名作为键，字段值作为值。
        print(record)
    else:
        break
    count += 1
print('-------------打印10条记录-----end--------------------------')



##5 与pandas库结合使用
start_time = time.time()


#加载数据,转成DataFrame耗时： 19.70460796356201 ,记录数: 375468
#加载数据,转成DataFrame耗时： 1.5372779369354248 ,记录数: 42286
df = pd.DataFrame(iter(table))
end_time = time.time()
execution_time = end_time - start_time
print("加载数据,转成DataFrame耗时：", execution_time,',记录数:', len(table))


engine = create_engine('mysql+pymysql://root:tm123456@localhost:3306/test')



##11 每隔一千条数据 获取DataFrame的数据后,打印出来
batch_size = 5000
total_rows = len(df)
start_time = time.time()
# for start in range(0, total_rows, batch_size):
#    end = min(start + batch_size, total_rows)
#    batch_start_time = time.time()
#    batch_df = df.iloc[start:end]
#    batch_end_time = time.time()
#    batch_execution_time = batch_end_time - batch_start_time
#    batch_start_time = time.time()
#    batch_df.to_sql('dbf_table', engine, if_exists='append', index=False)
#    batch_end_time = time.time()
#    batch_execution_time = batch_end_time - batch_start_time
#    print(f'写入一批次数据,耗时:{batch_execution_time:.10f}')

#获取表的列名称

#  df_match = pd.DataFrame()
# for col_n in col_name:
#     df_match[col_n] = self.df[col_n]

# 直接插入数据库,耗时：  27.01075005531311,记录数: 375468
df.to_sql('dbf_mysql_2_table', engine, if_exists='append', index=False,chunksize=1000)


end_time = time.time()
execution_time = end_time - start_time
print("插入数据库总耗时：", execution_time,'记录数:', len(table))





from dbfread import DBF
import pandas as pd
import time
from sqlalchemy import create_engine
 
table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/SJSMX1.dbf')
#table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/ZZGZ20180307.dbf',encoding='gbk')



print_total_cnt = 10
count = 0

##1 获取记录数量
print("总记录数：", len(table))


##2 获取字段名
print("字段名：", table.field_names)

##3 打印记录
print('--------------打印10条记录------------------start--------------------------')
for record in table:
    if count < print_total_cnt:
        # 打印每一条记录，记录是以字典的形式呈现的，字段名作为键，字段值作为值。
        print(record)
    else:
        break
    count += 1
print('-------------打印10条记录-----end--------------------------')

##4 筛选数据
# filtered_table = [record for record in table if record['ZQJC'] == '01国开21']
#
# print("筛选后记录数：", len(filtered_table))
# for record in filtered_table:
#     print('筛选后记录:', record)


##5 与pandas库结合使用
start_time = time.time()

## 加载方法1
#加载数据,转成DataFrame耗时： 19.5645968914032 ,记录数: 375468
#加载数据,转成DataFrame耗时： 1.5490238666534424 ,记录数: 42286

records = list(table)
df = pd.DataFrame.from_records(records)

## 加载方法2
#加载数据,转成DataFrame耗时： 19.70460796356201 ,记录数: 375468
#加载数据,转成DataFrame耗时： 1.5372779369354248 ,记录数: 42286
# df = pd.DataFrame(iter(table))



end_time = time.time()
execution_time = end_time - start_time
print("加载数据,转成DataFrame耗时：", execution_time,',记录数:', len(table))

print(df)

##6 查看头部和尾部的记录
print("头部记录：", df.head(1))
print("尾部记录：", df.tail(1))

##7 查看数据信息
print('查看数据信息:\n', df.info())

##8 统计数据
print('统计数据:\n', df.describe())

##9 使用query方式筛选数据
start_time = time.time()
#filtered_df = df.query('ZQJC == "01国债7" or ZQJC=="18贴现国债10"')
filtered_df = df.query('MXJSZH == "650120" or MXBFZH=="B001302000"')
end_time = time.time()
execution_time = end_time - start_time
print("使用query方式筛选数据耗时：", execution_time)
print(filtered_df)

##10 获取DataFrame的记录总数
start_time = time.time()
total_cnt = len(df)
end_time = time.time()
execution_time = end_time - start_time
print("获取DataFrame的记录总数耗时：", execution_time,",记录总数：", total_cnt)


engine = create_engine('mysql+pymysql://root:tm123456@localhost:3306/test')


##11 每隔一千条数据 获取DataFrame的数据后,打印出来
batch_size = 1000
total_rows = len(df)
start_time = time.time()
for start in range(0, total_rows, batch_size):
   end = min(start + batch_size, total_rows)
   batch_start_time = time.time()
   batch_df = df.iloc[start:end]
   batch_end_time = time.time()
   batch_execution_time = batch_end_time - batch_start_time
   print(f'获取一批次数据,耗时:{batch_execution_time:.10f}',',数据是:',batch_df)
   batch_start_time = time.time()
   batch_df.to_sql('dbf_table', engine, if_exists='append', index=False)
   batch_end_time = time.time()
   batch_execution_time = batch_end_time - batch_start_time
   print(f'写入一批次数据,耗时:{batch_execution_time:.10f}')
end_time = time.time()
execution_time = end_time - start_time
print("分批获取,总耗时：", execution_time)





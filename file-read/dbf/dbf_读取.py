from dbfread import DBF

table = DBF('/Users/douming/Documents/读数工具重构/dbf_files/ZZGZ20180307.dbf',encoding='gbk')


name = table.name  # 名称
encoding = table.encoding  # 编码
date = table.date  # 创建时间
field_names = table.field_names  # 字段名称列表（不包含FID）
header = table.header  # 文件头（元数据）
records = table.records  # 属性行
for record in records:
    print(record)

table = table.deleted  # 假删除
for record in table:
    print(record)
import dbf

def read_dbf(file_path):
    # 打开 DBF 文件
    df = dbf.open(file_path)

    # 读取所有记录
    for record in df:
        # 打印每条记录的字段值
        print(record)

    # 关闭文件
    df.close()


# 替换为实际的 DBF 文件路径
file_path = r'/Users/douming/Downloads/中泰文件拆分/SJSMX1.dbf'

read_dbf(file_path)
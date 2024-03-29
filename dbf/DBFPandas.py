import pandas as pd
import datetime
from dbfread import DBF

path = r'/Users/douming/Downloads/中泰文件拆分/SJSMX1.dbf'  # 文件目录
table = DBF(path)
startime = datetime.datetime.now()
df = pd.DataFrame(iter(table))
df.to_csv("/Users/douming/Downloads/中泰文件拆分/SJSMX1.csv", index_label="FID")

endtime = datetime.datetime.now()
print("共耗时：{0}".format(endtime - startime))


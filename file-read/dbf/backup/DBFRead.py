import dbfread

from dbfpy import dbf

'''
读取DBF文件
'''
def readDbfFile(filename):
    table = dbfread.DBF(filename, encoding='GBK')

    for field in table.fields:
        print(field)

    for record in table:
        print('this is a record...................')
        for field in record:
            print(field, record[field])

file_path = r'/Users/douming/Downloads/中泰文件拆分/SJSMX1.dbf'
# readDbfFile(file_path)


def writeDbfFile(filename, header, content):
    # 打开dbf
    db = dbf.Dbf(filename, new=True)
    # 写列头
    for field in header:
        # 此处需要改成长度可配的，长度太短会导致数据被截断
        if type(field) == unicode:
            field = field.encode('GBK')
        db.addField((field, 'C', 20))

    # 写数据
    for record in content:
        rec = db.newRecord()
        for key, value in itertools.izip(header, record):
            if type(value) == unicode:
                rec[key] = value.encode('GBK')
            else:
                rec[key] = value
            rec.store()
    # 关闭文档
    db.close()



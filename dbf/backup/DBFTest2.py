import dbf,datetime
import random
import os, time
from multiprocessing import Pool



def add_bpm(num, HKSZDM):
    table = dbf.Table(
        filename='test',
        field_specs='BMH C(20);XM C(10);XBM C(2);SFZJLXM C(2);'
                    'SFZJHM C(18);CSRQ C(8);MZM C(2);HKSZDM C(8);'
                    'ZP C(100)',
        on_disk=False,
    )
    table.open(mode=dbf.READ_WRITE)
    list = [1, 2, 3, 4, 'A', 'B', 'Z', 5, 6, 7, 8, 9]
    list2 = ['01', '02', '03', '04', '05', '06', '55', '56', '97', '98', '23']
    list_bp = ['3601021234501', '李考生一', '1', '1', '360102199904230123','2']
    b = []
    #num表示行数，要循环造多少行这样的数据
    for i in range(1,num+1):
        list_bp[0] = str(HKSZDM) + str(1234501 + i)  # BMH
        list_bp[1] = "xm" + str(i)  # XM
        list_bp[2] = str(random.randint(1, 2))  # XBM
        list_bp[3] = str(random.sample(list, 1)[0])  # SFZJLXM
        list_bp[4] = str(random.sample(list2, 1)[0])  # MZM
        list_bp[5] = str(HKSZDM)  # HKSZDM

        b.append(tuple(list_bp))

    for datum in tuple(b):
        table.append(datum)

    custom = table.new(
        filename=r'导入模板1.dbf',
        default_data_types=dict(C=dbf.Char, D=dbf.Date, L=dbf.Logical),
    )

    with custom:
        for record in table:
            custom.append(record)

    table.close()


def main():
    #cpu密集型任务采用多进程
    startime = datetime.datetime.now()
    print("主进程开始执行>>> pid={}".format(os.getpid()))
    ps = Pool(10)
    # ps.apply(add_bpm,args=(i,)) # 同步执行
    #一个dbf要造160000行数据
    #ps.apply_async(add_bpm(160000, 220102), args=())  # 异步执行
    ps.apply_async(add_bpm(160000, 220102), args=())  # 异步执行

    # 关闭进程池，停止接受其它进程
    ps.close()
    # 阻塞进程
    ps.join()
    print("主进程终止")
    endtime = datetime.datetime.now()
    print("共耗时：{0}".format(endtime-startime))

if __name__ == '__main__':
    main()
import os,time
import pandas as pd
import dbfread as df

filter = ['.DBF', '.dbf']  # 设置过滤后的文件类型 当然可以设置多个类型

def all_path(dirname):
    result = []  # 所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):
        print("提示：当前主目录", "1:", maindir)  # 当前主目录
        print("提示：当前主目录下的所有目录", "2:", subdir)  # 当前主目录下的所有目录
        # print("3:",file_name_list)  #当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            # 设置过滤器，过滤不符合格式的文件
            if ext in filter:
                result.append(apath)
    return result


if __name__ == '__main__':
    input_file_path = r'input/'  # 输入路径
    output_file_path = r'output/'  # 输出路径
    if not os.path.exists(output_file_path):
        # os.mkdir创建一个，os.makedirs可以创建路径上多个
        os.makedirs(output_file_path)
    file_list = all_path(input_file_path)
    if len(file_list) > 0:
        for dbf_file_name in file_list:
            try:
                data = df.DBF(dbf_file_name, encoding='utf-8',load=True)
            except:
                # 如果报错尝试下面这一句
                try:
                    data = df.DBF(dbf_file_name, encoding='gbk',load=True)
                except:
                    print('该文件未进行处理', dbf_file_name)
            df_data = pd.DataFrame(iter(data))
            name = os.path.basename(dbf_file_name).split('.')[0]
            start_time = time.time()
            df_data.to_excel(output_file_path + name + '.xlsx', index=False)  # 写入表格中
            end_time = time.time()
            print('已处理文件：', dbf_file_name, '用时：', end_time - start_time)
        print('----已处理完成----')
    else:
        print('----该路径下无dbf文件----')
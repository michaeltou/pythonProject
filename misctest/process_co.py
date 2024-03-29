import time
import pymongo

import_code('uc_fam_fp_config')


def get_dms(contract_no):
    """
    获得合约映射关系
    :param contract_no: 外部合约编号，我们用的是客户名称，因为做账是以文件为单位的
    :return: 映射关系列表
    """
    client = pymongo.MongoClient(uc_fam_fp_config.mongodb_uri)
    return list(client['fileanalyze']['data_mapping_setting'].find(
        {'bizType': 'biz00009', 'outerContractNo': contract_no}))


def get_far(fn):
    """
    根据文件名获得解析数据
    :param fn: 文件名
    :return: 解析数据列表
    """
    client = pymongo.MongoClient(uc_fam_fp_config.mongodb_uri)
    return list(client['fileanalyze']['file_analyze_result'].find({'fileName': fn}))


def process(fn):
    ret = []

    # 第一步，获取解析好的数据
    data_list = get_far(fn)
    if len(data_list) == 0:
        raise Exception(f'未查询到文件"{fn}"的解析结果！')

    for data in data_list:
        if data['bizType'] == 'biz00009':
            public_data = dict()
            public_data['fileName'] = fn
            public_data['bizType'] = data['bizType']
            # public_data['process_date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            public_data['processTime'] = float(time.strftime('%Y%m%d.%H%M%S', time.localtime()))

            # public_data['showInfo'] = [
            #     {'fileName': '文件名'},
            #     {'bizType': '业务类型'},
            #     {'processTime': '加工时间'}
            # ]

            if data['dataTag'] == '基础信息':
                info = data['extractTables']['汇总信息'][0]

                # 第二步，根据外部合约编号，获取合约映射关系
                dms = get_dms(info['客户名称'])
                if len(dms) == 0:
                    raise Exception(f'合约编号：{info["客户名称"]}找不到映射关系！')

                public_data['产品编号'] = dms[0]['fundId']
                public_data['合约编号'] = dms[0]['contactNo']

                # public_data['showInfo'].append({'产品编号': '账套编号'})
                # public_data['showInfo'].append({'合约编号': '合约编号'})

                if '名义本金_余额' in info and \
                        info['名义本金_余额'] is not None and \
                        info['名义本金_余额'] != 0:
                    temp = public_data.copy()
                    temp['interfaceTag'] = '名义本金'

                    temp['估值日期'] = info['估值日期']
                    temp['名义本金余额'] = info['名义本金_余额']

                    # temp['showInfo'].append({'估值日期': '估值日期'})
                    # temp['showInfo'].append({'名义本金余额': '名义本金余额'})

                    ret.append(temp)

                if '预付金_变动额' in info and \
                        info['预付金_变动额'] is not None and \
                        info['预付金_变动额'] != 0:
                    temp = public_data.copy()
                    temp['interfaceTag'] = '预付金'

                    temp['估值日期'] = info['估值日期']
                    temp['预付金调整金额'] = info['预付金_变动额']
                    ret.append(temp)

                if '期权费_变动额' in info and \
                        info['期权费_变动额'] is not None and \
                        info['期权费_变动额'] != 0:
                    temp = public_data.copy()
                    temp['interfaceTag'] = '期权费'

                    temp['估值日期'] = info['估值日期']
                    temp['期权费类型'] = 1
                    temp['期权费金额'] = info['期权费_变动额']
                    ret.append(temp)
                elif '期权费_余额' in info and \
                        info['期权费_余额'] is not None and \
                        info['期权费_余额'] != 0:
                    temp = public_data.copy()
                    temp['interfaceTag'] = '期权费'

                    temp['估值日期'] = info['估值日期']
                    temp['期权费类型'] = 2
                    temp['期权费金额'] = info['期权费_余额']
                    ret.append(temp)

                if '累计盈亏' in info and \
                        info['累计盈亏'] is not None and \
                        info['累计盈亏'] != 0:
                    temp = public_data.copy()
                    temp['interfaceTag'] = '估值增值'

                    temp['估值日期'] = info['估值日期']
                    temp['估值增值'] = info['累计盈亏']
                    ret.append(temp)
            elif data['dataTag'] == '结算信息':
                info = data['extractTables']['汇总信息'][0]

                dms = get_dms(info['客户名称'])
                if len(dms) == 0:
                    raise Exception(f'合约编号：{info["客户名称"]}找不到映射关系！')

                public_data['产品编号'] = dms[0]['fundId']
                public_data['合约编号'] = dms[0]['contactNo']

                if '当日_发生额' in info and \
                        info['当日_发生额'] is not None and \
                        info['当日_发生额'] != 0:
                    temp = public_data.copy()
                    temp['interfaceTag'] = '行权信息'
                    temp['估值日期'] = info['估值日期']
                    temp['交收日期'] = info['估值日期']

                    temp['结算类型'] = 1
                    temp['结算金额'] = info['当日_发生额']
                    ret.append(temp)
                elif '当日_余额' in info and \
                        info['当日_余额'] is not None and \
                        info['当日_余额'] != 0:
                    temp = public_data.copy()
                    temp['interfaceTag'] = '行权信息'
                    temp['估值日期'] = info['估值日期']
                    temp['交收日期'] = info['估值日期']

                    temp['结算类型'] = 2
                    temp['结算金额'] = info['当日_余额']
                    ret.append(temp)
    return ret


"""
#file_name = '/opt/upfile/fafile/gdzq/场外期权/光大证券/估值报告/2023-09-07_易股鑫源七号私募证券投资基金_ _估值报告.xlsx'
file_name = '/opt/upfile/fafile/gdzq/场外期权/光大证券/结算单/单宽投启明星8号_EBS1-KTZC-20221228到期结算通知.docx'

data = process(file_name)
print(data)
"""


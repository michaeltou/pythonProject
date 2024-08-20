
class OptionBaseInfo(object):
    def __init__(self):
        # self.data.bizType = '场外期权'
        self.bizType = 'biz00009'
        self.dataTag = '基础信息'

        self.tables_structure = {
            '汇总信息': ['客户名称', '估值日期', '预付金_余额', '预付金_变动额', '名义本金_余额', '期权费_余额', '期权费_变动额', '累计盈亏'],
            '预付金变动流水': ['日期', '金额'],
            '名义本金流水': ['合约编号', '起始日', '到期日', '余额'],
            '期权费调整流水': ['合约编号', '日期', '余额', '发生额'],
            '合约累计盈亏': ['合约编号', '估值日期', '累计盈亏']
        }

class OptionSettlementInfo(object):
    def __init__(self):
        # self.data.bizType = '场外期权'
        self.bizType = 'biz00009'
        self.dataTag = '结算信息'

        self.tables_structure = {
            '汇总信息': ['客户名称', '估值日期', '当日_余额', '当日_发生额'],
            '结算明细': ['合约编号', '交易日', '交收日', '余额', '发生额'],
        }


# 第三步，给返回对象赋值
ret_list = [OptionBaseInfo(), OptionSettlementInfo()]

# 创建一个列表params，其中每个元素是一个字典，字典的键为返回对象的表格结构中的表格名，值为空字典。
params = [
    {tb_name: dict() for tb_name in ret.tables_structure.keys()}
    for ret in ret_list
]



print(params)






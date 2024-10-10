from flask import Flask, request, render_template
from waitress import serve

##WAITRESS  Werkzeug  使用 Gunicorn 启动多个实例
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/execute/<method>', methods=['POST'])
def execute(method):
    json_data = request.get_json()
    read(**json_data)
    return 'ok'



def read(*args, **kwargs):
    print(args, kwargs)



'''
    #1: 根据接口, 获取匹配的配置 
    ( 不用文件名称的原因，正则匹配如何配置有误，会发生巨大的碰撞风险，
      另外 调用方，不用去路径上找文件，判断文件是否存在，会增加复杂度
    )
'''


'''
    #2: 根据配置，获取源配置, 目标配置
    源配置包含：文件类型fileFormat（dbf，excel，txt，xml，db，T2）, 来源字段（字段名称，字段位置）
    目标配置：目标数据库，目标表名称，目标字段名称
    映射配置：字段映射关系
    字段加工配置：字段加工逻辑
    前置逻辑： （初始化序列号）
    后置逻辑： 待定
    校验逻辑：读数完成后的校验逻辑
    
'''


'''
    #3:  执行读数流程
        1、获取源文件数据-> 转成统一 DataFrame 模型
        2、根据前置逻辑，初始化字段 
        3、根据字段加工配置，对源字段进行加工
        4、根据映射配置，映射源字段到目标字段
        5、写入目标数据库，目标表
        6、根据校验逻辑，对读数结果进行校验
        7、返回结果
'''



if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    serve(app, host='0.0.0.0', port=80, threads=4)




#动态生成变量
var_name = "dynamic_var"
var_value = "3"
exec(f"{var_name} = '{var_value}'")

print(dynamic_var) #dynamic_var

#
func_code = '''
def my_func(x):
    return x + 1
'''

exec(func_code)

print(my_func(8)) #9


#动态生成类
class_code = '''
class MyClass:
    def __init__(self, x):
        self.x = x
    
    def my_method(self):
        return self.x + 1
'''


exec(class_code)

my_obj = MyClass(5)
print(my_obj.my_method()) #6


filecontent = open("external_code.py").read()
exec(filecontent)

external_function() 



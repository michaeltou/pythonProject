
global_var = {}
local_var = {}
def create_function(func_name, func_body):
    exec(f'def {func_name}():\n\t{func_body}',global_var,local_var)

create_function('hello', 'print("Hello, World!")')

local_var['hello']()
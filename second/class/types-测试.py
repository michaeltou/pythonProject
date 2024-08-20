import types

def func():
    pass

if type(func) == types.FunctionType:
    print("func is a function")

if(type(lambda x:x+1) == types.LambdaType):
    print("lambda"
          " is a lambda function")

if(type((x for x in range(10))) == types.GeneratorType):
    print("generator"
          " is a generator function")
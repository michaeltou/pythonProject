
x = 1
y = 2

mycode = '''
z = 30
sum = x + y + z
print(sum)

def add(a,b):
    return a+b

print(add(1,2))
'''

myCompileResult = compile(mycode, '<string>', 'exec')

exec(myCompileResult)




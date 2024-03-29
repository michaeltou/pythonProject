import ast

py_src = """
def add(x, y):
    return x + y
     
print(add(3, 5))
a = 1
b = a + 3
if b > 3:
    print("xxx")
"""


def myfunc():
    pass

print(type(myfunc))
print(myfunc.__code__)
print(dir(myfunc.__code__))















f= lambda x:x**4

print(f)

print(f(2)) # Output: 4

def build(x,y):
    return lambda: x+y

f=build(2,3)

print(f()) # Output: 5
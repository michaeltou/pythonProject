

def add(x,y,f):
    return f(x) + f(y)


res = add(2,3,lambda x: x*2)
print(res)
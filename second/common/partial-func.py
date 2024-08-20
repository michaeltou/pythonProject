
from functools import partial

myint = partial(int, base=2)

print(myint('1010'))


mymax = partial(max, 10, 20, 30)
print(mymax(1,2,33))
import os
mylist = [x for x in range(1, 11) if x % 2 == 0]

print(mylist)


myfiles = [d for d in os.listdir('..')]
print(myfiles)
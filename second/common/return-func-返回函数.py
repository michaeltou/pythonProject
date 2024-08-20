
def lazy_sum(*args):
    def sum():
        r  = 0
        for n in args:
            r += n
        return r

    return sum


mysum1 = lazy_sum(1, 3, 5)
mysum2 = lazy_sum(1, 3, 5)
print(mysum1())

print(mysum1 == mysum2)

my_generator = (x for x in range(10))

# for i in my_generator:
#     print(i)


def fib(max):
    n,a,b = 0,0,1
    while b < max:
        yield b
        a,b = b,a+b
        n += 1
    return 'done'

fib_generator = fib(100)

# for i in fib_generator:
#     print(i,end=' ')

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

myodd = odd()

for oddd in myodd:
    print(oddd)


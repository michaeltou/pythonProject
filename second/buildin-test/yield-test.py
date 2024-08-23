def square_generator(n):
    for i in range(n):
        yield i**2

for i in square_generator(5):
    print(i)
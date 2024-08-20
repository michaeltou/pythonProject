
#https://liaoxuefeng.com/books/python/function/parameter/index.html

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print("Sum of squares of numbers is:", sum);
    return sum

list1 = [1, 2, 3, 4, 5]
calc(*list1)


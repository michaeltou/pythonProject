

def is_odd(n):
    return n % 2 == 1

filter_result = filter(is_odd, [1, 2, 3, 4, 5])
print(list(filter_result))  # [1, 3, 5]
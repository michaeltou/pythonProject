import math

# 'a test module'
#
def power(x,n = 2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        pass
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

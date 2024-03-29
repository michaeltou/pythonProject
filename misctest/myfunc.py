import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Argument must be an integer')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


def def_param(name, age=18):
    print('name:{},age:{}'.format(name,age))


def calc(numbers):
    result = 0
    for i in numbers:
        result = result + int(i)
    return result

def calc2(*numbers):
    result = 0
    for i in numbers:
        result = result + int(i)
    return result

def person(name,age,**kw):
    print('name:{},age:{},kw:{}'.format(name,age,kw))


def add(x, y, f):
    return f(x)+f(y)


def f(x):
    return x*x


def is_odd(x):
    return x % 2 == 0
def test():
    print("Hello World")


def _private_func1(name):
    return 'Hello '+ name


def _private_func2(name):
    return 'Hi, '+ name


def greeting(name):
    if len(name) > 3:
        return _private_func1(name)
    else:
        return _private_func2(name)





if __name__ == '__main__':
    test()


def _private_1(name):
    print("Hello, " + name + "!")
    return name


def _private_2(name):
    print("Hello, " + name + "!")


def greeting(name):
    if len(name) > 5:
        return _private_1(name)
    else:
        return _private_2(name)


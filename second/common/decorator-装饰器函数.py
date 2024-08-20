from datetime import datetime



def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} at {datetime.now()}")
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print(datetime.now())

#
# now = log(now)

now()
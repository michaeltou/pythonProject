from datetime import datetime



def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("tag:=",text,'func:=',func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log("time")
def now():
    print(datetime.now())


now()
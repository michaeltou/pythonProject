
class MyObject:
    def __init__(self):
        self.x = 10
    def power(self, n):
        return n * 2

obj = MyObject()

print(hasattr(obj, 'x')) # True
print(hasattr(obj, 'y')) # False

print(isinstance(obj, MyObject)) # True
print(isinstance(obj, int)) # False

setattr(obj, 'x', 20)
print(obj.x) # 20

print(getattr(obj, 'power')(3)) # 6

getattr(obj, 'y', 40 ) # 40 (default value is returned if attribute is not found)
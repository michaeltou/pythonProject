
class Student(object):
    def __init__(self,name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print(  args)
        print(  kwargs)



s = Student("Alice")

s(1,2,3,a= 4,b=5)



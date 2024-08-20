class Student(object):

    def __init__(self,name):
        self._name = name

    def __str__(self):
        return "Student object (name: %s)" % self._name


    def __len__(self):
        return len(self._name)

    __repr__ = __str__



s = Student("Alice")
print(s)
print(len(s))
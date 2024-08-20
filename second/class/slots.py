class Student(object):
    __slots__ = ('name', 'age', 'gender','set_age') # slots are defined here


s = Student()


def set_age(self, age):
    self.age = age


Student.set_age = set_age  # adding the set_age method to the instance

s.set_age(25)  # calling the set_age method

print(s.age)




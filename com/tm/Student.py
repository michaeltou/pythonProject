
class Student(object):
    age = 18
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))

print(Student.age)
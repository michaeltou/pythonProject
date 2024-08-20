class Student(object):

    _age = 18 # class variable

    def __init__(self,name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print(self.__name + "'s score is " + str(self.__score))


bart = Student("Bart", 85)


print(bart._age) # Bart



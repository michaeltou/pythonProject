
class Student:
    def __init__(self):
        self.name = "John"

    def __getattr__(self,attr):
        if attr == "score":
            return 80
        else:
            return "default value"


s = Student()
print(s.name)
print(s.score)
print(s.age)
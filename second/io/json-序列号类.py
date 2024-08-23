
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score



s = Student('Alice', 20, 90)



import json

json_str = json.dumps(s,default=lambda obj: obj.__dict__)



my_student = json.loads(json_str, object_hook=lambda d: Student(**d))

print(my_student)
print(type(my_student))
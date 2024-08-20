
class Student:
    hobby = "drive motorcycles"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")


print(Student.hobby)

s1 = Student("John", 20)

print(s1.hobby)
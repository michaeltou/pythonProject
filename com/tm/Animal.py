
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def call(self):
        print("Woof, my name is " + self.name + " and I am " + str(self.age) + " years old and I am a " + self.breed + ".")

if __name__ == '__main__':
    my_animal = Animal("Fido", 5)

    my_dog = Dog("Buddy", 3, "Labrador")
    my_dog.call()
    print(isinstance(my_animal, Dog))


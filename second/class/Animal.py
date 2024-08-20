

class Animal(object):
    def run(self):
        print("Animal is running")

    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

animal = Animal()
dog = Dog()
cat = Cat()


 
dog.run()
dog.eat()





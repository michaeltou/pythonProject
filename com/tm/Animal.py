
class Animal(object):
    def run(self):
        print('Animal is running.')


class Dog(Animal):
    def run(self):
        print('Dog is running.')


class Cat(Animal):
    def run(self):
        print('Cat is running.')


dog = Dog()
cat = Cat()


def run_twice(animal):
    animal.run()
    animal.run()


print(setattr(dog,'__name__',1))

print(getattr(dog,'__name__'))



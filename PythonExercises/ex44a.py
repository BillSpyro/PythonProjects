# Exercise 44A

class Dog(object):

    # Implicit Method
    def bark(self):
        print("woof!")

class Poodle(Dog):
    pass

fido = Dog()
spot = Poodle()

fido.bark()
spot.bark()

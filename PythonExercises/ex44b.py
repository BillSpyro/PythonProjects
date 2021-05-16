# Exervise 44B

class Bird(object):

    def fly(self):
        print("I can fly!")

class Penguin(Bird):

    #Override method
    def fly(self):
        print("I'll swim instead...")

tweety = Bird()
slippy = Penguin()

tweety.fly()
slippy.fly()

#Exercise 44E

class Other(object):

    def implicit(self):
        print("OTHER implicit")

    def override(self):
        print("OTHER override")

    def altered(self):
        print("OTHER altered")

class Compound(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("COMPOUND override")

    def altered(self):
        print("COMPUND before altered")
        self.other.altered()
        print("COMPOUND after altered")

x = Compound()

x.implicit()
x.override()
x.altered()

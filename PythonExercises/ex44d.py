# Exercise 44D

class Parent(object):

    def implicit(self):
        print("PARENT implicit")

    def override(self):
        print("PARENT override")

    def altered(self):
        print("PARENT altered")

class Child(Parent):

    def override(self):
        print("CHILD override")

    def altered(self):
        print("CHILD before altered")
        super(Child, self).altered()
        print("CHILD after altered")

x = Parent()
y = Child()

print("-" * 5)
x.implicit()
y.implicit()
#PARENT implicit
#PARENT implicit

print("-" * 5)
x.override()
y.override()
#PARENT override
#CHILD override

print("-" * 5)
x.altered()
y.altered()
#PARENT altered
#CHILD before altered
#PARENT altered
#CHILD after altered

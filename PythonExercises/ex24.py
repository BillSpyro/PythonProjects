# Exercise 24

people = 10
cats = 10
dogs = 10

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not too many cats! The world is safe.")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world stays dry.")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

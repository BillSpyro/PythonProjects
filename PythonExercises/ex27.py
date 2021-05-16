# Exercise 27

#LISTS NOT ARRAYS

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Looping through lists ...
# of numbers
for number in the_count:
    print(f"This is count {number}")

# of strings
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# of mixed types
for i in change:
    print(f"I got {i}")

# Build a list starting with an empty one
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}")

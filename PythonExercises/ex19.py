# Exercise 19


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def calculate(a, b):
    return a + b

print("Let's do some math with functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# Can you do it by hand?
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, ". Did you figure it out?")

number1 = int(input("Number1: "))
number2 = float(input("Number2: "))
print(calculate(number1, number2))

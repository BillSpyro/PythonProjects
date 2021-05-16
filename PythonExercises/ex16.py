# Exercise 16

# this is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"first: {arg1}, second: {arg2}")

# that *args was unecessary, try it this way
def print_two_again(arg1, arg2):
    print(f"first: {arg1}, second: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Max", "Crandall")
print_two_again("Max", "Crandall")
print_one("ONE!")
print_none()

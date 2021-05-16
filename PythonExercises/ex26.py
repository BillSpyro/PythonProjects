# Exercise 26

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("You see a giant bear eating a cheescake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Make loud noises")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, {bear} was probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothspins")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around between the doors, burt fall on your head and die. Good job!")

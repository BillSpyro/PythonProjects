#Triangle Loop
def Triangle_Loop(end):
    hash = '#'
    start = 0
    while start < end:
        print(hash)
        hash += '#'
        start += 1

#FizzBuzz
def Fizz_Buzz():
    for numbers in range(0,101):
        if numbers % 5 == 0 and numbers % 3 == 0:
            print("FizzBuzz")
        elif numbers % 5 == 0 and numbers % 3 != 0:
            print("Buzz")
        elif numbers % 3 == 0:
            print("Fizz")
        else:
            print(numbers)

#ChessBoard
def Chess_Board():
    hash = '#'
    space = ' '
    row = 8
    column = 8
    ans = ""

    for number1 in range(0, row):
        for number2 in range(0, column):
            if number1 % 2 == 0:
                if number2 % 2 == 0:
                    ans += hash
                else:
                    ans += space
            else:
                if number2 % 2 == 0:
                    ans += space
                else:
                    ans += hash

        ans += "\n"

    print(ans)

#Minimum
def Min(x, y):
    if (x > y):
        return y
    elif(x < y):
        return x
    else:
        return "They are equal"

#Recursion
def Is_Even(x):
    if x == 0:
        return True
    elif x == 1:
        return False
    elif x < 0:
        return Is_Even(x + 2)
    else:
        return Is_Even(x - 2)

#Bean Counting
def Count_Bs(x):
    ans = 0
    for number in range(0, len(x)):
        #Need to fix
        if x[number] == 'B':
            ans += 1
    return ans


def Count_Char(x, y):
    ans = 0
    for number in range(0, len(x)):
        #Need to fix
        if x[number] == y:
            ans += 1
    return ans


triangle = int(input("How big is the triangle? "))
Triangle_Loop(triangle)

Fizz_Buzz()

Chess_Board()

print(Min(1,5))
print(Min(6,5))

print(Is_Even(50))
print(Is_Even(75))
print(Is_Even(-1))
print(Is_Even(-10))

print(Count_Bs("BBC"))
print(Count_Char("kakkerlak", "k"))
print(Count_Char("pepper", "p"))

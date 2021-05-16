# Exercise 28

times = int(input("How many times: "))
increment = int(input("Increment by: "))

def Loop(times, increment):
    numbers = []
    for i in range(0, times, increment):
        print(f"At the top is {i}")

        numbers.append(i)
        print(f"Numbers now: {numbers}")

    return numbers

result = Loop(times, increment)

print("The numbers:")
for num in result:
    print(num)

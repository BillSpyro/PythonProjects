#Hotdogs in packages of 10
#Hotdogs buns come in package of 8
#Calculate number of packages of hot dogs and number of packages of hot dog buns with minium amount of leftovers
#Ask user for the number of people attending the cookout and the number of each dogs per person

people = input("Hello User, How many people are attending? ")
dogsPerPerson = input("How many hot dogs per person? ")

people = int(people)
dogsPerPerson = int(dogsPerPerson)

hotdogPackagesNeeded = (dogsPerPerson * people) / 10
hotdogBunsPackagesNeeded = (dogsPerPerson * people) / 8

hotdogsNeeded = (dogsPerPerson * people)
hotdogBunsNeeded = (dogsPerPerson * people)

hotDogsLeftovers = hotdogsNeeded % 10
hotDogBunsLeftovers = hotdogBunsNeeded % 8

print("Hot dogs left over: " + str(hotDogsLeftovers))
print("Hot dog buns left over: " + str(hotDogBunsLeftovers))
print("Hot dog packages left over: " + str(int(hotdogPackagesNeeded)))
print("Hot dog buns packages left over: " + str(int(hotdogBunsPackagesNeeded)))

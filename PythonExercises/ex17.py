# Exercise 17

#Creates a function of two arguements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("That's enough for a party!")

# we can give it numbers directly
cheese_and_crackers(20, 30)

# or we can use variables
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# or we can do math within the function call
cheese_and_crackers(10 + 20, 5 + 6)

# or we can combine the two
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

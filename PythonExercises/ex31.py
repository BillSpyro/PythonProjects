# Exercise 31

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])
print('-' * 10)

# print some states
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
print('-' * 10)

# Use both at once
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
print('-' * 10)

# print every abbreviation
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print ('-' * 10)

# print every city
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)

# loop through both at once
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)

# safely get an abbreviation that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas")

print('-' * 10)

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city}")


# Exercise 12

from sys import argv

script, user_name, email = argv
prompt = '> '

print(f"Hi {user_name}, {email} is your email I presume. I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"How do you feel about Python, {user_name}?")
feel = input(prompt)

print("Which Broswer are you using?")
broswer = input(prompt)

print("What kind of person are you?")
person = input(prompt)

print(f"""
Alright, {user_name}, your email is {email}, so you said "{feel}" about Python.
You're using {broswer} on your computer. You are a {person} kind of person. Nice.
""")

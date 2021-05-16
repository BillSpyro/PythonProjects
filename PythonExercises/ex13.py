# Exercise 13

from sys import argv

script, filename = argv

#Opens the file
txt = open(filename)

#Prints the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

#Asks to open a file
print("Type the filename again:")
file_again = input('> ')

#Opens the asked file
txt_again = open(file_again)

#Prints that file
print(txt_again.read())


#Using input
filename2 = input("Input file name ")

txt2 = open(filename2)

print(f"Here's your file {filename}:")
print(txt2.read());

txt.close()
txt_again.close()
txt2.close()

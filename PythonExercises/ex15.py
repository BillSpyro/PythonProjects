# Exercise 15.py

from sys import argv
script, from_file, to_file = argv
in_file = open(from_file).read()
out_file = open(to_file, 'w').write(in_file)

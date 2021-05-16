#Move Script

from sys import argv
import shutil, os

script, from_file, to_file = argv

os.rename(from_file, to_file)

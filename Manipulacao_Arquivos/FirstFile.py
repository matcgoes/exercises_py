# file = open("first_file.txt", "w")
#
# file.write("This is my first file!")
#
# file.close()

from Dicionarios_Package.Funcoes import *

with open("first_file.txt", "r") as file:
    for line in file.readlines():
        print(line)

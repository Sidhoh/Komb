# Imports

import os

try:
    _path = os.getcwd()
    _file_name = input("File name: ")
    f = open(_file_name + ".txt", "w+")
    print("Sucessfily created a new text document!")
    os.startfile(_path)
except OSError as error:
    print("Couldn't able to create a new text document...")

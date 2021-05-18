# Imports

import os

try:
    _fldr = input("Folder name: ")
    _path = os.getcwd()
    os.mkdir(_fldr)
    print("Sucessfuly created a new folder!")
    os.startfile(_path)
except OSError as error:    
    print("Couldn't able to create folder...")   

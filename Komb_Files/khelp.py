# Imports

import os

try:
    print("COMMAND LIST\n")
    print("KOFF.exe - This command will turn off your computer\n")
    print("nfldr.exe - This command will create a new folder in your current directory\n")
    print("nps.exe - This command will create a new python script in your current directory\n")
    print("ntd.exe - This command will create a new text document in your current directory\n")
except OSError as error:
    print("Command dosen't exist")


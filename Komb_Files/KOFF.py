# Imports

import os

try: 
    shutdown = input("Do you wish to shutdown your computer ? (y / n): ")
    if shutdown == 'n':
        exit()
    else:
        os.system("shutdown /s /t 1")
except OSError as error:
    print("Couldn't able to shutdown your computer..")


import os

path = "C:\\Users\\WONDERS\\Documents\\SampleTest.txt" # need double bach slash for escape sequence

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path): # To check if it is a file
        print("That is a file")
    elif os.path.isdir(path): # To check if it is a directory
        print("That is a directory")
else:
    print("That location doesn't exist!")

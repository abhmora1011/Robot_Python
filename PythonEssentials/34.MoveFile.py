import os

# We can also move a directory

source = "C:\\Users\\WONDERS\\Documents\\SampleTest.txt"
destination = "C:\\Users\\WONDERS\\Desktop\\SampleTest2.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source + " was not found!")

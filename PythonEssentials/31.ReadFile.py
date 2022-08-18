try:
    with open('C:\\Users\\WONDERS\\Documents\\SampleTest.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print("The file was not found " + e)

print(file.closed)

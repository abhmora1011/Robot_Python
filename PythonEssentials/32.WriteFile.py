text = "\nHave a nice day!"

# if 'w' it will overwrite the content while 'a' will append
#with open("C:\\Users\\WONDERS\\Documents\\SampleTest.txt", "w") as file:
with open("C:\\Users\\WONDERS\\Documents\\SampleTest.txt", "a") as file:
    file.write(text)

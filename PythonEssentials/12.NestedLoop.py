# nested loop =  is the general concept of having one loop inside another loop

# nested loop = the 'inner loop' will finish all of its iteration before finishing the iteration of the outer loop

# To best demonstrate this we will create a program to draw a rectangle made out of a symbol of our choice

# We need to set a width, height and the symbol choice

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("What symbol would you like to use?: ")

# Now it's time for the nested loop. We're going to create an outer for loop and an inner for loop
# The outer for loop will be in charge of the rows and the inner will be for the columns

for i in range(rows):
    for j in range(columns): # this will be iterated first
        print(symbol, end="") # this will print the symbol once every iteration. Will iterate 'columns' times
        # After we use a print statement the console will starr a new line. We don't want this when defining the columns so we add "end=".

    print() # this will print the symbol once every iteration. Will iterate 'rows' times
            #  We don't want this when defining the rows so we add a print statement that is empty to initiate a new row per iteration.

# How many rows?: 4
# How many columns?: 5
# What symbol would you like to use?: $
# $$$$$
# $$$$$
# $$$$$
# $$$$$

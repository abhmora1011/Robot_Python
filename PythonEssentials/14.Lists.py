# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "Sushi" # Update the value of index 0

food.append("ice cream") # add food on the list
food.remove("hotdog") # remove the hotdog to the list
food.pop() # remove the last element
food.insert(0, "cake") # insert value to a specific index
food.sort() # sort in alphabetical order
food.clear() # remove all the elements

for x in food:
    print(x)

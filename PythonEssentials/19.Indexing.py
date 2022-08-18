# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "Bro code"

# if(name[0].islower()):
#     name = name.capitalize()
#     print(name)

first_name = name[:3].upper() # capitalize the 0 index up to but not included the 3 index
last_name = name[4:].lower() # convert to lowercase the 4th index up to the end index
last_character = name[-1] # access the last index using negative indexing

print(first_name)
print(last_name)
print(last_character)

# BRO
# code
# e
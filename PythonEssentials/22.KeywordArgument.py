# Keyword arguments = arguments preceeded by an indentifier when we pass them to a function
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that a function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last = "Code", middle="Dude", first="Bro") # Not a positional arguments

hello("Code", "Bro", "Dude") # positional arguments

# Hello Bro Dude Code
# Hello Code Bro Dude
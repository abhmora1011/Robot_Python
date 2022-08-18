# Scope = The region that a variable is recognized
# A variable is only available from inside the region it is created
# A global and locally scoped version of a variable can be created

name = "Bro" # global scope (available inside and outside the function)

def display_name():
    name = "Code" # Local scope (available inside this function)
    print(name)

display_name()
print(name)

# Code
# Bro

# L = Local
# E = Enclosing
# G = Global
# B = Built-in

# logical opetators = (and, or, not) = used to check if two or more conditional statements is true

temp = int(input("What us the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today!")
    print("go outside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today!")
    print("stay inside!")

# What us the temperature outside?: 30
# The temperature is good today!
# go outside!

# What us the temperature outside?: 41
# The temperature is bad today!
# stay inside!

#NOT OPERATOR
# What us the temperature outside?: 22
# The temperature is bad today!
# stay inside!
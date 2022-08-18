#  str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)

# {} = format field

print("The {} jumped over the {}".format("cow", "moon"))
print("The {0} jumped over the {1}".format(animal, item)) # positional arguments
print("The {1} jumped over the {0}".format(animal, item)) # positional arguments
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # keyword arguments
print("The {animal} jumped over the {animal}".format(animal="cow", item="moon")) # keyword arguments

# The cow jumped over the moon
# The cow jumped over the moon
# The cow jumped over the moon
# The moon jumped over the cow
# The cow jumped over the moon
# The cow jumped over the cow

print("***************************")

text = "The {} jumped over the {}"
print(text.format("cow", "moon"))
print(text.format(animal, item))

# The cow jumped over the moon
# The cow jumped over the moon

print("***************************")

name = "Bro"

print("My name is {}".format(name))
print("My name is {:<10} nice to meet you".format(name, name)) # <= left align and add some padding
print("My name is {:>10} nice to meet you".format(name, name)) # <= right align
print("My name is {:^10} nice to meet you".format(name, name)) # <= center align

# My name is Bro
# My name is Bro        nice to meet you
# My name is        Bro nice to meet you
# My name is    Bro     nice to meet you

print("***************************")

#str.format() = optional method that gives user more control when displaying output

number = 1000000

print("The number pi is {:.3f}".format(number)) # display first 3 decimal value
print("The number pi is {:,}".format(number)) # add a comma
print("The number pi is {:b}".format(number)) # binary representation
print("The number pi is {:o}".format(number)) # octal
print("The number pi is {:X}".format(number)) # hex
print("The number pi is {:E}".format(number)) # scientific notation

# The number pi is 1000000.000
# The number pi is 1,000,000
# The number pi is 11110100001001000000
# The number pi is 3641100
# The number pi is F4240
# The number pi is 1.000000E+06

# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*args): # * is the most important the args itself can be renamed
    sum = 0
    # args[0] = 0 This is not allowed since the *args is a tuple might as well that you convert first
    # Ex. args = list(args)
    #     args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5))

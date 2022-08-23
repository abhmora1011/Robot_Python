# *********************************
# if __name__ == '__main__'
# *********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the _name_ variable a value of '__main__' if it's
#  the initial module being run

print(__name__)

def main():
    print("Hello!")

if __name__ == '__main__': 
    main()
else:
    print("Running module indirectly")
